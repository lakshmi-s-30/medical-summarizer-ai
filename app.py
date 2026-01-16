import streamlit as st
import os
from src.processor import MedicalDocProcessor
from src.summarizer import MedicalSummarizer

# 1. Page Configuration
st.set_page_config(page_title="MedSum AI", page_icon="🏥", layout="centered")

st.title("🏥 Medical Document Summarizer")
st.markdown("""
Summarize complex medical reports locally and securely. 
**Privacy Note:** Your data never leaves this machine.
""")

# 2. File Uploader
uploaded_file = st.file_uploader("Upload a medical report (PDF)", type="pdf")

if uploaded_file is not None:
    # Define a temporary path to save the file
    # We use the original filename to avoid conflicts
    temp_file_path = os.path.join(os.getcwd(), f"temp_{uploaded_file.name}")

    try:
        # 3. Save the uploaded file to disk
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 4. Process Metadata (UI Feedback)
        processor = MedicalDocProcessor()
        metadata = processor.get_metadata(temp_file_path)
        
        st.success(f"✅ Document Loaded: {metadata['pages']} page(s)")
        
        # 5. Summarization Logic
        if st.button("Generate Medical Summary"):
            with st.spinner("Llama 3.1 is analyzing medical terminology... (this may take a moment)"):
                summarizer = MedicalSummarizer()
                summary = summarizer.summarize(temp_file_path)
                
                st.divider()
                st.subheader("📋 Clinical Summary")
                st.write(summary)
                
                # Option to download the summary
                st.download_button("Download Summary", data=summary, file_name="summary.txt")

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.info("Check if Ollama is running and Llama 3.1 is pulled.")

    finally:
        # 6. Clean Up: Delete the temp file after processing is done
        # This prevents the 'FileNotFound' error on next run
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

else:
    st.info("Please upload a PDF file to begin.")