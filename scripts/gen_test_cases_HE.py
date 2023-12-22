import json
import os

# load "./dataset/HumanEval.jsonl" file
jsonl_file = open("./dataset/HumanEval.jsonl", "r")
jsonl_lines = jsonl_file.readlines()

# for each question in the jsonl file, read ['test'] key
for idx, line in enumerate(jsonl_lines):
    json_obj = json.loads(line)

    # assert 'test', 'entry_point' key exists
    assert 'entry_point' in json_obj.keys(), "entrypoint key not found"
    assert 'test' in json_obj.keys(), "test key not found"

    # extract 'test', 'entry_point' key
    test = "\ndef check" + json_obj['test'].split("def check")[-1]
    entry_point = json_obj['entry_point']
    print(entry_point, test)

    # if test_cases folder does not exist, create one
    if not os.path.exists("./test_cases/HE"):
        os.mkdir("./test_cases/HE")

    # pad idx into 3 digits
    idx = str(idx).zfill(3)

    # generate test case python file in test_cases folder
    test_case_file = open("./test_cases/HE/" + f"testcase_{idx}" + ".py", "w")
    test_case_file.write(f"from main import {entry_point}\n\n")
    test_case_file.write(f"{test}\n")
    test_case_file.write(f"if __name__ == '__main__':\n")
    test_case_file.write(f"    check({entry_point})")

