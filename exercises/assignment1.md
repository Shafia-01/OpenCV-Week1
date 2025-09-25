# Assignment 1 - Basic Image Operations

## 🎯 Objective
Introduce basic image input/output and pixel-level operations in OpenCV.  
Learn how images are represented as arrays and how to manipulate them using NumPy.

## ✅ Tasks
1. **Load and display an image**  
   - Print image shape, data type, and pixel value range.

2. **Convert to grayscale**  
   - Save the grayscale image.

3. **Brightness & Contrast adjustment**  
   - Brighten the image by adding a constant.  
   - Increase contrast by scaling pixel values.

4. **Color channel separation & recombination**  
   - Split image into **Blue, Green, Red** channels.  
   - Save each channel as an image.  
   - Recombine to reconstruct the original.

5. **Negative image**  
   - Invert pixel values (`255 - value`).

## 📂 Files
- `assignment1_basics.py` — Python script implementing all tasks.  
- `assignment1.md` — This instructions file.  

## ▶️ How to Run
```bash
python exercises/assignment1_basics.py --image path/to/sample.jpg --output_dir outputs/
```

## Example Output Files
- gray.jpg - Grayscale version
- bright.jpg - Brightened image
- contrast.jpg - High-contrast image
- blue_channel.jpg, green_channel.jpg, red_channel.jpg - Individual channels
- merged.jpg - Recombined image
- negative.jpg - Negative transformation

## 🔑 Key Learnings
- OpenCV stores images as NumPy arrays (H x W x C).
- Pixel intensities range from 0–255 for uint8 images.
- Basic transformations (brightness, contrast, negative) are just arithmetic on arrays.
- Channel manipulation helps understand how RGB images are formed.

## 📖 References

- [OpenCV Image Basics](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html)
- [PyImageSearch: Basic Image Processing with OpenCV](https://pyimagesearch.com/)
