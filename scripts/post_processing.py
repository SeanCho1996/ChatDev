import os
import shutil
import re

folder_path = "./HE"

# Iterate over all subfolders
for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    
    # Check if the subfolder is a directory
    if os.path.isdir(subfolder_path):
        prefix_files = {}
        
        # check if there are any files name with "*_Mod*.py"
        mod_files = [file for file in os.listdir(subfolder_path) if re.match(r".*_Mod.*\.py", file)]

        # if there are, find their prefixes
        if mod_files:
            for mod_file in mod_files:
                prefix = mod_file.split("_Mod")[0]
                prefix_files.setdefault(prefix, []).append(mod_file)
            # find the last modified file for each prefix
            for prefix, files in prefix_files.items():
                files.sort(reverse=True)
                shutil.copy2(os.path.join(subfolder_path, files[0]), os.path.join(subfolder_path, f"{prefix}.py"))
        else:
            # if there are no files name with "*_Mod*.py", find the original files and copy them
            ori_files = [file for file in os.listdir(subfolder_path) if re.match(r".*_ori\.py", file)]
            for ori_file in ori_files:
                shutil.copy2(os.path.join(subfolder_path, ori_file), os.path.join(subfolder_path, ori_file.split("_ori.py")[0] + ".py")) 

