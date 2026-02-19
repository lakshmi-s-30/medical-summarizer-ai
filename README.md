# Medical Summarizer AI: Privacy-First Medical Summarizer

**Medical Summarizer AI** is an end-to-end solution for summarizing complex medical reports locally. By leveraging **Llama 3.1** via **Ollama**, it ensures that sensitive patient data never leaves your hardware, providing a secure alternative to cloud-based LLM APIs.

---

## Key Features
- **100% Data Privacy:** Zero data sent to external servers; all processing happens locally.
- **Medical Intelligence:** Powered by Llama 3.1 (8B) for high-accuracy clinical summaries.
- **Smart Chunking:** Uses `RecursiveCharacterTextSplitter` to handle long PDFs without losing context.
- **Instant Deployment:** Interactive UI built with Streamlit for rapid document analysis.

---

## Technical Architecture



The application follows a modular pipeline designed for scalability:
1. **Frontend:** Streamlit handles file ingestion and displays results.
2. **Processor:** A custom module cleans PDF text and handles metadata extraction using `PyMuPDF`.
3. **Summarizer Engine:** Uses **LangChain's Map-Reduce** chain to compress long medical texts into concise, actionable insights.

---

## Getting Started

### Prerequisites
* **Python:** 3.10 or higher
* **Ollama:** [Download here](https://ollama.com/)
* **Local Model:** Run `ollama pull llama3.1` in your terminal.

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/medical-summarizer-ai.git](https://github.com/yourusername/medical-summarizer-ai.git)
   cd medical-summarizer-ai
