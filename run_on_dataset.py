import os
import sys
sys.path.append(f"{os.environ['PWD']}")
import json
import errno
with open("./api_key", "r") as f:
    api_key = f.read()
os.environ["OPENAI_API_KEY"] = api_key
from run import main as ChatDevMain

# set openai api key

dataset = "MBPP"

# choose dataset, get corresponding dataset config
if dataset == "HE":
    dataset_file = "./dataset/HumanEval.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
elif dataset == "MBPP":
    dataset_file = "./dataset/MBPP.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
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
for i in questions[:10]:
    question = i[question_key]
    test_cases = i[test_key]
    task_id = str(i[task_id_key])
    print(question)
    print(test_cases)
    
    task = f"""{question}
        """
    name = f"ChatDev_{task_id}"
    ChatDevMain(task=task, name=name, save_folder=dataset)
