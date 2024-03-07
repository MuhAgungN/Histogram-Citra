import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def apply_histogram_operations(img, operation, value):
    # Splitting the image into channels
    blue, green, red = cv.split(img)
    
    # Applying the specified operation to each channel
    blue = operation(blue, value)
    green = operation(green, value)
    red = operation(red, value)
    
    # Merging the channels back into a single image
    result_img = cv.merge([blue, green, red])
    
    return result_img

def increase_brightness(channel, value):
    return np.clip(channel + value, 0, 255)

def decrease_brightness(channel, value):
    return np.clip(channel - value, 0, 255)

def multiply_brightness(channel, value):
    return np.clip(channel * value, 0, 255)

def divide_brightness(channel, value):
    return np.clip(channel / value, 0, 255)

# Load the image
img = cv.imread("Aerial.jpg")

# Show the original image
cv.imshow("Original Image", img)

# Display the original histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# Input user untuk memilih operasi
operation_choice = int(input("Pilih operasi (1: Penambahan, 2: Pengurangan, 3: Perkalian, 4: Pembagian): "))
value = float(input("Masukkan nilai operasi: "))

if operation_choice == 1:
    result_img = apply_histogram_operations(img, increase_brightness, value)
    operation_name = "Increased Brightness"
elif operation_choice == 2:
    result_img = apply_histogram_operations(img, decrease_brightness, value)
    operation_name = "Decreased Brightness"
elif operation_choice == 3:
    result_img = apply_histogram_operations(img, multiply_brightness, value)
    operation_name = "Multiplied Brightness"
elif operation_choice == 4:
    result_img = apply_histogram_operations(img, divide_brightness, value)
    operation_name = "Divided Brightness"
else:
    print("Pilihan operasi tidak valid")

# Display the result image and histogram
cv.imshow(operation_name, result_img)
plt.hist(result_img.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
