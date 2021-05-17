
from tqdm import tqdm

import subprocess

print(" Youtube Downloader ")

inputUrl = input("    Enter Video Url:   ")
command_title = f"youtube-dl -e {inputUrl}"
command_format=f"youtube-dl -F {inputUrl}"


selected_val=int(input("""
    Select the Option
    1 -- Download Video With Different Formats
    2 -- Download Audio Only                       
"""))
titile = (subprocess.check_output(
    command_title.split()).decode('utf-8')).split("\n")
if selected_val==1:
    print(subprocess.check_output(command_format.split()).decode('utf-8'))
    
    selected_format=int(input("""
        Enter The Selected Formated Code         
        """))
    command=f"youtube-dl -f {selected_format} {inputUrl}"
    print(command)
    print(subprocess.run(command.split()))
    
elif selected_val==2:
    print("Downloading Audio......")
    print(subprocess.run(f"youtube-dl -f bestaudio {inputUrl}".split()))
    