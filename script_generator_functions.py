import fitz  # PyMuPDF


# Function to extract the synthetic dataset from a pdf doc "scripts_dataset.pdf"
def extract_text_from_pdf(pdf_path):
    # Open doc
    doc = fitz.open(pdf_path)
    # Create 'texts' as empty list
    texts = []
    # Loop to iterate through each page in the PDF doc and appending the content to 'texts' list
    for page in doc:
        texts.append(page.get_text())
    return " ".join(texts)

# dataset_text = extract_text_from_pdf("scripts_dataset.pdf")
# print(dataset_text)