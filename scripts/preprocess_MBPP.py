import json
import os


# load "./dataset/santinized-mbpp.json" file
json_file = open("./dataset/sanitized-mbpp.json", "r")
json_obj = json.load(json_file)

# create a jsonl file to store processed data
jsonl_file = open("./dataset/MBPP.jsonl", "w")

# for each question in the json list, read "code" key
for idx, line in enumerate(json_obj):
    # reset task_id
    task_id = str(idx).zfill(3)
    ori_task_id = line['task_id']

    # assert 'code' key exists
    assert 'code' in line.keys(), "code key not found"
    # extract 'code' key
    code = line['code']
    # check if there is only one "def " in the code
    if code.count("def ") != 1:
        # find the last "def " in the code and set it as entry point
        entry_point = code.split("def ")[-1].split("(")[0]
        function_signature = code.split("def ")[-1].split(":")[0]
    else:
        # set the only "def " in the code as entry point
        entry_point = code.split("def ")[1].split("(")[0]
        function_signature = code.split("def ")[1].split(":")[0]

    # assert 'test_list' key exists
    assert 'test_list' in line.keys(), "test_list key not found"
    # change test_list to python test code
    test = "\ndef check(candidate):\n"
    for i in line['test_list']:
        i = i.replace(entry_point, "candidate")
        test += f"    {i}\n"

    # assert 'prompt' key exists
    assert 'prompt' in line.keys(), "prompt key not found"
    # extract 'prompt' key
    prompt = line['prompt']
    # add function signature to prompt
    prompt += f"\nThe function signature is: {function_signature}\n"

    # write all extracted information to a new dict
    new_dict = {
        "task_id": task_id,
        "ori_task_id": ori_task_id,
        "prompt": prompt,
        "entry_point": entry_point,
        "test": test
    }

    # write the new dict to jsonl file as a new line
    jsonl_file.write(json.dumps(new_dict) + "\n")

