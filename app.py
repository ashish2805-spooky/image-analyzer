import streamlit as st
from PIL import Image
from ultralytics import YOLO
from rembg import remove
import io

# 1. Page Config
st.set_page_config(page_title="AI Image Analyzer", page_icon="🤖", layout="wide")

# 2. Load AI Model
@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')

model = load_model()

# 3. Sidebar
st.sidebar.title("About the AI")
st.sidebar.write("This app uses YOLOv8 for detection and Rembg for background removal.")
st.sidebar.markdown("---")
st.sidebar.markdown("- 👤 People & Objects")
st.sidebar.markdown("- ✂️ Background Removal")
st.sidebar.markdown("- 💾 Download Results")

# 4. Main UI
st.title("🤖 AI Image Analyzer Pro")
st.write("Upload an image to start analyzing!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 Detect Objects"):
            with st.spinner("AI is thinking..."):
                results = model(image)
                st.image(results[0].plot(), caption="Detected Objects", use_container_width=True)
                st.success("Detection complete!")
            
    with col2:
        if st.button("✂️ Remove Background"):
            with st.spinner("Removing background..."):
                input_image = image.convert("RGB")
                output_image = remove(input_image)
                st.image(output_image, caption="Background Removed", use_container_width=True)
                
                # Convert image to bytes for downloading
                buf = io.BytesIO()
                output_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="💾 Download Image",
                    data=byte_im,
                    file_name="result.png",
                    mime="image/png"
                )
                st.success("Background removed!")
else:
    st.info("👆 Please upload an image to get started.")