import sys
import time
import json
import os
import threading
import requests
import base64
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    import colorama
    colorama.init()
except ImportError:
    pass

def getch():
    try:
        import tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch
    except Exception:
        try:
            import msvcrt
            return msvcrt.getwch()
        except Exception:
            return input()[:1]

R      = "\033[0m"
PA     = "\033[38;2;87;2;125m"
PB     = "\033[38;2;100;10;145m"
PC     = "\033[38;2;118;20;168m"
PD     = "\033[38;2;138;35;195m"
PE     = "\033[38;2;155;50;215m"
PDIM   = "\033[38;2;55;0;85m"
G1     = "\033[38;2;55;50;68m"
G2     = "\033[38;2;90;85;108m"
G3     = "\033[38;2;130;125;148m"
G4     = "\033[38;2;170;165;188m"
BOLD   = "\033[1m"
ITALIC = "\033[3m"

BANNER = r"""
  ███╗   ██╗ ██████╗  █████╗ 
  ████╗  ██║██╔═══██╗██╔══██╗
  ██╔██╗ ██║██║   ██║███████║
  ██║╚██╗██║██║   ██║██╔══██║
  ██║ ╚████║╚██████╔╝██║  ██║
  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def animate_banner():
    cols = [PDIM, PA, PB, PC, PD, PE, PD]
    for col in cols:
        sys.stdout.write("\033[H")
        sys.stdout.write(f"{col}{BANNER}{R}")
        sys.stdout.flush()
        time.sleep(0.065)

def show_header():
    clear()
    sys.stdout.write("\033[?25l")
    animate_banner()
    sys.stdout.write("\033[?25h")
    subtitle = "  N U M B E R   F I N D E R"
    print(f"{PDIM}  {'─' * 34}{R}")
    shades = [PA, PB, PC, PD, PE]
    for i, ch in enumerate(subtitle):
        sys.stdout.write(f"{shades[i % len(shades)]}{ch}{R}")
        sys.stdout.flush()
        time.sleep(0.018)
    print()
    print(f"{PDIM}  {'─' * 34}{R}")
    print()

class Spinner:
    FRAMES = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]

    def __init__(self, msg=""):
        self.msg = msg
        self._stop = threading.Event()
        self._t = threading.Thread(target=self._spin, daemon=True)

    def _spin(self):
        i = 0
        while not self._stop.is_set():
            f = self.FRAMES[i % len(self.FRAMES)]
            sys.stdout.write(f"\r  {PD}{f}{R}  {G3}{self.msg}{R}  ")
            sys.stdout.flush()
            i += 1
            time.sleep(0.09)

    def start(self):
        self._t.start()

    def stop(self):
        self._stop.set()
        self._t.join()
        sys.stdout.write(f"\r{' ' * 60}\r")
        sys.stdout.flush()

class NoaAPI:
    def __init__(self):
        self.base_url = "https://apphamed.com/app/v1/api/09c0c62ee895dc8b"
        self.key = b"mysecretkey12345"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "okhttp/5.0.0-alpha.10",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive",
            "Content-Type": "text/plain; charset=UTF-8",
            "Host": "apphamed.com"
        })
        self.session.verify = False

    def _decrypt(self, data_b64):
        try:
            raw = base64.b64decode(data_b64)
            cipher = AES.new(self.key, AES.MODE_ECB)
            return unpad(cipher.decrypt(raw), AES.block_size).decode("utf-8")
        except Exception:
            return None

    def search(self, query):
        try:
            resp = self.session.post(
                f"{self.base_url}/Search",
                data=query.encode("utf-8"),
                timeout=15
            )
            if resp.status_code == 200:
                dec = self._decrypt(resp.text)
                if dec:
                    return json.loads(dec)
            return {"not_found": True}
        except requests.exceptions.Timeout:
            return {"not_found": True, "hint": "timeout"}
        except requests.exceptions.ConnectionError:
            return {"not_found": True, "hint": "connection"}
        except Exception:
            return {"not_found": True, "hint": "unknown"}

def fix_rtl(text):
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except ImportError:
        return text

BOX_W = 47

def menu():
    inner = BOX_W - 2

    top   = f"  {PA}┌{'─' * inner}┐{R}"
    bot   = f"  {PA}└{'─' * inner}┘{R}"
    empty = f"  {PA}│{R}{' ' * inner}{PA}│{R}"

    rows = [
        ("1", "Phone lookup", "find who's calling"),
        ("2", "Name search",  "find numbers by name"),
    ]

    print(top)
    print(empty)

    for key, title, desc in rows:
        visible = f"  {key}  {title:<13} {desc}"

        pad = max(0, inner - len(visible))

        content = (
            f"  {PE}{BOLD}{key}{R}"
            f"  {G4}{BOLD}{title:<13}{R}"
            f" {G2}{ITALIC}{desc}{R}"
            f"{' ' * pad}"
        )

        print(f"  {PA}│{R}{content}{PA}│{R}")

    print(empty)
    print(bot)
    print()
    print(
        f"  {G2}press {PE}1{R} {G2}or{R} "
        f"{PE}2{R} {G2}or{R} "
        f"{PE}q{R} {G2}to quit{R}"
    )
    print()

def glitch_line(text, color=PD):
    glitch = ["▓","░","▒","█","▄"]
    garbled = ""
    for ch in text:
        garbled += random.choice(glitch) if random.random() < 0.07 else ch
    sys.stdout.write(f"\r{color}{BOLD}{garbled}{R}")
    sys.stdout.flush()
    time.sleep(0.06)
    sys.stdout.write(f"\r{color}{BOLD}{text}{R}\n")
    sys.stdout.flush()

def divider(char="─", width=48, color=PA):
    print(f"  {color}{char * width}{R}")

def print_profile(idx, profile, total):
    name_raw = profile.get("name", "—")
    number   = profile.get("number", "—")
    name     = fix_rtl(name_raw)

    t = idx / max(total - 1, 1)
    r = int(87  + t * 68)
    g = int(2   + t * 48)
    b = int(125 + t * 70)
    num_col = f"\033[38;2;{r};{g};{b}m"

    badge   = f"{G1}[{idx+1:02d}/{total:02d}]{R}"
    diamond = f"{PC}◈{R}"
    print(f"  {badge}  {diamond}  {G4}{name:<30}{R}  {num_col}{number}{R}")
    time.sleep(0.032)

def show_results(profiles, query):
    print()
    divider("═", 68, PB)
    count = len(profiles)
    glitch_line(f"  ◆  {count} result{'s' if count != 1 else ''}  ›  {query}")
    divider("─", 68, PA)
    print()
    for i, p in enumerate(profiles):
        print_profile(i, p, count)
    print()
    divider("═", 68, PB)
    print()

def show_not_found(hint=None):
    print()
    if hint == "timeout":
        print(f"  {PA}◈  Number or Name not Found  ·  try again with a different number{R}")
    elif hint == "connection":
        print(f"  {PA}◈  Could not reach server  ·  check connection{R}")
    else:
        print(f"  {PA}◈  Nothing found  ·  check format and try again{R}")
    print(f"  {G1}    phone > 09XXXXXXXXX    name > first or last name{R}")
    print()

def get_line(prompt_text):
    sys.stdout.write(f"\n  {PB}›{R}  {G3}{prompt_text}{R}  {PD}")
    sys.stdout.flush()
    val = input()
    sys.stdout.write(R)
    return val.strip()

def loop_search(api, mode):
    label = "phone number" if mode == "1" else "name"

    while True:
        print()
        print(f"  {G1}[ b ] back    [ q ] quit{R}")
        val = get_line(f"Enter {label}")

        if val.lower() == "q":
            farewell()
            sys.exit(0)
        if val.lower() == "b" or val == "":
            return
        if not val.strip():
            print(f"  {PA}⚠  empty input{R}")
            continue

        print()
        sp = Spinner("searching ...")
        sp.start()
        result = api.search(val)
        sp.stop()

        if result.get("not_found"):
            show_not_found(result.get("hint"))
            continue

        profiles = result.get("Profiles", [])
        if not profiles:
            show_not_found()
        else:
            show_results(profiles, val)

def farewell():
    print()
    msg = "  [ NOA ]  —  session closed"
    for ch in msg:
        sys.stdout.write(f"{PDIM}{ch}{R}")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

def main():
    api = NoaAPI()

    while True:
        show_header()
        menu()
        ch = getch()

        if ch == "q":
            farewell()
            sys.exit(0)
        if ch in ("1", "2"):
            loop_search(api, ch)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        farewell()
        sys.exit(0)
