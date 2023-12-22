import os
import shutil

# list all folders in folder "HE" and sort
folders = os.listdir("HE")
folders.sort()

print(folders[:10])

# for each project in "HE", run main.py inside, save success/failure in a list
success = []
failure = []
for folder in folders[:20]:
    # enter project folder
    project_folder = os.path.join(f"{os.environ['PWD']}", "HE", folder)
    os.chdir(project_folder)

    # find test case file
    case_number = folder.split("_")[1]
    test_case_file = os.path.join(f"{os.environ['PWD']}", "test_cases", f"case_{case_number}.py")
    
    # copy test file to project folder
    shutil.copy(test_case_file, project_folder)

    # run test file
    run_code = os.system(f"python case_{case_number}.py")
    if run_code == 0:
        print(f"\033[92m{case_number} success\033[0m")
        success.append(case_number)
    else:
        print(f"\033[91m{case_number} failure\033[0m")
        failure.append(case_number)

# print success/failure
print(success)
print(failure)
