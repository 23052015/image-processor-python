import cv2
import pytesseract



# Read the image
image = cv2.imread('/workspace/image-processor-python/images/proizvodi.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or other preprocessing if needed
# ...

# Use pytesseract to perform OCR
text = pytesseract.image_to_string(gray)

# Print the extracted text
print("Extracted Text:")
print(text)