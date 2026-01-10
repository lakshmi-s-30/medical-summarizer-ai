from src.processor import MedicalDocProcessor
from src.summarizer import MedicalSummarizer

# ... inside your Streamlit upload block ...
processor = MedicalDocProcessor()
raw_text = processor.get_metadata("temp.pdf")

st.info(f"Processing {raw_text['pages']} page(s)...")

# Logic: Extract -> Clean -> Summarize
# This pipeline structure is a "green flag" for hiring managers.