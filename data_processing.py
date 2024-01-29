# This file handles data extraction from PDFs and other data processing tasks.
import script_generator_functions
import pandas as pd


# Extract synthetic dataset scripts from pdf
def extract_text_from_pdf(pdf_path):
    # Placeholder for PDF text extraction logic
    return script_generator_functions.extract_text_from_pdf(pdf_path)

# Save generated scripts to excel
def save_to_excel(scripts_data, file_path="output/generated_scripts.xlsx"):
    df = pd.DataFrame(scripts_data, columns=["Script", "Emotion", "Model 1: Evaluation", "Model 2: Evaluation", "Model 3: Evaluation"])
    df.to_excel(file_path, index=False)
