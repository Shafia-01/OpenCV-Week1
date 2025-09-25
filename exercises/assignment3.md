# Assignment 3 - Thresholding & Segmentation

## 🎯 Objective
Separate foreground and background using thresholding, and detect shapes using contours.

## ✅ Tasks
1. **Global Thresholding** (fixed threshold value).  
2. **Adaptive Thresholding** (local neighborhood thresholds).  
3. **Otsu’s Method** (automatic global threshold).  
4. **Contour Detection** (draw object boundaries after thresholding).  

## ▶️ How to Run
```bash
python exercises/assignment3_thresholding.py --image path/to/sample.jpg --output_dir outputs/
```

## 📂 Output Files
- threshold_global.jpg
- threshold_adaptive.jpg
- threshold_otsu.jpg
- contours.jpg

## 🔑 Key Learnings
- Global thresholding works well with uniform lighting.
- Adaptive thresholding handles uneven illumination.
- Otsu’s method is robust for bimodal histograms.
- Contours are useful for object detection, counting, and shape analysis.

## 📖 References
- [OpenCV Thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)
- [OpenCV Contours](https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html)