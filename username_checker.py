import requests, datetime, random, xml.etree.ElementTree as ET, time, os
from concurrent.futures import ThreadPoolExecutor, as_completed # type: ignore
from colorama import Fore

def generate_random_birthday():
    year = random.randint(1950, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    dt = datetime.datetime(year, month, day, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    return dt.isoformat(timespec='milliseconds') + 'Z'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_discord(username):
    url = 'https://discord.com/api/v9/unique-username/username-attempt-unauthed'
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    r = requests.post(url, json={"username": username}, headers=headers)
    if r.ok:
        data = r.json()
        return not data.get("taken", True)
    return False

def check_roblox(username: str) -> bool:
    url = 'https://auth.roblox.com/v1/usernames/validate'
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    payload = {
        "username": username,
        "context": "Signup",
        "birthday": generate_random_birthday()
    }

    for _ in range(3):  # retry a few times if token fails
        # obtain CSRF
        r = session.post(url, json=payload, headers=headers)
        token = r.headers.get('x-csrf-token')

        if token:
            headers['X-csrf-token'] = token
            # Use CSRF
            r2 = session.post(url, json=payload, headers=headers)
            if r2.ok:
                data = r2.json()
                # check for availability if success with token
                return data.get("code") == 0

        # retry incase token failed
    return False

def check_neocities(username):
    url = "https://neocities.org/create_validate"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = f"field=username&value={username}&is_education=false"
    r = requests.post(url, data=payload, headers=headers)
    if r.ok:
        data = r.json()
        return data.get("result") == "ok"
    return False

def check_github(username):
    url = f"https://github.com/signup_check/username?value={username}"
    r = requests.get(url)
    return r.status_code == 200 and f"{username} is available" in r.text

def check_devto(username):
    url = f"https://dev.to/{username}"
    r = requests.get(url)
    return r.status_code == 404

def check_replit(username):
    url = f"https://replit.com/@{username}"
    r = requests.get(url)
    return r.status_code == 404

def check_gitlab(username):
    url = f"https://gitlab.com/users/{username}/exists"
    r = requests.get(url)
    if r.ok:
        data = r.json()
        return data.get("exists") == False
    return False

def check_soundcloud(username):
    url = f"https://soundcloud.com/{username}"
    r = requests.get(url)
    return r.status_code == 404

def check_patreon_creator(username):
    url = f"https://www.patreon.com/api/campaigns?filter[vanity]={username}&fields[campaign]=[]&json-api-version=1.0&json-api-use-default-includes=false&include=[]"
    r = requests.get(url)
    return r.status_code == 404

def check_steam_vanity(username):
    url = f"https://steamcommunity.com/id/{username}"
    r = requests.get(url)
    if not r.ok:
        return True
    html = r.text.lower()
    not_found_markers = [
        "the specified profile could not be found",
        "this profile is private or does not exist"
    ]
    for marker in not_found_markers:
        if marker in html:
            return True  # available
    if username.lower() not in html: # check if the username is seen anywhere in the page's html
        return True  # available
    return False  # taken

def check_twitter_x(username):
    url = f"https://api.x.com/i/users/username_available.json?username={username}"
    r = requests.get(url)
    if r.ok:
        data = r.json()
        return data.get("valid") == True
    return False

def check_steam_group(username: str) -> bool:
    url = "https://steamcommunity.com/actions/AvailabilityCheck"
    payload = {
        "xml": "1",
        "type": "groupLink",
        "value": username
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.post(url, data=payload, headers=headers)
    if not r.ok:
        return False  # failed

    root = ET.fromstring(r.text)
    bResults = root.find("bResults")
    if bResults is not None:
        return bResults.text == "1"
    
    return False  # fallback incase XML is weird

def check_minecraft_username(username: str) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://laby.net/api/search/names/{username}"
    r = requests.get(url, headers=headers)
    if not r.ok:
        return False
    data = r.json()
    results = data.get("results", [])
    if not results:
        return True

    for entry in results:
        if entry.get("user_name", "").lower() == username.lower():
            return False  # Taken

    return False  # no exact match, assume unavailable

def check_fiverr(username):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    payload = {
        "username": username
    }
    url = "https://www.fiverr.com/validate_username"
    r = requests.post(url, json=payload, headers=headers)
    if r.ok:
        data = r.json()
        return data.get("status") == "success"
    return False

def check_modrinth(username):
    url = f"https://api.modrinth.com/v2/user/{username}"
    r = requests.get(url)
    return r.status_code == 404

def check_chess(username):
    url = f"https://www.chess.com/callback/user/valid?username={username}"
    r = requests.get(url)
    if r.ok:
        data = r.json()
        return data.get("valid") == True
    return False

def check_lichess(username):
    url = f"https://lichess.org/api/player/autocomplete?term={username}&exists=1"
    r = requests.get(url)
    if r.ok:
        return r.text.strip().lower() == "false"
    return False
    
def check_tryhackme(username):
    url = f"https://tryhackme.com/api/v2/users/availability?username={username}"
    r = requests.get(url)
    if r.ok:
        data = r.json()
        return data.get("data", {}).get("available") == True
    return False

def check_hypixel_forums(username):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
    }
    payload = {
        "content": username,
        "_xfResponseType": "json",
        "_xfWithData": 1,
        "_xfRequestUri": "/register/"
    }
    url = "https://hypixel.net/misc/validate-username"
    r = requests.post(url, json=payload, headers=headers)
    if r.ok:
        return r.json().get("inputValid") == True
    return False

def check_letterboxd(username):
    url = f"https://letterboxd.com/s/checkusername?q={username}"
    r = requests.get(url)
    if r.ok:
        return r.json().get("data", {}).get("result") == "AVAILABLE"
    return False

def check_buymeacoffee(username):
    payload = {
        "project_slug": username
    }
    url = "https://app.buymeacoffee.com/api/v1/check_availability"
    r = requests.post(url, json=payload)
    if r.ok:
        return r.json().get("data", {}).get("available") == True
    return False
    
def check_dailymotion(username):
    url = f"https://api.dailymotion.com/user/{username}"
    r = requests.get(url)
    return r.status_code == 404 and r.json().get("error", {}).get("code") == 404

def check_scratch(username):
    url = f"https://api.scratch.mit.edu/accounts/checkusername/{username}"
    r = requests.get(url)
    if r.ok:
        return r.json().get("msg") == "valid username"
    return False

def check_dockerhub(username):
    normalized_name = username.lower()
    if not normalized_name.isalnum() or len(normalized_name) < 4:
        return False # cause anything under 4 letters will always return not found and therefore be marked as available.
    url = f"https://hub.docker.com/v2/users/{normalized_name}" # also seems like this is the only website which actually doesnt convert the username itself.
    r = requests.get(url)
    return r.status_code == 404 and r.json().get("message") == "User not found"

def check_monkeytype(username):
    url = f"https://api.monkeytype.com/users/checkName/{username}"
    r = requests.get(url)
    if r.ok:
        return r.json().get("data", {}).get("available") == True
    return False

def check_shopify_domain_name(username): # cause why not
    url = f"https://app.shopify.com/services/signup/check_availability.json?shop_name={username}"
    r = requests.get(url)
    if r.ok:
        return r.json().get ("status") == "available"
    return False

def check_all_old(username): # old check_all, left it in cause why not
    results = {
        "Discord": check_discord(username),
        "Roblox": check_roblox(username),
        "Neocities": check_neocities(username),
        "GitHub": check_github(username),
        "Dev.to": check_devto(username),
        "Replit": check_replit(username),
        "GitLab": check_gitlab(username),
        "SoundCloud": check_soundcloud(username),
        "Patreon Creator": check_patreon_creator(username),
        "Steam Vanity": check_steam_vanity(username),
    }
    for platform, available in results.items():
        if available:
            print(f"[✓] {platform}: '{username}' is available")
        else:
            print(f"[✗] {platform}: '{username}' is taken")

def check_all(username):
    checks = {
        "Discord": check_discord,
        "Roblox": check_roblox,
        "Neocities": check_neocities,
        "GitHub": check_github,
        "Dev.to": check_devto,
        "Replit": check_replit,
        "GitLab": check_gitlab,
        "SoundCloud": check_soundcloud,
        "Patreon Creator": check_patreon_creator,
        "Steam Vanity": check_steam_vanity,
        "Steam Group": check_steam_group,
        "Twitter/X": check_twitter_x,
        "Minecraft Username": check_minecraft_username,
        "Fiverr": check_fiverr,
        "Modrinth": check_modrinth,
        "Chess.com": check_chess,
        "Lichess": check_lichess,
        "TryHackMe": check_tryhackme,
        "Hypixel Forums": check_hypixel_forums,
        "Letterboxd": check_letterboxd,
        "Buy Me a Coffee": check_buymeacoffee,
        "DailyMotion": check_dailymotion,
        "Scratch": check_scratch,
        "Docker Hub": check_dockerhub,
        "MonkeyType": check_monkeytype,
        "Shopify Domain": check_shopify_domain_name,
    }

    # Starts de clock
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=len(checks)) as executor:
        future_to_platform = {
            executor.submit(func, username): (platform, time.perf_counter())
            for platform, func in checks.items()
        }

        for future in as_completed(future_to_platform):
            platform, task_start = future_to_platform[future]
            try:
                available = future.result()
                ms = int((time.perf_counter() - task_start) * 1000) # platform time calculation, fyi no response time calc for single api calls cause i just dont wanna spam it that much (code-wise)
                
                if available:
                    if ms <= 600: # 600 ms or less is fast no? well depends ig
                        print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET + f" {platform}: '{username}' is Available (" + Fore.LIGHTCYAN_EX + f"{ms}ms" + Fore.RESET + ")")
                    elif ms >= 1100: # i assume 1100 ms to be slow
                        print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET + f" {platform}: '{username}' is Available (" + Fore.LIGHTYELLOW_EX + f"{ms}ms" + Fore.RESET + ")")
                    else:
                        print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET + f" {platform}: '{username}' is Available ({ms}ms)")
                else:
                    if ms <= 500:
                        print(Fore.LIGHTRED_EX + "[✗]" + Fore.RESET + f" {platform}: '{username}' is Unavailable (" + Fore.LIGHTCYAN_EX + f"{ms}ms" + Fore.RESET + ")")
                    elif ms >= 1500:
                        print(Fore.LIGHTRED_EX + "[✗]" + Fore.RESET + f" {platform}: '{username}' is Unavailable (" + Fore.LIGHTYELLOW_EX + f"{ms}ms" + Fore.RESET + ")")
                    else:
                        print(Fore.LIGHTRED_EX + "[✗]" + Fore.RESET + f" {platform}: '{username}' is Unavailable ({ms}ms)")
            except Exception as e:
                print(f"[!] {platform}: error ({e})")

def main():
    while True:
        print("\n--- Username Checker ---")
        print("FYI: this username checker uses SignUp API Endpoints (mostly),")
        print("therefore it may say that the username is taken/unavailable,")
        print("when the user profile for said username doesn't exist.")
        print("")
        print(Fore.LIGHTGREEN_EX + "[✓] " + Fore.RESET + "<- Available")
        print(Fore.LIGHTRED_EX + "[✗] " + Fore.RESET + "<- Unavailable")
        print("[!] <- Issue with the platform or code")
        print("")
        print("1. Discord")
        print("2. Roblox")
        print("3. Neocities")
        print("4. GitHub")
        print("5. Dev.to <- Unreliable, Private Banished Word List")
        print("6. Replit")
        print("7. GitLab")
        print("8. SoundCloud")
        print("9. Patreon Creator")
        print("10. Steam Vanity")
        print("11. Steam Group")
        print("12. Twitter/X")
        print("13. Minecraft Username (using Laby.net's api)")
        print("14. Fiverr")
        print("15. Modrinth")
        print("16. Chess.com")
        print("17. Lichess")
        print("18. TryHackMe")
        print("19. Hypixel Forums")
        print("20. Letterboxd")
        print("21. Buy Me a Coffee")
        print("22. DailyMotion")
        print("23. Scratch (mit.edu)")
        print("24. Docker Hub")
        print("25. MonkeyType")
        print("26. Shopify Domain <- <username>.myshopify.com")
        print("27. Check ALL (Ordered by response latency, Fastest -> Slowest)")
        print("28. Exit")
        choice = input("Choose an option (1-28): ").strip()

        if choice == '28':
            print("Exiting...")
            break

        if choice in map(str, range(1, 28)): # the /back and single api choices
            while True:
                username = input("Enter username (or '/back' to return): ").strip()
                if username.lower() == '/back':
                    break
                if not username:
                    print("Username can't be empty.")
                    continue

                if choice == '1':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_discord(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Discord: {username}")
                elif choice == '2':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_roblox(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Roblox: {username}")
                elif choice == '3':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_neocities(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Neocities: {username}")
                elif choice == '4':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_github(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"GitHub: {username}")
                elif choice == '5':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_devto(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Dev.to: {username}")
                elif choice == '6':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_replit(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Replit: {username}")
                elif choice == '7':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_gitlab(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"GitLab: {username}")
                elif choice == '8':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_soundcloud(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"SoundCloud: {username}")
                elif choice == '9':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_patreon_creator(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Patreon Creator: {username}")
                elif choice == '10':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_steam_vanity(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Steam Vanity: {username}")
                elif choice == '11':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_steam_group(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Steam Group: {username}")
                elif choice == '12':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_twitter_x(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Twitter/X: {username}")
                elif choice == '13':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_minecraft_username(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Minecraft Username: {username}")
                elif choice == '14':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_fiverr(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Fiverr: {username}")
                elif choice == '15':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_modrinth(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Modrinth: {username}")
                elif choice == '16':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_chess(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Chess.com: {username}")
                elif choice == '17':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_lichess(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Lichess: {username}")
                elif choice == '18':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_tryhackme(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"TryHackMe: {username}")
                elif choice == '19':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_hypixel_forums(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Hypixel Forums: {username}")
                elif choice == '20':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_letterboxd(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Letterboxd: {username}")
                elif choice == '21':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_buymeacoffee(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Buy Me a Coffee: {username}")
                elif choice == '22':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_dailymotion(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"DailyMotion: {username}")
                elif choice == '23':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_scratch(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Scratch: {username}")
                elif choice == '24':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_dockerhub(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Docker Hub: {username}")
                elif choice == '25':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_monkeytype(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"MonkeyType: {username}")
                elif choice == '26':
                    print(Fore.LIGHTGREEN_EX + "[✓]" + Fore.RESET if check_shopify_domain_name(username) else Fore.LIGHTRED_EX + "[✗]" + Fore.RESET, f"Shopify Domain: {username}")
                elif choice == '27':
                    check_all(username)
        else:
            print("Invalid input.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_console()
        import sys
        sys.exit(0)



# Email check @ Twitter:
# https://api.x.com/i/users/email_available.json?email=<email>
# returns 'valid' = false, 'taken' = true if taken, i'm assuming opposite if available.
