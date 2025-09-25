"""
Assignment 2: Filtering & Edge Detection
----------------------------------------
Tasks:
1. Apply Gaussian, Median, and Bilateral filters
2. Detect edges with Sobel, Laplacian, and Canny
3. Save all results
"""

import cv2
import argparse
import os

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def assignment2(image_path, output_dir="outputs"):
    ensure_dir(output_dir)

    # Load image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. Filters
    gaussian = cv2.GaussianBlur(img, (7, 7), 1.5)
    median = cv2.medianBlur(img, 5)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    cv2.imwrite(os.path.join(output_dir, "gaussian.jpg"), gaussian)
    cv2.imwrite(os.path.join(output_dir, "median.jpg"), median)
    cv2.imwrite(os.path.join(output_dir, "bilateral.jpg"), bilateral)

    # 2. Edge Detection
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = cv2.convertScaleAbs(sobel_combined)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    canny = cv2.Canny(gray, 100, 200)

    cv2.imwrite(os.path.join(output_dir, "sobel.jpg"), sobel_combined)
    cv2.imwrite(os.path.join(output_dir, "laplacian.jpg"), laplacian)
    cv2.imwrite(os.path.join(output_dir, "canny.jpg"), canny)

    print("All outputs saved in", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assignment 2: Filtering & Edge Detection")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output_dir", default="outputs", help="Directory to save results")
    args = parser.parse_args()
    assignment2(args.image, args.output_dir)
