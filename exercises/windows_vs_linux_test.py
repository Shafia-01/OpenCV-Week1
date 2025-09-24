"""
windows_vs_linux_test.py
------------------------------------
Demonstrates differences in OpenCV window handling
between Linux and Windows when using threads.

- On Linux (X11/Wayland):
  * cv2.imshow MUST run in the main thread
  * Running in a worker thread may freeze or crash

- On Windows:
  * More tolerant; may work in a worker thread
  * Still recommended to keep GUI calls in main thread
"""

import cv2
import threading
import numpy as np

# Create a simple test image (blue-green gradient)
img = np.zeros((300, 300, 3), dtype=np.uint8)
for i in range(img.shape[0]):
    img[i, :, 0] = i % 256          # Blue channel wraps 0–255
    img[i, :, 1] = (255 - i) % 256  # Green channel wraps 0–255

def show_in_thread():
    """Attempt to run imshow in a worker thread"""
    cv2.imshow("Thread Window", img)
    cv2.waitKey(3000)  # Display for 3 seconds
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("=== OpenCV imshow threading test ===")
    print("1) Showing window in MAIN thread (should work everywhere)...")
    cv2.imshow("Main Thread Window", img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    print("\n2) Showing window in WORKER thread (may fail on Linux)...")
    t = threading.Thread(target=show_in_thread)
    t.start()
    t.join()

    print("\nTest complete.")
    print("On Linux, the second window may freeze or crash.")
    print("On Windows, it often works, but main-thread usage is still recommended.")
