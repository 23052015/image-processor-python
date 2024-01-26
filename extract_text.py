import cv2
import pytesseract
import re

# Read the image
image = cv2.imread('/workspace/image-processor-python/images/proizvodi.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or other preprocessing if needed
# ...

# Use pytesseract to perform OCR
text = pytesseract.image_to_string(gray)

# Define multiple keywords to split on
keywords = ['keyword1', 'keyword2', 'keyword3']

# Create a regular expression pattern with the specified keywords
pattern = r'\n\s*(' + '|'.join(map(re.escape, keywords)) + r')\s*'

# Split the text into articles based on the specified keywords
articles = re.split(pattern, text)

# Concatenate all articles into a single text
all_text = '\n'.join(articles)

# Save all text to a single file
output_file = '/workspace/image-processor-python/all_articles.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_text)

print(f"All articles saved to {output_file}")
