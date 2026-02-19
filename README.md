**Medical Summarizer AI**
Medical Summarizer AI is a specialized tool designed to summarize complex medical reports locally. By leveraging Llama 3.1 via Ollama, this application ensures that sensitive patient data never leaves the local machine, addressing the critical privacy concerns (HIPAA compliance) associated with cloud-based LLMs.

**Key Features**
100% Local Inference: Uses Llama 3.1 via Ollama to ensure total data privacy.

Advanced Document Processing: Custom PDF parsing and cleaning logic using PyMuPDF.

Smart Chunking: Employs RecursiveCharacterTextSplitter to maintain medical context across long documents.

PII Masking: Automated regex-based sanitization of sensitive information (SSNs, Phone Numbers) before processing.

Professional UI: Built with Streamlit for a seamless, interactive user experience.

**Technical Architecture**
The project follows a modular "Pipeline" architecture:

Ingestion: Streamlit handles the PDF upload and saves it to a secure temporary local path.

Processing: MedicalDocProcessor cleans the text and extracts metadata.

Summarization: MedicalSummarizer uses a Map-Reduce chain to handle large documents that exceed the model's context window.

Local LLM: The system communicates with the Ollama API to run Llama 3.1 locally.

**Getting Started**
*Prerequisites*
Python 3.10+

Ollama installed and running

Llama 3.1 model pulled: ollama pull llama3.1

*Installation*
Clone the repo:

Bash
git clone https://github.com/yourusername/med-summarizer-ai.git
cd med-summarizer-ai
Set up Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows
Install Dependencies:

Bash
pip install -r requirements.txt
Running the App
Bash
streamlit run app.py

**Challenges & Solutions**
Version Migrations: Navigated the LangChain v1.0 migration by implementing langchain-classic and the new standalone langchain-text-splitters package.

Memory Management: Implemented a try...finally block in the file handler to ensure temporary medical data is deleted immediately after processing.

Context Window Issues: Used the Map-Reduce strategy to summarize long medical histories that would otherwise crash a standard LLM prompt.

**Tech Stack**
Language: Python 3.11

AI Framework: LangChain, Ollama

LLM: Llama 3.1 (8B)

Frontend: Streamlit

PDF Engine: PyMuPDF (fitz)

