import fitz  # PyMuPDF
import re

class MedicalDocProcessor:
    def __init__(self):
        # Common medical abbreviations to protect during cleaning
        self.protected_terms = ["mg", "mcg", "dL", "BP", "HR"]

    def clean_text(self, text: str) -> str:
        """
        Cleans extracted PDF text for better LLM consumption.
        """
        # Remove multiple newlines and extra spaces
        text = re.sub(r'\s+', ' ', text)
        
        # Basic PII Masking (Startup-lite version)
        # This shows you're thinking about HIPAA/Privacy
        text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN-REDACTED]', text)
        
        return text.strip()

    def get_metadata(self, file_path: str) -> dict:
        """
        Extracts document metadata to show in the UI.
        """
        with fitz.open(file_path) as doc:
            return {
                "pages": len(doc),
                "format": doc.metadata.get("format", "Unknown"),
                "author": doc.metadata.get("author", "Hidden")
            }