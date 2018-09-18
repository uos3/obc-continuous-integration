import requests
import os.path
#from git import Repo

# load file and get git repo name
git_repo = 'https://github.com/uos3/obc-firmware.git'

# find latest commit on master


# compare to previous commit stored in logs
r = requests.get('https://api.github.com/repos/uos3/obc-firmware/commits')
online_commit = r.json()[0]["sha"]
offline_commit = ""

#os.path.isfile(fname)
with open("logs/latest-commit", 'r') as file:
    offline_commit = file.readline()
print("offline_commit", offline_commit)

if not online_commit == offline_commit:
    with open("logs/latest-commit", 'w') as file:
        file.write(online_commit)

    # Create temporary file
    with open("logs/NEW-COMMIT", 'w') as file:
        file.write(" ")
