from scoreboard import save_score, show_top_5
from game import main_game
from colorama import Fore, Style

def main():
    print(Fore.MAGENTA + "=== WELCOME TO GUESS BATTLE GAME ===")
    nama = input("Masukkan nama login Anda: ").strip()
    if not nama:
        nama = "Player_Unknown"
        
    skor_akhir = main_game()
    print(Fore.GREEN + f"\nPermainan selesai! Total skor {nama}: {skor_akhir} pts")
    
    if skor_akhir > 0:
        save_score(nama, skor_akhir)
        
    show_top_5()

if __name__ == "__main__":
    main()