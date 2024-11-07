import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_chunks = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        if text.strip():
            text_chunks.append(text.strip())
    
    doc.close()
    return text_chunks

pdf_path = "constitution_of_india.pdf"  # Your PDF path
chunks = extract_text_from_pdf(pdf_path)
