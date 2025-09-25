# Image Processing Concepts - Theory & Applications

This note covers the fundamental operations in image processing: **filtering**, **thresholding**, and **transformations**, along with their real-world use cases.

## 1. Filtering (Convolution)
### Theory
- **Filtering** involves applying a kernel (small matrix) over an image to modify pixel values.
- Common types:
  - **Low-pass filters (smoothing/blur):** Average or Gaussian filters remove high-frequency noise.
  - **High-pass filters (sharpening/edges):** Highlight edges by detecting rapid intensity changes.
- Mathematically:
  ```
  g(x, y) = Σ Σ f(i, j) * h(x - i, y - j)
  ```
  where `h` is the filter kernel.

### Real-World Applications
- **Gaussian blur:** Reducing noise before edge detection in autonomous vehicles.
- **Median filter:** Removing salt-and-pepper noise in medical X-rays.
- **Sharpening:** Enhancing satellite images for terrain recognition.

## 2. Thresholding
### Theory
- Converts grayscale images into **binary images** by classifying pixels as foreground/background.
- Types:
  - **Global thresholding:** One fixed value `T` for all pixels.  
    ```
    dst(x,y) = { 255 if src(x,y) > T else 0 }
    ```
  - **Adaptive thresholding:** Different thresholds based on local neighborhoods.
  - **Otsu’s method:** Automatically selects the threshold by minimizing intra-class variance.

### Real-World Applications
- **Document scanning:** Converting scanned pages into clean black-and-white for OCR.
- **Medical imaging:** Segmenting tumors or regions of interest in MRI scans.
- **Quality control:** Detecting defects (e.g., cracks in manufactured parts).

## 3. Geometric Transformations
### Theory
- Operations that change the **position, orientation, or shape** of an image.
- Types:
  - **Translation:** Shifting images by (x, y).
  - **Scaling (resize):** Changing dimensions with interpolation.
  - **Rotation:** Rotating around a point (usually the center).
  - **Affine transform:** Preserves parallelism (shear, rotation, translation).
  - **Perspective transform:** Maps quadrilaterals → rectangles (used in warping).

### Real-World Applications
- **Autonomous vehicles:** Bird’s-eye view of roads using perspective transforms.
- **Augmented reality:** Aligning virtual objects with markers using affine transforms.
- **Robotics:** Aligning camera feeds for calibration and navigation.

## 4. Insights
- Filtering prepares images (denoise, sharpen) before higher-level tasks.
- Thresholding extracts **meaningful regions** (foreground vs. background).
- Transformations enable **geometric alignment**, crucial in vision pipelines.
- These basic operations are building blocks for advanced CV tasks like detection, segmentation, and recognition.

## 5. References
- *Digital Image Processing* by Gonzalez & Woods (classic textbook)  
- [OpenCV Image Processing Docs](https://docs.opencv.org/4.x/d7/dbd/group__imgproc.html)  
- [PyImageSearch Tutorials](https://pyimagesearch.com/)  
