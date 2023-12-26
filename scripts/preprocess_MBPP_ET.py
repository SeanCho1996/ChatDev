import json
import os


# load "./dataset/ori_MBPP_ET.jsonl" and "./dataset/MBPP.jsonl" file
jsonl_file = open("./dataset/ori_MBPP_ET.jsonl", "r")
jsonl_lines = jsonl_file.readlines()
jsonl_file2 = open("./dataset/MBPP.jsonl", "r")
jsonl_lines2 = jsonl_file2.readlines()
new_jsonl_file = open("./dataset/MBPP_ET.jsonl", "w")

# for each line in jsonl_lines2, find the corresponding line in jsonl_lines
for idx, line in enumerate(jsonl_lines2):
    ref_obj = json.loads(line)
    ori_task_id = ref_obj['ori_task_id']
    
    json_obj = json.loads(jsonl_lines[int(ori_task_id) - 1])
    assert json_obj['task_id'] == int(ori_task_id), "task_id not match"

    # reset task_id
    task_id = ref_obj['task_id']

    # assert 'code' key exists
    assert 'code' in json_obj.keys(), "code key not found"
    # extract 'code' key
    code = json_obj['code']
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
    assert 'test_list' in json_obj.keys(), "test_list key not found"
    # change test_list to python test code
    test = "\ndef check(candidate):\n"
    for i in json_obj['test_list']:
        i = i.replace(entry_point, "candidate")
        test += f"    {i}\n"

    # assert 'text' key exists
    assert 'text' in json_obj.keys(), "text key not found"
    # extract 'text' key
    prompt = json_obj['text']
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
    new_jsonl_file.write(json.dumps(new_dict) + "\n")