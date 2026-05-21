import argparse
from analyzer import menganalisis_teks

def main():
    parser = argparse.ArgumentParser(description="Program Analisis Teks Otomatis")
    parser.add_argument('--file', type=str, default='teks.txt', help='Nama file input teks (.txt)')
    parser.add_argument('--out', type=str, default='report.txt', help='Nama file output hasil laporan')
    
    args = parser.parse_args()
    
    print(f"Memulai analisis pada file: {args.file} ...")
    menganalisis_teks(args.file, args.out)

if __name__ == "__main__":
    main()