import os
import shutil

# testing datasets
testing_datasets = ["HE", "HE_ET", "MBPP", "MBPP_ET"]

# run evaluation on each dataset
for dataset in testing_datasets:
    # list all corresponding dataset case folders and sort
    if dataset == "HE" or dataset == "HE_ET":
        case_folder = "HE"
    else:
        case_folder = "MBPP"
    folders = os.listdir(case_folder)
    folders.sort()

    # for each project in dataset, run main.py inside, save success/failure in a list
    success = []
    failure = []
    for folder in folders:
        # enter project folder
        project_folder = os.path.join(f"{os.environ['PWD']}", f"{case_folder}", folder)
        os.chdir(project_folder)

        # find test case file
        case_number = folder.split("_")[1]
        test_case_file = os.path.join(f"{os.environ['PWD']}", "test_cases", f"{dataset}", f"testcase_{case_number}.py")
        
        # copy test file to project folder
        shutil.copy2(test_case_file, os.path.join(project_folder, f"testcase_{dataset}_{case_number}.py"))

        # run test file
        run_code = os.system(f"python testcase_{dataset}_{case_number}.py")
        if run_code == 0:
            print(f"\033[92m{case_number} success\033[0m")
            success.append(case_number)
        else:
            print(f"\033[91m{case_number} failure\033[0m")
            failure.append(case_number)

    # print success/failure
    print(f"Dataset: {dataset}:")
    print(f"success: {success}")
    print(f"failure: {failure}")
    os.chdir(os.environ['PWD'])
