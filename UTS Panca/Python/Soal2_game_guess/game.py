import random
from colorama import Fore, Style, init

init(autoreset=True)

def main_game():
    levels = {
        1: {"range": (1, 10), "attempts": 3, "points_multiplier": 50},
        2: {"range": (1, 50), "attempts": 5, "points_multiplier": 100},
        3: {"range": (1, 100), "attempts": 7, "points_multiplier": 200}
    }
    
    total_score = 0
    
    for lvl in [1, 2, 3]:
        cfg = levels[lvl]
        target = random.randint(cfg["range"][0], cfg["range"][1])
        print(Fore.CYAN + f"\n--- MEMASUKI LEVEL {lvl} (Tebak angka {cfg['range'][0]}-{cfg['range'][1]}) ---")
        print(Fore.YELLOW + f"Anda memiliki {cfg['attempts']} percobaan.")
        
        menang = False
        for sisa in range(cfg["attempts"], 0, -1):
            try:
                tebakan = int(input(f"Masukkan tebakan Anda ({sisa}x sisa): "))
            except ValueError:
                print(Fore.RED + "Input harus berupa angka valid!")
                continue
                
            if tebakan == target:
                poin_level = sisa * cfg["points_multiplier"]
                total_score += poin_level
                print(Fore.GREEN + f"HEBAT! Tebakan benar. Anda mendapatkan {poin_level} poin.")
                menang = True
                break
            elif tebakan < target:
                print(Fore.BLUE + "Terlalu RENDAH!")
            else:
                print(Fore.BLUE + "Terlalu TINGGI!")
                
        if not menang:
            print(Fore.RED + f"Game Over di Level {lvl}! Angka yang benar adalah {target}.")
            break
            
    return total_score