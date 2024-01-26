import cv2
import numpy as np

# Read the image
image = cv2.imread('/workspace/image-processor-python/images/example.jpg')

# Convert the image from BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a color range for potential colors of the bottle (you might need to adjust this)
lower_color_bottle = np.array([0, 0, 0], dtype=np.uint8)
upper_color_bottle = np.array([179, 255, 100], dtype=np.uint8)

# Create a binary mask for the potential color range
mask_potential_color = cv2.inRange(hsv, lower_color_bottle, upper_color_bottle)

# Find contours in the binary mask
contours, _ = cv2.findContours(mask_potential_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask with the same dimensions as the original image
mask_combined = np.zeros_like(image, dtype=np.uint8)  # Ensure the correct data type

# Iterate through contours and draw them on the combined mask
for contour in contours:
    area = cv2.contourArea(contour)
    # Filter contours based on area (adjust the threshold as needed)
    if area > 1000:  # You might need to adjust this threshold
        cv2.drawContours(mask_combined, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

# Invert the combined mask to get the region to be removed
mask_removed = cv2.bitwise_not(mask_combined)

# Convert the mask_removed to 1 channel (grayscale)
mask_removed = cv2.cvtColor(mask_removed, cv2.COLOR_BGR2GRAY)

# Get the region to be removed from the original image
object_removed = cv2.bitwise_and(image, image, mask=mask_removed)

# Save the result to a file
cv2.imwrite('/workspace/image-processor-python/images/removed_objects/object_removed.jpg', object_removed)
