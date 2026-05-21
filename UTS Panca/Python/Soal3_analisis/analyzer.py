import collections

def menganalisis_teks(file_input, file_output):
    try:
        with open(file_input, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_input}' tidak ditemukan!")
        return False

    jumlah_baris = len(lines)
    teks_utuh = "".join(lines)
    
    words = teks_utuh.lower().split()
    jumlah_kata = len(words)
    
    cleaned_words = [w.strip(".,!?;:()\"'") for w in words if w.strip(".,!?;:()\"'")]
    counter_kata = collections.Counter(cleaned_words)
    top_5_kata = counter_kata.most_common(5)
    
    vokal = "aeiou"
    jumlah_vokal = 0
    jumlah_konsonan = 0
    
    for char in teks_utuh.lower():
        if char.isalpha():
            if char in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1
                
    with open(file_output, 'w', encoding='utf-8') as out:
        out.write("=== LAPORAN STATISTIK TEKS ===\n")
        out.write(f"Jumlah baris           : {jumlah_baris}\n")
        out.write(f"Jumlah kata            : {jumlah_kata}\n")
        out.write(f"Jumlah huruf vokal     : {jumlah_vokal}\n")
        out.write(f"Jumlah huruf konsonan  : {jumlah_konsonan}\n\n")
        
        out.write("=== 5 KATA TERBANYAK & GRAFIK FREKUENSI ===\n")
        for kata, frek in top_5_kata:
            grafik_ascii = "#" * frek
            out.write(f"{kata:<12} : {grafik_ascii} ({frek}x)\n")
            
    print(f"Analisis sukses! Laporan disimpan di '{file_output}'")
    return True