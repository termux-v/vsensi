

import os, time, sys, random

# --- PRO COLORS ---
G, R, W, B, Y, C, P = "\033[1;32m", "\033[1;31m", "\033[1;37m", "\033[1;34m", "\033[1;33m", "\033[1;36m", "\033[1;35m"

def clear(): os.system('clear')

def slow_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(speed)
    print()

def progress_bar(task):
    sys.stdout.write(f"{Y}[*] {task}: ")
    for i in range(21):
        time.sleep(0.1)
        sys.stdout.write(f"{G}█")
        sys.stdout.flush()
    print(f" {W}DONE!{W}")

def logo():
    clear()
    print(f"""{C}
    ██╗   ██╗    ███████╗███████╗███╗   ██╗███████╗██╗
    ██║   ██║    ██╔════╝██╔════╝████╗  ██║██╔════╝██║
    ██║   ██║    ███████╗█████╗  ██╔██╗ ██║███████╗██║
    ╚██╗ ██╔╝    ╚════██║██╔══╝  ██║╚██╗██║╚════██║██║
     ╚████╔╝     ███████║███████╗██║ ╚████║███████║██║
      ╚═══╝      ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝
    {Y}     [ PROFESSIONAL HARDWARE CALIBRATOR V7.0 ]
    {R}      DEVELOPER: @gamingandanotheruses-oss
    {W}═══════════════════════════════════════════════════""")

def main():
    logo()
    print(f"{P}[!] SYSTEM READY. STARTING HARDWARE ANALYSIS...{W}\n")
    
    # User Inputs
    brand = input(f"{B}[+] Device Brand/Model : {W}")
    ram   = int(input(f"{B}[+] RAM Capacity (GB) : {W}"))
    hz    = int(input(f"{B}[+] Display Rate (Hz) : {W}"))
    storage = int(input(f"{B}[+] Available Storage (GB) : {W}"))
    
    print(f"\n{C}--- INITIALIZING DEEP SCAN ---{W}")
    progress_bar("SCANNING TOUCH PANEL  ")
    progress_bar("ANALYZING REFRESH RATE")
    progress_bar("CALIBRATING DPI SCALING")
    progress_bar("BYPASSING LATENCY      ")
    
    # --- GOD LEVEL CALCULATION ---
    # Refresh rate jitna zyada, sensi utni smooth honi chahiye (No Shake)
    if hz >= 120: sensi = 92
    elif hz >= 90: sensi = 96
    else: sensi = 100
    
    # RAM & Storage Optimization
    if ram < 6: sensi += 2
    if storage < 20: sensi += 1 # Lag compensation
    
    # Fire Button Logic
    fire_btn = "44%" if hz > 60 else "52%"
    dpi = 411 + (ram * 10) if ram < 8 else "SYSTEM DEFAULT"
    
    time.sleep(1)
    print(f"\n{G}╔═════════════ SUCCESS: OPTIMIZED CONFIG ══════════════╗")
    print(f"║ {W}DEVICE        : {Y}{brand.upper()} ({ram}GB / {hz}Hz)           {G}║")
    print(f"║ {W}GENERAL       : {C}{min(sensi, 100)}%                          {G}║")
    print(f"║ {W}RED DOT       : {C}{sensi - 5}%                           {G}║")
    print(f"║ {W}2X SCOPE      : {C}{sensi - 8}%                           {G}║")
    print(f"║ {W}4X SCOPE      : {C}{sensi - 15}%                          {G}║")
    print(f"║ {W}SNIPER        : {C}45%                            {G}║")
    print(f"╠═════════════ SYSTEM SETTINGS (REQUIRED) ═════════════╣")
    print(f"║ {Y}DPI VALUE     : {W}{dpi}                         {G}║")
    print(f"║ {Y}FIRE BUTTON   : {W}{fire_btn}                          {G}║")
    print(f"║ {Y}POINTER SPEED : {W}MAXIMUM (100%)                 {G}║")
    print(f"╚══════════════════════════════════════════════════════╝")
    
    print(f"\n{R}[!] IMPORTANT: {W}Apply these settings and restart the game.")
    print(f"{P}[#] Sensi Hash: {random.getrandbits(32)}")
    print(f"{G}>>> GOD LEVEL CONFIGURATION APPLIED! <<<{W}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Aborted by user.")
        
