import json
import os

# open "MBPP.jsonl" file in "dataset" folder
jsonl_file = open("./dataset/MBPP.jsonl", "r")
jsonl_lines = jsonl_file.readlines()

# for each question in the json list, read "test_list" key
for idx, line in enumerate(jsonl_lines):
    json_obj = json.loads(line)

    # assert 'test', 'entry_point' key exists
    assert 'entry_point' in json_obj.keys(), "entrypoint key not found"
    assert 'test' in json_obj.keys(), "test key not found"

    # extract 'test', 'entry_point' key
    test = json_obj['test']
    entry_point = json_obj['entry_point']
    print(entry_point, test)

    # if test_cases folder does not exist, create one
    if not os.path.exists("./test_cases/MBPP"):
        os.mkdir("./test_cases/MBPP")

    # pad idx into 3 digits
    task_id = json_obj['task_id']

    # generate test case python file in test_cases folder
    test_case_file = open("./test_cases/MBPP/" + f"testcase_{task_id}" + ".py", "w")
    test_case_file.write(f"from main import {entry_point}\n\n")
    test_case_file.write(f"{test}\n")
    test_case_file.write(f"if __name__ == '__main__':\n")
    test_case_file.write(f"    check({entry_point})")
