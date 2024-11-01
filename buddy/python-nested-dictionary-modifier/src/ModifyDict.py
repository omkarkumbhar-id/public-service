class ModifyDict():

    @staticmethod
    def get_nested_key_values(input_dict: dict) -> tuple:
        Keys, Values = list(input_dict.keys()), list(input_dict.values())
        i = 0
        while(i < len(Values)):
            if type(Values[i]) == dict:
                nestedKeys, nestedValues = ModifyDict.get_nested_key_values(Values[i])
                Keys.insert(i+1, nestedKeys)
                Values.pop(i)
                Values.insert(i, nestedValues)
                Values.insert(i, "(%)")
                i += 1
            i += 1
        return Keys, Values

    @staticmethod
    def get_nested_dictionary(keys: list, values: list) -> dict:
        i = 0
        while(i < len(values)):
            if values[i] == "(%)":
                nestedDict = ModifyDict.get_nested_dictionary(keys[i+1], values[i+1])
                keys.pop(i+1)
                values.pop(i)
                values.pop(i)
                values.insert(i, nestedDict)
            i += 1
        return dict(zip(keys, values))
