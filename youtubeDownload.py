import subprocess

print(" Youtube Downloader ")

inputUrl = input("    Enter Video Url:   ")
command_title = f"youtube-dl -e {inputUrl}"
command_format = f"youtube-dl -F {inputUrl}"
title = (subprocess.check_output(
    command_title.split()).decode('utf-8')).split("\n")
print(title[0])
selected_val = int(input("""

    1 -- Download Video With Different Formats
    2 -- Download Audio Only       
                    
    Select the Option :   """))

if selected_val == 1:
    res = (subprocess.check_output(
        command_format.split()).decode('utf-8').split("\n"))
    for data in res[3:]:
        try:
            print(data.split()[0] + " ==> " +
                data.split()[2]+" "+data.split()[3] +" -- "+data.split()[len(data.split())-1])
        except:
            print("")
    selected_format = int(input("""
    Enter The Selected Formated Code         
    """))
    command = f"youtube-dl -f {selected_format} {inputUrl}"
    print(command)
    # try:
    print(subprocess.run(command.split()))

elif selected_val == 2:
    print("Downloading Audio......")
    print(subprocess.run(f"youtube-dl -f bestaudio {inputUrl}".split()))
