# streamlit_app.py
import streamlit as st
import os
import time
from PIL import Image

def main():
    st.set_page_config(page_title="Virtual Try-On", layout="centered")
    
    st.title("👗 Virtual Clothing Try-On")
    st.markdown("Upload a photo of yourself and a clothing item to see how it looks!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload Person Image")
        person_image = st.file_uploader("Choose a full-body photo...", 
                                      type=["jpg", "jpeg", "png"], 
                                      key="person_upload")
        
        if person_image:
            st.image(person_image, caption="Uploaded Person Image", width=300)
            with open("static/origin_web.jpg", "wb") as f:
                f.write(person_image.getbuffer())
    
    with col2:
        st.subheader("Upload Clothing Item")
        cloth_image = st.file_uploader("Choose a clothing item...", 
                                     type=["jpg", "jpeg", "png"], 
                                     key="cloth_upload")
        
        if cloth_image:
            st.image(cloth_image, caption="Uploaded Clothing Item", width=300)
            with open("static/cloth_web.jpg", "wb") as f:
                f.write(cloth_image.getbuffer())
    
    st.subheader("Step 3: Generate Result")
    if st.button("Run Virtual Try-On"):
        if not (person_image and cloth_image):
            st.error("Please upload both images first!")
            return
            
        with st.spinner("Processing... This may take 2-3 minutes"):
            start_time = time.time()
            
            try:
                # Run the main processing script
                os.system("python3 main.py")
                
                # Display result
                st.subheader("Virtual Try-On Result")
                if os.path.exists("static/finalimg.png"):
                    result_image = Image.open("static/finalimg.png")
                    st.image(result_image, caption="Final Result", width=400)
                else:
                    st.error("Processing failed - no output generated")
                
                st.success(f"Processing time: {time.time()-start_time:.1f} seconds")
                st.markdown("### Tips:")
                st.markdown("- Use well-lit, front-facing photos")
                st.markdown("- Avoid loose clothing on model")
                st.markdown("- Show full body in frame")
                    
            except Exception as e:
                st.error(f"Error during processing: {str(e)}")

if __name__ == "__main__":
    main()
