import requests
from colorama import *
from time import sleep

def spam(channel_id, friend_id):
    try:
        url = f"https://discord.com/api/v9/channels/{channel_id}/recipients/{friend_id}"
        headers={"Authorization": "DISCORD_TOKEN_HERE"}

        r = requests.put(url, headers=headers)
        id = (r.json()["id"])

        rn = requests.patch(url, headers=headers, json={"name": "x4n on top"})
        for i in range(3):
            m = requests.post(url=f"https://discord.com/api/v9/channels/{id}/messages", headers=headers, data={"content": "@everyone https://discord.gg/y8mMfA796F :joy:"})
        try:
            l = requests.delete(url=f"https://discord.com/api/v9/channels/{id}?silent=true", headers=headers)
        except:
            pass

        print(f"{Fore.RESET}GROUP_ID{Fore.GREEN} ({id}){Fore.RESET} {i}\nStatus For Group: {Fore.GREEN}{r.status_code}\n{Fore.RESET}Status For Message: {Fore.GREEN}{m.status_code}\n{Fore.RESET}Status For Leaving: {Fore.GREEN}{l.status_code}\n{Fore.RESET}Status For Renaming: {Fore.RED}{rn.status_code}\n")

        #while True:
        #    sleep(0.2)
    except:
        print(r.json())
        pass

for i in range(10):
    spam(channel_id=1234, friend_id=1234) # put the channel id of person u wanna spam on channel_id, friend_id for a recipient to add (required)
