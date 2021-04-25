import subprocess

inputUrl=input("    Enter Video Url:   ")
command_url = f"youtube-dl -g {inputUrl}"
command_title = f"youtube-dl -e {inputUrl}"
titile = (subprocess.check_output(
    command_title.split()).decode('utf-8')).split("\n")
url = (subprocess.check_output(command_url.split()).decode('utf-8')).split("\n")
subprocess.check_output(['wget', '-O', f"{titile[0]}.mp3", url[1]])