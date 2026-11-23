import os

LINE = "My agent files a progress report, a research brief, and a victory lap — all for renaming one file to final_v2_REAL.py"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE.strip() + "\n")

if __name__ == "__main__":
    main()
