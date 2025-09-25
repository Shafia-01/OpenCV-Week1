"""
Assignment 3: Thresholding & Segmentation
-----------------------------------------
Tasks:
1. Global thresholding
2. Adaptive thresholding
3. Otsu's method
4. Contour detection
"""

import cv2
import argparse
import os

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def assignment3(image_path, output_dir="outputs"):
    ensure_dir(output_dir)

    # Load grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # 1. Global thresholding
    _, th_global = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(output_dir, "threshold_global.jpg"), th_global)

    # 2. Adaptive thresholding
    th_adapt = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    cv2.imwrite(os.path.join(output_dir, "threshold_adaptive.jpg"), th_adapt)

    # 3. Otsu's thresholding
    _, th_otsu = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    cv2.imwrite(os.path.join(output_dir, "threshold_otsu.jpg"), th_otsu)

    # 4. Contour detection
    contours, _ = cv2.findContours(th_otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(img_color, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(os.path.join(output_dir, "contours.jpg"), img_color)

    print("All outputs saved in", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assignment 3: Thresholding & Segmentation")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output_dir", default="outputs", help="Directory to save results")
    args = parser.parse_args()
    assignment3(args.image, args.output_dir)
