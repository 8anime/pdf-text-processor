
import os

from src.textToPdf import extractTextFromPDF, createPDFFromText

# Determine the absolute path of the directory containing the current script file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the input PDF file to be processed
PDF_FILE = os.path.join(ROOT_DIR, 'data', 'SurveyAct25of1961.pdf')

# Path to the output text file where extracted text will be saved
TEXT_FILE = os.path.join(ROOT_DIR, 'survey_data.txt')

# Path to the output PDF file to be generated from the text data
OUTPUT_PDF = os.path.join(ROOT_DIR, 'survey.pdf')


if __name__ == '__main__':
    # Extract text from the PDF and save it to a text file
    extractTextFromPDF(PDF_FILE, TEXT_FILE)

    # Create a PDF from the text file
    createPDFFromText(TEXT_FILE, OUTPUT_PDF)