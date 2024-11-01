import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ModifyDict import ModifyDict

# In order to change the value of input keys in given dictionary(inputDict) please declare desired outputKeys array.
# The format of outputKeys array should be same as inputKeys array.
# To know the format of inputKeys array run the program once and the format of inputKeys array will be printed.
# If you change the inputDict then format of inputKeys array will also change and you will have to change the format of outputKeys array


class Examples():

    @staticmethod
    def nested_dict_with_non_repetetive_format():
        inputDict = {"Key1": "Value1",
                     "Key2": {"Key21": {"Key211": "Value211",
                                        "Key212": "Value212"},
                              "Key22": "Value22",
                              "Key23": {"Key231": "Value231",
                                        "Key232": "Value232"}
                              }
                     }

        outputKeys = ['KEY1', 'KEY2', ['KEY21', ['KEY211', 'KEY212'],
                                       'KEY22', 'KEY23', ['KEY231', 'KEY232']]]

        inputKeys, inputValues = ModifyDict.get_nested_key_values(inputDict)
        outputDict = ModifyDict.get_nested_dictionary(outputKeys, inputValues)
        print("The format of input keys is :")
        print(inputKeys)
        print("Input dictionary is :")
        print(inputDict)
        print("Output dictionary is :")
        print(outputDict)

    @staticmethod
    def nested_dict_with_repetetive_format():
        inputDict = {"Clone1": {"Key1": "Value1",
                                "Key2": {"Key21": {"Key211": "Value211",
                                                   "Key212": "Value212"},
                                         "Key22": "Value22",
                                         "Key23": {"Key231": "Value231",
                                                   "Key232": "Value232"}
                                         }
                                },
                     "Clone2": {"Key1": "Value1",
                                "Key2": {"Key21": {"Key211": "Value211",
                                                   "Key212": "Value212"},
                                         "Key22": "Value22",
                                         "Key23": {"Key231": "Value231",
                                                   "Key232": "Value232"}
                                         }
                                },
                     "Clone3": {"Key1": "Value1",
                                "Key2": {"Key21": {"Key211": "Value211",
                                                   "Key212": "Value212"},
                                         "Key22": "Value22",
                                         "Key23": {"Key231": "Value231",
                                                   "Key232": "Value232"}
                                         }
                                }
                     }

        outputDictValues = []

        repetetiveFormatKeys, repetetiveFormatValues = list(
            inputDict.keys()), list(inputDict.values())

        i = 0
        while(i < len(repetetiveFormatValues)):
            inputKeys, inputValues = ModifyDict.get_nested_key_values(
                repetetiveFormatValues[i])
            outputKeys = ['KEY1', 'KEY2', ['KEY21', ['KEY211', 'KEY212'],
                                           'KEY22', 'KEY23', ['KEY231', 'KEY232']]]
            outputDictValues.append(
                ModifyDict.get_nested_dictionary(outputKeys, inputValues))
            i += 1

        outputDict = dict(zip(repetetiveFormatKeys, outputDictValues))

        print("Input Dictionary is :")
        print(inputDict)
        print("Output Dictionary is :")
        print(outputDict)
