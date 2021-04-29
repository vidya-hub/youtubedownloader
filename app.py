# import pyfiglet
from tqdm import tqdm
# ascii_banner = pyfiglet.figlet_format("Youtube Url => MP3")
# print(ascii_banner)
import subprocess
# import re
import requests
# print(
# """
#   __   __          _         _            _   _      _   _____       __  __      _____ 
#   \ \ / /__  _   _| |_ _   _| |__   ___  | | | |_ __| | |_   _|__   |  \/  |_ __|___ / 
#    \ V / _ \| | | | __| | | | '_ \ / _ \ | | | | '__| |   | |/ _ \  | |\/| | '_ \ |_ \ 
#     | | (_) | |_| | |_| |_| | |_) |  __/ | |_| | |  | |   | | (_) | | |  | | |_) |__) |
#     |_|\___/ \__,_|\__|\__,_|_.__/ \___|  \___/|_|  |_|   |_|\___/  |_|  |_| .__/____/ 
#                                                                            |_|         
 
# """
# )
inputUrl=input("    Enter Video Url:   ")
command_url = f"youtube-dl -g {inputUrl}"
command_title = f"youtube-dl -e {inputUrl}"
titile = (subprocess.check_output(
    command_title.split()).decode('utf-8')).split("\n")
url = (subprocess.check_output(command_url.split()).decode('utf-8')).split("\n")
file_size_request = requests.get(url[1], stream=True)
file_size = int(file_size_request.headers['Content-Length'])
print(file_size)
block_size = 1024 
filename = f"{titile[0]}.mp3"
t=tqdm(total=file_size, unit='A', unit_scale=True, desc=str(filename))
with open(filename , 'wb') as f:
    for data in file_size_request.iter_content(block_size):
        t.update(len(data))
        f.write(data)
t.close()
print("Audio downloaded successfully")
# subprocess.check_output(['wget', '-O', f"{titile[0]}.mp3", url[1]])