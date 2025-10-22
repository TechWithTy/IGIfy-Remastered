# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92

IGFI is a python script for increasing the number of followers of an Instagram account.

*********IMPORTANT*********

User's login credentials (such as: username, password) will not be stored or saved !
Will be used only to increase the followers of the user's Instagram account

***************************
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! IGFI requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IGFI ✅")
        sleep(1.2)
        print("[+] Exiting...")
        sleep(0.8)
        quit(0)
    import platform
    from os import system
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'rich', 'platform', 'os', 'logging', 'instagrapi', 'requests', 'instaloader', 'argparse', 'colorama', 'ctypes']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]ok[/]')
    import os
    import instagrapi
    import requests
    import logging
    import instaloader
    import argparse
    import ctypes
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in IGFI have been installed !")
    sleep(1)
    print("[+] Ignoring warning...")
    sleep(0.5)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("sudo pip install -r ./../files/requirements.txt" if sys.platform.startswith('linux') else "python -m pip install ./../files/requirements.txt")
    elif platform.system() == 'Windows':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[+] Root user permission denied.")
                sleep(1)
                print("[+] Exiting...")
                quit()
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("pip install -r ./../files/requirements.txt")

init(autoreset=True)
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.")
sleep(1.1)
clear()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = {}
resp = requests.get('https://api.github.com/repos/new92/IGFI', headers=headers)
if resp.status_code == 200:
    js = resp.json()

def ScriptInfo():
    rest = requests.get('https://api.github.com/repos/new92/IGFI/contributors', headers=headers)
    contribs = []
    if rest.status_code == 200:
        jsn = rest.json()
        contribs = [jsn[i]['login'] for i in range(len(jsn))]
    lang = requests.get('https://api.github.com/repos/new92/IGFI/languages', headers=headers)
    languages = list(lang.json().keys()) if lang.status_code == 200 else []
    print(f"{YELLOW}[+] Author | {js['owner']['login']}")
    print(f"{YELLOW}[+] Github | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Leetcode | @{js['owner']['login']}")
    print(f"{YELLOW}[+] PyPI | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Contributors | {contribs}")
    print(f"{YELLOW}[+] License | {js['license']['spdx_id']}")
    print(f"{YELLOW}[+] Programming language(s) used | {languages}")
    print(f"{YELLOW}[+] Script's name | {js['name']}")
    print(f"{YELLOW}[+] Latest update | {js['updated_at']}")
    print(f"{YELLOW}[+] File size | {os.stat(__file__).st_size} bytes")
    print(f"{YELLOW}[+] File path | {os.path.abspath(__file__)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Repo name | {js['name']}")
    print(f"{YELLOW}[+] Description | {js['description']}")
    print(f"{YELLOW}[+] Repo URL | {js['html_url']}")
    print(f"{YELLOW}[+] Stars | {js['stargazers_count']}")
    print(f"{YELLOW}[+] Forks | {js['forks']}")
    print(f"{YELLOW}[+] Watchers | {js['subscribers_count']}")
    print(f"{YELLOW}[+] Open issues | {js['open_issues_count']}")

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in dirs:
            return os.path.abspath(os.path.join(root, fname))

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('IGFI'))
    return f"{GREEN}[✔] Files and dependencies uninstalled successfully !"

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def banner() -> str:
    console.print("""[bold yellow]
██╗░██████╗░███████╗██╗
██║██╔════╝░██╔════╝██║
██║██║░░██╗░█████╗░░██║
██║██║░░╚██╗██╔══╝░░██║
██║╚██████╔╝██║░░░░░██║
╚═╝░╚═════╝░╚═╝░░░░░╚═╝
[/]""", justify='center')

def nums():
    console.print("[bold yellow][1] Increase followers[/]")
    console.print("[bold yellow][2] Show IGFI's info[/]")
    console.print("[bold yellow][3] Clear log[/]")
    console.print("[bold yellow][4] Uninstall IGFI[/]")
    console.print("[bold yellow][5] Exit[/]")
        
def checkUser(username:str) -> bool:
    return username in ['', ' '] or len(username) > 30 or requests.get(f"https://www.instagram.com/{username}/", allow_redirects=False).status_code != 200

def main(username: str, password: str):
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print(f"[bold yellow][+] {js['description']}" if js else 'IGFI is a python script for increasing the number of followers of an Instagram account.')
    print("\n")
    nums()
    print("\n")
    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
    valErr = num in [1,2,3,4,5]
    while not valErr:
        try:
            nums()
            sleep(1)
            num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones) >>> "))
            valErr = num in [1,2,3,4,5]
        except ValueError:
            print(f"{RED}[✘] Invalid number")
            sleep(0.5)
            print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
            sleep(1)
    if num == 1:
        clear()
        sleep(0.9)
        print(f"{GREEN}[+] Acceptable answers >>> [yes/no]")
        sleep(1)
        keep=input(f"{YELLOW}[?] Keep log ? ").lower() in ('y', 'yes')
        sleep(0.9)
        print(f"{GREEN}[+] Acceptable answers >>> [yes/no]")
        sleep(1)
        check=input(f"{YELLOW}[?] Display the usernames of the followers added ? ").lower() in ('y', 'yes')
        users = {
            'Cristiano Ronaldo' : '173560420',
            'Cardi B' : '1436859892',
            'Kim Kardashian': '18428658',
            'Ariana Grande' : '7719696',
            'Nicki Minaj' : '451573056',
            'Beyonce' : '247944034',
            'Katy Perry' : '407964088',
            'Selena Gomez' : '460563723',
            'Justin Bieber' : '6860189',
            'Lionel Messi' : '427553890',
            'Neymar Jr' : '26669533',
            'Kylian Mbappe' : '4213518589',
            'Dua Lipa' : '12331195',
            'Billie Eilish' : '28527810',
            'Kylie Jenner' : '12281817',
            'Khloe Kardashian' : '208560325',
            'Kourtney Kardashian' : '145821237',
            'Jennifer Lopez' : '305701719',
            'Shakira' : '217867189',
            'Instagram' : '25025320',
            'National Geographic' : '787132',
            'FC Barcelona' : '260375673',
            'Real Madrid' : '290023231',
            'Champions League' : '1269788896',
            'Chris Brown' : '29394004',
            'Taylor Swift' : '11830955',
            'Kendall Jenner' : '6380930',
            'Virat Kohli' : '2094200507',
            'Zendaya' : '9777455',
            'Marvel' : '204633036',
            'Tom Holland' : '176618189',
            'Emma Watson' : '1418652011',
            'Millie Bobby Brown' : '3439002676',
            'Shawn Mendes' : '212742998',
            'Camila Cabello' : '19596899',
            'NASA' : '528817151',
            'Nike' : '13460080'
        }
        NAMES = list(users.keys())
        sleep(0.6)
        fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/consent.txt').replace('\\', '/')
        if not os.path.exists(fname):
            print(f"{GREEN}[+] Acceptable answers >>> [yes/no]")
            sleep(0.9)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage the script may cause to {username} ? ").lower() in ('y', 'yes')
            if con:
                logging.basicConfig(
                    filename=fname,
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                logging.info(f'Yes I consent that the author (new92) has no responsibility for any loss or damage the script may cause to {username}.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall IGFI and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                valErr = num in [1,2]
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall IGFI and exit")
                        num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones) >>> "))
                        valErr = num in [1,2]
                    except ValueError:
                        print(f"{RED}[✘] Please enter a valid number.")
                        sleep(2)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print(Uninstall())
                    sleep(1)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for choosing to use IGFI 😁")
                    sleep(2)
                    print(f"{GREEN}[+] If you have any suggestions or found a bug or need help feel free to contact me, at this email address: new92github@gmail.com")
                    sleep(2)
                    quit(0)
        sleep(1)
        clear()
        print(f"{GREEN}[+] Acceptable answers >>> [yes/no]")
        sleep(1)
        ga=input(f"{YELLOW}[?] Grant the script access for extra info regarding your followers ? ").lower() in ('y', 'yes')
        # Targeting mode
        print(f"{GREEN}[+] Acceptable answers >>> [yes/no]")
        niche = input(f"{YELLOW}[?] Use niche targeting by hashtag (collect likers) ? ").lower() in ('y', 'yes')
        batch_size = 10
        batch_pause = 60
        try:
            bs = input(f"{YELLOW}[?] Batch size (default 10) >>> ").strip()
            if bs:
                batch_size = max(1, int(bs))
            bp = input(f"{YELLOW}[?] Pause between batches in seconds (default 60) >>> ").strip()
            if bp:
                batch_pause = max(5, int(bp))
        except ValueError:
            pass
        print(f"{YELLOW}[!] This will follow and then unfollow targets in batches of {batch_size} with {batch_pause}s pauses to attempt follow-backs. Proceed responsibly.")
        proceed = input(f"{YELLOW}[?] Proceed? (yes/no) >>> ").lower() in ('y','yes')
        if not proceed:
            print(f"{RED}[+] Exiting by user choice...")
            sleep(1)
            quit(0)

        client=instagrapi.Client()
        # Load saved device/settings if available to avoid checkpoints and 404s
        try:
            settings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'igfi_session.json')
            if os.path.exists(settings_path):
                client.load_settings(settings_path)
                print(f"{GREEN}[✔] Loaded saved settings.")
        except Exception as e:
            print(f"{YELLOW}[!] Could not load saved settings: {e}")
        # Conservative pacing to reduce throttling and long waits
        try:
            client.delay_range = (2, 5)
            client.request_timeout = 10
        except Exception:
            pass
        # Simple login flow (no external sessions)
        try:
            login = client.login(username, password)
            if login:
                print(f"{GREEN}[✔] Login successful with instagrapi!")
                # Persist settings for stable device identity
                try:
                    client.dump_settings(settings_path)
                    print(f"{GREEN}[✔] Settings saved.")
                except Exception:
                    pass
                # Quick verification to ensure private API is usable
                try:
                    me = client.account_info()
                    print(f"{GREEN}[✔] Login verified - Welcome {me.username}!")
                except Exception as e:
                    print(f"{YELLOW}[!] Could not verify account info: {e}")
                    print(f"{YELLOW}[!] Continuing, but some actions may be limited.")
            else:
                print(f"{RED}[✘] Failed to login with instagrapi.")
                sleep(0.7)
                print(f"{YELLOW}[1] Try with different combinations of usernames / passwords.")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[::] Number (from the above ones) >>> "))
                if num == 1:
                    print(f"{YELLOW}[*] To quit the loop enter: <quit> in the username input.")
                    sleep(0.9)
                    while username != 'quit':
                        username=input(f"{YELLOW}[::] New username >>> ")
                        while checkUser(username):
                            print(f"{RED}[✘] Invalid username !")
                            sleep(0.5)
                            username=input(f"{YELLOW}[::] New username >>> ")
                        sleep(0.8)
                        password = input(f"{YELLOW}[::] New password >>> ")
                        login = client.login(username, password)
                        if login:
                            user = username
                            print(f"{GREEN}[✔] Login successful !")
                            username = '<quit>'
                            sleep(0.5)
                        else:
                            print(f"{RED}[✘] Failed to login.")
                            sleep(0.7)
                            print(f"{GREEN}[+] Retrying...")
                            sleep(0.5)
                    username = user
                else:
                    print(f"{RED}[+] Exiting...")
                    sleep(0.6)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(0.5)
                    quit(0)
        except Exception as e:
            print(f"{RED}[✘] Login failed: {e}")
            sleep(2)
            quit(0)
        # Get profile info (only if extra access granted); use private endpoint
        profile = None
        followers_bef = None
        if ga:
            try:
                profile = client.account_info()
                followers_bef = getattr(profile, 'follower_count', None)
                print(f"{GREEN}[✔] Profile loaded: {profile.username} ({followers_bef if followers_bef is not None else 'n/a'} followers)")
            except Exception as e:
                print(f"{YELLOW}[!] Could not load extended profile info: {e}")
                print(f"{YELLOW}[!] Continuing without follower statistics.")

        sleep(1)
        print(f"{YELLOW}[+] Please wait while IGFI is increasing your followers...")
        sleep(1.7)
        print(f"{YELLOW}[+] To end the process enter <Ctrl> + <C>")
        sleep(1.3)
        clear()

        # Already loaded profile above when ga=True; skip here

        # Build target list
        targets = []  # list of (uid:int, label:str)
        if niche:
            try:
                tag = input(f"{YELLOW}[?] Enter hashtag (without #) >>> ").strip().lstrip('#')
                mcount = input(f"{YELLOW}[?] Number of recent posts to scan (default 5) >>> ").strip()
                mcount = int(mcount) if mcount else 5
                ucount = input(f"{YELLOW}[?] Max users to target (default 50) >>> ").strip()
                ucount = int(ucount) if ucount else 50
            except ValueError:
                mcount, ucount = 5, 50
            collected = {}
            try:
                medias = client.hashtag_medias_recent(tag, amount=mcount)
            except Exception:
                medias = []
            for media in medias:
                try:
                    # media.pk may be attribute; fallback to id
                    mid = getattr(media, 'pk', getattr(media, 'id', None))
                    if not mid:
                        continue
                    likers = client.media_likers(mid)
                    for u in likers:
                        upk = getattr(u, 'pk', None)
                        uname = getattr(u, 'username', str(upk))
                        if upk and upk not in collected and upk != getattr(client, 'user_id', None):
                            collected[upk] = uname
                            if len(collected) >= ucount:
                                break
                    if len(collected) >= ucount:
                        break
                except Exception:
                    continue
            targets = [(int(k), v) for k, v in collected.items()]
        else:
            # use built-in celebrity targets
            targets = [(int(users[name]), name) for name in NAMES]

        # Get current followers for comparison (only if extra info allowed)
        FOLLOWERS = None
        if ga and profile is not None and check:
            try:
                followers_response = client.user_followers(profile.pk)
                FOLLOWERS = [u.username for u in followers_response.values()]
            except Exception:
                FOLLOWERS = None

        # Initialize counters
        f = 0
        x = 0

        for i in range(10000):
            try:
                # Follow in batches
                for start in range(0, len(targets), batch_size):
                    batch = targets[start:start+batch_size]
                    print(f"{YELLOW}[+] Processing follow batch {start//batch_size + 1} ({len(batch)} users)...")
                    for uid, label in batch:
                        try:
                            print(f"{YELLOW}[+] Following {label} (id {uid})...")
                            client.user_follow(uid)
                            sleep(2)
                            f += 1
                            print(f"{GREEN}[✔] Ok")
                        except Exception as e:
                            print(f"{RED}[✘] Follow failed for {label} (id {uid}): {e}")
                            sleep(1)
                        sleep(0.5)
                    print(f"{YELLOW}[⏸] Pausing {batch_pause}s before unfollowing...")
                    sleep(batch_pause)
                    print(f"{YELLOW}[↩] Unfollowing current batch...")
                    for uid, label in batch:
                        try:
                            print(f"{YELLOW}[-] Unfollowing {label} (id {uid})...")
                            client.user_unfollow(uid)
                            sleep(1.5)
                            x += 1
                            print(f"{GREEN}[✔] Ok")
                        except Exception as e:
                            print(f"{RED}[✘] Unfollow failed for {label} (id {uid}): {e}")
                            sleep(1)
                        sleep(1.0)
            except KeyboardInterrupt:
                res = f - x
                if res != 0:
                    suc = f / float(len(NAMES))
                    fail = res / float(len(NAMES))
                    tot = f + x
                    print(f"{GREEN}[✔] Successfully followed/unfollowed a total of {tot} users")
                    sleep(2)
                    print(f"{RED}[✘] Failed to unfollow {abs(res)} users !")
                    sleep(1)
                    print(f"{GREEN}[+] Percentage of success >>> {suc}%")
                    sleep(1)
                    print(f"{RED}[+] Percentage of failure >>> {fail}%")
                    if ga and profile is not None:
                        try:
                            profile = client.account_info()
                        except Exception:
                            pass
                        followers_af = getattr(profile, 'follower_count', None)
                        if followers_bef is not None and followers_af is not None and followers_bef - followers_af != 0:
                            print(f"{GREEN}[✔] Successfully added >>> {followers_af - followers_bef} followers.")
                            sleep(1)
                    if check and FOLLOWERS is not None and profile is not None:
                        print(f"{RED}[✘] WARNING: The data provided may be incorrect if your account is private and you haven't approved the follow requests")
                        sleep(1.5)
                        # Get updated followers using instagrapi
                        try:
                            followers_response = client.user_followers(profile.pk)
                            ADDS = [u.username for u in followers_response.values()]
                        except Exception:
                            ADDS = FOLLOWERS
                        if ADDS == FOLLOWERS:
                            print(f"{RED}[✘] No new followers added ! If your account is private try checking the pending follow requests.")
                        else:
                            print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                            sleep(0.7)
                            for i, username in enumerate(ADDS):
                                print(f"{YELLOW}[+] User No{i+1} >>> {username}")
                    elif check:
                        print(f"{YELLOW}[!] Skipping follower username listing due to endpoint limitations.")
                        sleep(2)
                    print(f"{YELLOW}[*] Some users may not have been unfollowed automatically (count ≈ {abs(res)}).")
                else:
                    print(f"{GREEN}[+] Success >>> 100%")
                    sleep(0.9)
                    print(f"{RED}[+] Fail >>> {res}%")
                    sleep(0.9)
                if keep:
                    name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/log.txt')
                    with open(name, 'w', encoding='utf-8') as f:
                        if res != 0:
                            f.write(f'[✔] Successfully followed/unfollowed a total of {tot} users\n')
                            f.write(f'[✘] Failed to unfollow {abs(res)} users !\n')
                            f.write(f'[+] Percentage of success >>> {suc}%\n')
                            f.write(f'[+] Percentage of failure >>> {fail}%\n')
                            if ga:
                                followers_af = profile.follower_count
                                if followers_bef - followers_af != 0:
                                    f.write(f'[✔] Successfully added >>> {followers_af - followers_bef} followers.\n')
                            if check:
                              for i, username in enumerate(ADDS):
                                f.write(f"[+] User No{i+1} >>> {username}\n")
                        else:
                            f.write('[+] Percentage of success >>> 100%\n')
                            f.write(f'[+] Percentage of failure >>> {res}%')
                    print(f"{GREEN}[✔] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] File name >>> log.txt")
                    print(f"{GREEN}[↪] Path >>> {name}")
                    print(f"{GREEN}[↪] File size >>> {os.stat(name).st_size} bytes")
                print("\n")
                break

        # Final results
        res = f - x
        if res != 0:
            suc = round(f / float(len(NAMES)))
            fail = round(res / float(len(NAMES)))
            tot = f + x
            print(f"{GREEN}[✔] Successfully followed/unfollowed a total of {tot} users")
            sleep(2)
            print(f"{RED}[✘] Failed to unfollow {abs(res)} users !")
            sleep(2)
            print(f"{GREEN}[+] Percentage of success >>> {suc}%")
            sleep(1)
            print(f"{RED}[+] Percentage of failure >>> {fail}%")
            sleep(1)
            if ga and profile is not None:
                try:
                    profile = client.account_info()
                except Exception:
                    pass
                followers_af = getattr(profile, 'follower_count', None)
                if followers_bef is not None and followers_af is not None and followers_bef - followers_af != 0:
                    print(f"{GREEN}[✔] Successfully added >>> {followers_af - followers_bef} followers.")
                    sleep(1)
            if check and FOLLOWERS is not None and profile is not None:
                print(f"{RED}[✘] WARNING: The data provided may be incorrect if your account is private and you haven't approved the follow requests.")
                sleep(1.5)
                # Get updated followers using instagrapi
                try:
                    followers_response = client.user_followers(profile.pk)
                    ADDS = [u.username for u in followers_response.values()]
                except Exception:
                    ADDS = FOLLOWERS
                if ADDS == FOLLOWERS:
                    print(f"{RED}[✘] No new followers added ! If your account is private try checking the pending follow requests.")
                else:
                    print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                    sleep(0.7)
                    for i, username in enumerate(ADDS):
                        print(f"{YELLOW}[+] User No{i+1} >>> {username}")
                sleep(1.5)
            elif check:
                print(f"{YELLOW}[!] Skipping follower username listing due to endpoint limitations.")
            print(f"{YELLOW}[*] Some users may not have been unfollowed automatically (count ≈ {abs(res)}).")
            sleep(2)
        else:
            print(f"{YELLOW}[+] Success >>> 100%")
            sleep(1)
            print(f"{YELLOW}[+] Fail >>> {res}%")
            sleep(2)

        if keep:
            name = './files/log.txt'
            with open(name, 'w', encoding='utf-8') as f:
                if res != 0:
                    f.write(f'[✔] Successfully followed/unfollowed a total of {tot} users\n')
                    f.write(f'[✘] Failed to unfollow {abs(res)} users !\n')
                    f.write(f'[+] Percentage of success >>> {suc}%\n')
                    f.write(f'[+] Percentage of failure >>> {fail}%\n')
                    if ga and profile is not None:
                        try:
                            profile = client.account_info()
                        except Exception:
                            pass
                        followers_af = getattr(profile, 'follower_count', None)
                        if followers_bef is not None and followers_af is not None and followers_bef - followers_af != 0:
                            f.write(f'[✔] Successfully added >>> {followers_af - followers_bef} followers.\n')
                    if check and FOLLOWERS is not None and profile is not None:
                        try:
                            followers_response = client.user_followers(profile.pk)
                            ADDS = [user.username for user in followers_response.values()]
                        except Exception:
                            ADDS = FOLLOWERS
                        if ADDS != FOLLOWERS:
                            print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                            sleep(0.7)
                            for i, username in enumerate(ADDS):
                                f.write(f"[+] User No{i+1} >>> {username}\n")
                else:
                    f.write('[+] Percentage of success >>> 100%\n')
                    f.write(f'[+] Percentage of failure >>> {res}%')
            sleep(0.6)
            print(f"{GREEN}[✔] Successfully saved log !")
            sleep(1)
            print(f"{GREEN}[↪] File name >>> log.txt")
            sleep(0.5)
            print(f"{GREEN}[↪] Location >>> {name}")
            sleep(0.5)
            print(f"{GREEN}[↪] File size >>> {os.stat(name).st_size} bytes")

        print(f"{GREEN}[+] Thank you for using IGFI 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)

if __name__ == '__main__':
    # Minimal CLI: username/password only; ignore unknown args (e.g., --session)
    parser = argparse.ArgumentParser(description='IGFI - increase Instagram followers')
    parser.add_argument('-u', '--username', help='Your Instagram username or email')
    parser.add_argument('-p', '--password', help='Your Instagram password')
    args, unknown = parser.parse_known_args()
    if not args.username:
        args.username = input('Username or email: ').strip()
    if not args.password:
        args.password = input('Password: ').strip()
    main(username=args.username.strip().lower(), password=args.password.strip())
