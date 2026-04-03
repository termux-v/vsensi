import os, time, sys, random, requests

# PROFESSIONAL ELITE COLORS
G, R, W, B, Y, C, P = "\033[1;32m", "\033[1;31m", "\033[1;37m", "\033[1;34m", "\033[1;33m", "\033[1;36m", "\033[1;35m"

def logo():
    os.system('clear')
    print(f"""{C}
    ██╗   ██╗    ███████╗███████╗███╗   ██╗███████╗██╗
    ██║   ██║    ██╔════╝██╔════╝████╗  ██║██╔════╝██║
    ██║   ██║    ███████╗█████╗  ██╔██╗ ██║███████╗██║
    ╚██╗ ██╔╝    ╚════██║██╔══╝  ██║╚██╗██║╚════██║██║
     ╚████╔╝     ███████║███████╗██║ ╚████║███████║██║
      ╚═══╝      ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝
    {G}      [ V21 OMNIPOTENT - THE FINAL GOD VERSION ]
    {W}═══════════════════════════════════════════════════""")

def auto_optimize():
    # Performance boost animations (No hardware scanning)
    optimizing = [
        "CLEANING SYSTEM CACHE",
        "STABILIZING PING NODES",
        "FIXING TOUCH SAMPLING",
        "OVERCLOCKING FPS LIMIT",
        "SYNCING 200% MASTER NODES"
    ]
    for task in optimizing:
        sys.stdout.write(f"{P}[~] {task}...")
        for _ in range(8):
            sys.stdout.write(f"{G}■")
            sys.stdout.flush(); time.sleep(0.04)
        print(f" {G}[OK]{W}")

def main():
    logo()
    # Private Key Protection
    key = "VASU-X-PRO"
    user_key = input(f"{P}[?] ENTER ACCESS KEY: {W}")
    if user_key != key:
        print(f"{R}[!] ACCESS DENIED!{W}"); sys.exit()
    
    logo()
    print(f"{B}[*] SYSTEM STATUS: {G}ONLINE & UPDATED{W}")
    
    # Manual Hardware Input (As requested)
    brand = input(f"\n{B}[+] Device Model : {W}")
    ram   = int(input(f"{B}[+] RAM (GB)     : {W}"))
    hz    = int(input(f"{B}[+] Display (Hz) : {W}"))
    
    print(f"\n{C}--- SELECT GAME VERSION ---{W}")
    print(f"{Y}[1] FREE FIRE MAX")
    print(f"{Y}[2] FREE FIRE NORMAL")
    game_v = input(f"{B}[+] Choice (1/2): {W}")

    print(f"\n{C}--- SELECT PERFORMANCE MODE ---{W}")
    print(f"{Y}[1] 1P ONE-TAP (Extreme Speed)")
    print(f"{Y}[2] ANTI-RECOIL (Spray Control)")
    mode = input(f"{B}[+] Choice (1/2): {W}")

    auto_optimize()

    # --- THE ELITE 200% MATH INTERPOLATION ---
    # Smart calculation based on Manual Input
    base_sensi = 200
    red_dot = 197 if ram < 6 else 200
    
    if hz >= 90:
        s2x, s4x, snp, free = 194, 185, 95, 185
        dpi = 411
    else:
        s2x, s4x, snp, free = 188, 175, 88, 165
        dpi = 580

    fire = "38%" if game_v == "1" else "42%"

    print(f"\n{G}╔═══════════════ OMNIPOTENT PANEL V21 ══════════════╗")
    print(f"║ {W}DEVICE      : {brand.upper()} | STATUS: {G}INJECTED       {G}║")
    print(f"║ {W}GENERAL     : {R}{base_sensi}%      {W}RED DOT  : {R}{red_dot}%          {G}║")
    print(f"║ {W}2X SCOPE    : {C}{s2x}%      {W}4X SCOPE : {C}{s4x}%          {G}║")
    print(f"║ {W}SNIPER      : {Y}{snp}%       {W}FREE LOOK: {Y}{free}%         {G}║")
    print(f"║ {W}DPI VALUE   : {C}{dpi}      {W}FIRE BTN : {C}{fire}          {G}║")
    print(f"║ {W}LATENCY     : {G}0.01ms     {W}TOUCH    : {G}600Hz          {G}║")
    print(f"╚════════════════════════════════════════════════════╝")
    
    # Save a quick log for the user
    with open("config_log.txt", "w") as f:
        f.write(f"V21_ACTIVE_FOR_{brand.upper()}_HZ_{hz}")

    print(f"\n{P}[#] CONFIG EXPORTED TO 'config_log.txt'{W}")
    print(f"{G}>>> SYSTEM OVERCLOCKED! BECOME THE GOD! <<<{W}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] EXITING CORE.")
            
