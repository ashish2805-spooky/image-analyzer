# AI Image Analyzer Pro 🤖

A powerful web application that allows users to analyze images using Artificial Intelligence.

## Features
- **Object Detection:** Detects and labels 80+ common objects using YOLOv8.
- **Background Removal:** Automatically removes backgrounds from images using AI segmentation.
- **Downloadable Results:** Save your processed images directly to your device.

## Built With
- [Streamlit](https://streamlit.io/) - The web framework
- [Ultralytics YOLOv8](https://ultralytics.com/) - For object detection
- [rembg](https://github.com/danielgatis/rembg) - For background removal

## How to run locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`