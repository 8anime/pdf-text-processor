
import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def extractTextFromPDF(pdfFile, outputTextFile):
    """
    Extracts text content from a PDF file and writes it to a text file.

    Parameters:
    - pdfFile (str): The path to the input PDF file.
    - outputTextFile (str): The path to the output text file where extracted text will be saved.

    This function reads the content of the input PDF file page by page and extracts the text.
    The extracted text is then written to the specified output text file using UTF-8 encoding.

    If any exceptions occur during the process, they are caught and printed to the console.

    Returns:
    None
    """
    text = ''  # Store the extracted text
    try:
        with open(pdfFile, 'rb') as readFile:            # Open the PDF file in a context manager
            pdfReader = PyPDF2.PdfFileReader(readFile)   # Read the PDF file
            for pageNum in range(pdfReader.numPages):    # Use a for loop to go through each page
                page = pdfReader.getPage(pageNum)        # Get each page
                text += page.extractText()               # Extract text from each page and add it to the text variable

        # Open the output text file in write mode and write the text
        with open(outputTextFile, 'w', encoding='utf-8') as textFile:
            textFile.write(text)   # Write the extracted text to a text file
    except Exception as e:
        print(e)


def createPDFFromText(inputTextFile, outputPDFFile):
    """
    Creates a PDF document from text content in a text file.

    Parameters:
    - inputTextFile (str): The path to the input text file containing the text content.
    - outputPDFFile (str): The path to the output PDF file to be created.

    This function reads the text content from the input text file and generates a PDF document.
    It formats the text, sets fonts and sizes, and paginates the content to fit within the page size.
    The resulting PDF document is saved to the specified output PDF file.

    If the text content exceeds the page size, the function automatically starts a new page and continues
    the text on the next page.

    Returns:
    None
    """
    try:
        with open(inputTextFile, 'r', encoding='utf-8') as textFile:  # Open the Text file in a context manager
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

        c.save()   # Save the contents in the PDF file

    except Exception as e:
        print(e)

