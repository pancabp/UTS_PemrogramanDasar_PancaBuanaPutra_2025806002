import json
import os

FILE_NAME = "scores.json"

def load_scores():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_score(nama, skor_baru):
    scores = load_scores()
    if nama in scores:
        scores[nama] = max(scores[nama], skor_baru)
    else:
        scores[nama] = skor_baru
        
    with open(FILE_NAME, 'w') as f:
        json.dump(scores, f, indent=4)

def show_top_5():
    scores = load_scores()
    print("\n" + "="*7 + " TOP 5 SCORE " + "="*7)
    if not scores:
        print("Belum ada skor tercatat.")
        return
    
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores[:5], start=1):
        print(f"{i}. {name:<10} {score} pts")
    print("=" * 27)