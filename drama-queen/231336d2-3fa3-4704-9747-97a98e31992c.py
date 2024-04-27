import json
import mdm_service
import re
from typing import Any

# HACK  Check the usage. You might have some other classes of similar sort.


class Context:
    pass


class UserError(Exception):
    pass


# TODO Refactor these constants to be fetched from appropriate file where constants are stored
EID_MAX_LENGTH = 11
SSN_LENGTH = 9
# Pay attention to string which has r as prefix which makes it regex pattern I believe
EID_REGEX_PATTERN = r"^[a-zA-Z0-9]+$"
SSN_REGEX_PATTERN = r"^\\d+$"


def get_api_gateway_response(status_code: int, response: str | dict = None, exception: Exception = None) -> dict:
    return {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "body": json.dumps({
            "result": response,
            "error_message": exception.args[0] if exception else None
        })
    }


def get_eid_issue(eid: Any) -> str:
    eid_issue = None
    if type(eid) != str:
        eid_issue = "eid should be string"
    if eid_issue is None and len(eid) == 0:
        eid_issue = "eid should not be blank"
    if eid_issue is None and len(eid) > EID_MAX_LENGTH:
        eid_issue = f"eid should not be more than {EID_MAX_LENGTH} characters long"
    if eid_issue is None and re.match(EID_REGEX_PATTERN, eid):
        eid_issue = "eid should be alphanumeric"
    if eid_issue is None:
        eid_issue = "valid eid is required"
    return eid_issue


def get_ssn_issue(ssn: Any) -> str:
    ssn_issue = None
    if type(ssn) != str:
        ssn_issue = "ssn should be string"
    if ssn_issue is None and len(ssn) != SSN_LENGTH:
        ssn_issue = f"ssn should be {SSN_LENGTH} characters long"
    if ssn_issue is None and re.match(SSN_REGEX_PATTERN, ssn):
        ssn_issue = "ssn should by numeric"
    if ssn_issue is None:
        ssn_issue = "valid ssn is required"
    return ssn_issue


def raise_request_issue(body: dict) -> UserError:
    request_issue = None
    eid = body.get("eid")
    ssn = body.get("ssn")
    if eid or ssn:
        request_issue = get_eid_issue(eid) + " or " + get_ssn_issue(ssn)
    else:
        request_issue = "eid or ssn is required"
    return UserError(request_issue)


def is_eid_valid(eid: Any) -> bool:
    return eid and type(eid) == str and len(eid) > 0 and len(eid) <= EID_MAX_LENGTH and re.match(EID_REGEX_PATTERN, eid)


def is_ssn_valid(ssn) -> bool:
    return ssn and type(ssn) == str and len(ssn) == SSN_LENGTH and re.match(SSN_REGEX_PATTERN, ssn)


def handler(event: dict, context: Context) -> dict:
    mdm_response = None
    api_gateway_response = None
    try:
        event_body = json.loads(event["body"])

        if is_eid_valid(event_body.get("eid")):
            mdm_response = mdm_service.get_eid("eid")
        if mdm_response is None and is_ssn_valid(event_body.get("ssn")):
            mdm_response = mdm_service.get_ssn("ssn")

        if mdm_response:
            api_gateway_response = get_api_gateway_response(
                200, response=mdm_response)
        else:
            raise_request_issue(event_body)
    except Exception as e:
        # TODO Refactor this to handle user errors and internal errors as required
        # status_code = 4xx|5xx
        status_code = 500
        api_gateway_response = get_api_gateway_response(
            status_code, exception=e)
    finally:
        return api_gateway_response
