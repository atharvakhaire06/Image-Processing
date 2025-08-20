import cv2
import numpy as np
from collections import Counter
#function starts here
def shannon_fano(symbols, codes, prefix=""):
    if len(symbols) == 1:
        codes[symbols[0][0]] = prefix or "0"  # assign "0" if single symbol
        return

    total = sum(freq for _, freq in symbols)
    acc, split_index = 0, 0

    for i, (_, freq) in enumerate(symbols):
        acc += freq
        if acc >= total / 2:
            split_index = i + 1
            break

    left = symbols[:split_index]
    right = symbols[split_index:]

    shannon_fano(left, codes, prefix + "0")
    shannon_fano(right, codes, prefix + "1")
#ends here
img = cv2.imread("Images\\CuteCat.jpg")  

pixels = [tuple(rgb) for rgb in img.reshape(-1, 3)]

freqs = Counter(pixels)

symbols = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
codes = {}
shannon_fano(symbols, codes)

print("Shannon–Fano Codes (first 10 colors):")
for sym, code in list(codes.items())[:10]:
    print(f"Color {sym} -> {code}")

encoded_bits = "".join(codes[p] for p in pixels)

original_size = len(pixels) * 24  # 24 bits per RGB pixel 8 per pixel
compressed_size = len(encoded_bits)

print("Original size (bits):", original_size)
print("Compressed size (bits):", compressed_size)
print("Compression ratio:", round(original_size / compressed_size, 2))
