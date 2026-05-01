#!/usr/bin/env python3
import sys
from remover import remove_bg, upscale, clean_mask

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input> [output] [scale 2|4]")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.png"
    scale       = int(sys.argv[3]) if len(sys.argv) > 3 else 4

    print("Removing background...")
    img = remove_bg(input_path)

    print("Cleaning mask...")
    img = clean_mask(img)

    print(f"Upscaling {scale}x...")
    final = upscale(img, scale)

    final.save(output_path, "PNG")
    print(f"Done → {output_path}")

if __name__ == "__main__":
    main()