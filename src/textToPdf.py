
import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

PDF_FILE = os.path.join(ROOT_DIR, 'data', 'SurveyAct25of1961.pdf')
TEXT_FILE = os.path.join(ROOT_DIR, 'survey_data.txt')
OUTPUT_PDF = os.path.join(ROOT_DIR, 'survey.pdf')


def extractTextFromPDF(pdfFile, outputTextFile):
    text = ''
    try:
        with open(pdfFile, 'rb') as readFile:
            pdfReader = PyPDF2.PdfFileReader(readFile)
            for pageNum in range(pdfReader.numPages):
                page = pdfReader.getPage(pageNum)
                text += page.extractText()

        # Open the output text file in write mode and write the text
        with open(outputTextFile, 'w', encoding='utf-8') as textFile:
            textFile.write(text)
    except Exception as e:
        print(e)


def createPDFFromText(inputTextFile, outputPDFFile):
    try:
        with open(inputTextFile, 'r', encoding='utf-8') as textFile:
            text = textFile.read()  # Read the text file

        # Drawing surface that allows you to add various elements such as text, shapes,
        # images and more to a PDF page.
        c = canvas.Canvas(outputPDFFile, pagesize=letter)

        # Set the font and size for the text
        c.setFont('Helvetica', 12)

        # Calculate the layout of the text based on the page size
        width, height = letter    # Obtain width and height of a standard page size which is (612, 792) points.
        x, y = 50, height - 50    # Adjust the position as needed

        # Split the text into lines to fit within the page
        lines = text.split('\n')  # When a new line character is encountered, the line is split.
        for line in lines:        # Loop through the split lines
            if y < 50:            
                c.showPage()      # Start a new page if the current one is full
                y = height - 50   # Reset the y position
            c.drawString(x, y, line)
            y -= 15  # Adjust the spacing between lines

        c.save()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # Extract text from the PDF and save it to a text file
    extractTextFromPDF(PDF_FILE, TEXT_FILE)

    # Create a PDF from the text file
    createPDFFromText(TEXT_FILE, OUTPUT_PDF)