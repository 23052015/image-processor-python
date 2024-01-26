FROM gitpod/workspace-full-vnc:latest

# Install Tesseract
RUN sudo apt-get update \
    && sudo apt-get install -y tesseract-ocr