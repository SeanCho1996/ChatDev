import json
import errno
import os
os.environ["OPENAI_API_KEY"] = "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"
from run import main as ChatDevMain

# set openai api key

dataset = "HE"

# choose dataset, get corresponding dataset config
if dataset == "HE":
    dataset_file = "./dataset/HumanEval.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
elif dataset == "HE-E":
    dataset_file = "./dataset/HumanEval_Extend.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
elif dataset == "MBPP":
    dataset_file = "./dataset/MBPP.jsonl"
elif dataset == "MBPP-E":
    dataset_file = "./dataset/MBPP_Extend.jsonl"
else:
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), dataset)

# load all questions
questions = []
with open(dataset_file, "r") as f:
    for line in f:
        data = json.loads(line)
        questions.append(data)

# extract question and run ChatDev
flag = False
for i in questions[:2]:
    question = i[question_key]
    test_cases = i[test_key]
    task_id = i[task_id_key].split("/")[-1]
    print(question)
    print(test_cases)
    
    task = f"""Finish the following function delimited by triple quotes:\
        \"\"\"{question}\"\"\"
        """
    name = f"ChatDev-{task_id}"
    ChatDevMain(task=task, name=name, save_folder=dataset)
