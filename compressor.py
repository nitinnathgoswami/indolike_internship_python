# Simple file compression tool using pthon inbuilt module "zipfile"
# Intern Name:NITIN NATH GOSWAMI
# Intern id:217256425
# Internship Task for @indolike
# Different Emojies picked From @emojiepedia.org
# This tool is for multiple files 

import zipfile
import os

def compress_files(file_list,zip_name):
    #creating Zip files
    with zipfile.ZipFile(zip_name,'w')as zipf:
        for file_path in file_list:
            if os.path.exists(file_path):
                zipf.write(file_path,os.path.basename(file_path))
                print(f"✅ Added:{file_path}")
            else:
                print(f"❌ Skipped(not found):{file_path}")
    
    print(f"\n 🎉All files zipped into :{zip_name}")      
    
#Main  🎯🎯
print("---- File Compression Tool----") 
file_list=[]
while True:
    path=input("Enter file path (or type 'done' to finish):").strip()
    if path.lower()=='done':
        break
    FileExistsError.append(path)
    
if file_list:
    zip_name=input("Enter a name for your Zip file(e.g., my_files.zip):").strip()
    compress_files(file_list,zip_name)
else:
    print("⚠️ No files entered. Exiting!")     
    
#How to use this tool
#------------------------------
# Run the script
# Enter the file path(full path or just the name if in the same folder)
# Type 'DONE' when you've added the files
# Name your zip file
# ✅ All selected files will be zipped into one archieve           