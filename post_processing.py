import os
import shutil

folder_path = "./HE"

# Iterate over all subfolders
for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    
    # Check if the subfolder is a directory
    if os.path.isdir(subfolder_path):
        prefix_files = {}
        
        # Find all files matching the "_ori.py" pattern
        ori_files = [file for file in os.listdir(subfolder_path) if file.endswith("_ori.py")]
        
        # Group the files by prefix
        for ori_file in ori_files:
            prefix = ori_file.split("_ori.py")[0]
            prefix_files.setdefault(prefix, []).append(ori_file)
        
        # Process each prefix
        for prefix, files in prefix_files.items():
            mod_files = [file for file in os.listdir(subfolder_path) if file.startswith(prefix + "_Mod")]
            
            # Sort the mod_files in descending order
            mod_files.sort(reverse=True)
            
            # Copy the appropriate file based on the conditions
            if mod_files:
                shutil.copy2(os.path.join(subfolder_path, mod_files[0]), os.path.join(subfolder_path, f"{prefix}.py"))
            elif files:
                shutil.copy2(os.path.join(subfolder_path, files[0]), os.path.join(subfolder_path, f"{prefix}.py"))
