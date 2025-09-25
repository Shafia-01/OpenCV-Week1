"""
Assignment 1: Basic Image Operations
------------------------------------
Tasks:
1. Load & display image
2. Convert to grayscale
3. Brightness & contrast adjustment
4. Split & merge color channels
5. Create negative image
"""

import cv2
import numpy as np
import argparse
import os

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def assignment1(image_path, output_dir="outputs"):
    ensure_dir(output_dir)

    # 1. Load image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    print("Original image shape:", img.shape)
    print("Data type:", img.dtype)
    print("Pixel range: min =", img.min(), "max =", img.max())

    # 2. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(output_dir, "gray.jpg"), gray)

    # 3. Brightness & contrast
    bright = cv2.convertScaleAbs(img, alpha=1, beta=50)   # beta = brightness
    contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0) # alpha = contrast
    cv2.imwrite(os.path.join(output_dir, "bright.jpg"), bright)
    cv2.imwrite(os.path.join(output_dir, "contrast.jpg"), contrast)

    # 4. Split & merge channels
    B, G, R = cv2.split(img)
    zeros = np.zeros_like(B)
    cv2.imwrite(os.path.join(output_dir, "blue_channel.jpg"), cv2.merge([B, zeros, zeros]))
    cv2.imwrite(os.path.join(output_dir, "green_channel.jpg"), cv2.merge([zeros, G, zeros]))
    cv2.imwrite(os.path.join(output_dir, "red_channel.jpg"), cv2.merge([zeros, zeros, R]))
    merged = cv2.merge([B, G, R])
    cv2.imwrite(os.path.join(output_dir, "merged.jpg"), merged)

    # 5. Negative image
    negative = 255 - img
    cv2.imwrite(os.path.join(output_dir, "negative.jpg"), negative)

    print("All outputs saved in", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assignment 1: Basic Image Operations")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output_dir", default="outputs", help="Directory to save results")
    args = parser.parse_args()
    assignment1(args.image, args.output_dir)
