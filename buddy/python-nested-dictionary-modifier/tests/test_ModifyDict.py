import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ModifyDict import ModifyDict


class Test_ModifyDict():

    def test_get_nested_key_values(self):
        input_dict = {'Key1': 'Value1', 'Key2': {'Key21': {'Key211': 'Value211', 'Key212': 'Value212'},
                                                 'Key22': 'Value22', 'Key23': {'Key231': 'Value231', 'Key232': 'Value232'}}}
        expected_value = ['Key1', 'Key2', [
            'Key21', ['Key211', 'Key212'], 'Key22', 'Key23', ['Key231', 'Key232']]]
        actual_value = ModifyDict.get_nested_key_values(input_dict)
        assert expected_value == actual_value[0]

    def test_get_nested_dictionary(self):
        input_dict = {"Key1": "Value1",
                      "Key2": {"Key21": {"Key211": "Value211",
                                         "Key212": "Value212"},
                               "Key22": "Value22",
                               "Key23": {"Key231": "Value231",
                                         "Key232": "Value232"}
                               }
                      }
        output_keys = ['KEY1', 'KEY2', ['KEY21', ['KEY211', 'KEY212'],
                                        'KEY22', 'KEY23', ['KEY231', 'KEY232']]]
        expected_value = {'KEY1': 'Value1', 'KEY2': {'KEY21': {'KEY211': 'Value211', 'KEY212': 'Value212'},
                                                     'KEY22': 'Value22', 'KEY23': {'KEY231': 'Value231', 'KEY232': 'Value232'}}}
        input_keys, input_values = ModifyDict.get_nested_key_values(input_dict)
        actual_value = ModifyDict.get_nested_dictionary(
            output_keys, input_values)
        assert expected_value == actual_value
