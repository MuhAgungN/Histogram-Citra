import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def apply_histogram_operations(img, operation):
    # Splitting the image into channels
    blue, green, red = cv.split(img)
    
    # Applying the specified operation to each channel
    blue = operation(blue)
    green = operation(green)
    red = operation(red)
    
    # Merging the channels back into a single image
    result_img = cv.merge([blue, green, red])
    
    return result_img

def increase_brightness(channel):
    # Example: Increase the brightness by adding 50 to each pixel value
    return np.clip(channel + 50, 0, 255)

def decrease_brightness(channel):
    # Example: Decrease the brightness by subtracting 50 from each pixel value
    return np.clip(channel - 50, 0, 255)

def multiply_brightness(channel):
    # Example: Multiply the brightness by a factor of 1.5
    return np.clip(channel * 50, 0, 255)

def divide_brightness(channel):
    # Example: Divide the brightness by a factor of 2
    return np.clip(channel / 50, 0, 255)

# Load the image
img = cv.imread("Aerial.jpg")

# Show the original image
cv.imshow("Original Image", img)

# Display the original histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# Apply and display histogram operations
brighter_img = apply_histogram_operations(img, increase_brightness)
cv.imshow("Increased Brightness", brighter_img)
plt.hist(brighter_img.ravel(), 256, [0, 256])
plt.show()

darker_img = apply_histogram_operations(img, decrease_brightness)
cv.imshow("Decreased Brightness", darker_img)
plt.hist(darker_img.ravel(), 256, [0, 256])
plt.show()

multiplied_img = apply_histogram_operations(img, multiply_brightness)
cv.imshow("Multiplied Brightness", multiplied_img)
plt.hist(multiplied_img.ravel(), 256, [0, 256])
plt.show()

divided_img = apply_histogram_operations(img, divide_brightness)
cv.imshow("Divided Brightness", divided_img)
plt.hist(divided_img.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
