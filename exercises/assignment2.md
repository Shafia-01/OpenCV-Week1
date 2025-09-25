# Assignment 2 - Filtering & Edge Detection

## 🎯 Objective
Learn how to reduce noise with filters and detect edges in images.  
Compare different methods and their effects.

## ✅ Tasks
1. **Filtering**  
   - Gaussian Blur  
   - Median Blur  
   - Bilateral Filter  

2. **Edge Detection**  
   - Sobel Derivatives (X, Y)  
   - Laplacian Operator  
   - Canny Edge Detector  

## ▶️ How to Run
```bash
python exercises/assignment2_filters_edges.py --image path/to/sample.jpg --output_dir outputs/
```

## 📂 Output Files
- gaussian.jpg, median.jpg, bilateral.jpg
- sobel.jpg, laplacian.jpg, canny.jpg

## Key Learnings
- Filtering reduces noise but may also blur details.
- Gaussian Blur smooths uniformly, Median Blur preserves edges better, Bilateral Filter keeps sharp edges while denoising.
- Sobel & Laplacian highlight intensity changes (edges).
- Canny provides accurate, multi-stage edge detection.

## 📖 References
- [OpenCV Filtering](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
- [OpenCV Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)