import cv2
import numpy as np

# Read the image
image = cv2.imread('your_image.jpg')

# Extract the blue channel
blue_channel = image[:, :, 0]  # Assuming the image is in BGR format, so blue is the first channel

# Apply a threshold to create a binary mask
_, thresh = cv2.threshold(blue_channel, 240, 255, cv2.THRESH_BINARY)

# Find contours in the binary mask
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask with the same dimensions as the original image
mask = np.zeros_like(image)

# Fill the mask with white where the contours are found
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Use the mask to extract the foreground
result = cv2.bitwise_and(image, mask)


cv2.imwrite('/workspace/image-processor-python/images/removed_objects/object_removed.jpg', object_removed)