import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak


def dict_to_sing_pdf(data):
    # Define the file name and document size
    file_name = "Editorials.pdf"

    # Create a new SimpleDocTemplate object
    pdf_template = SimpleDocTemplate(file_name, pagesize=A4)

    # Define the title style and center alignment
    title_style = getSampleStyleSheet()["Title"]
    title_style.alignment = 1

    # Define the paragraph style and justify alignment
    paragraph_style = getSampleStyleSheet()["Normal"]
    paragraph_style.alignment = 4

    # Define the story list to hold the title and paragraphs
    story = []

    # Loop through each key-value pair in the dictionary
    for title, paragraph in data.items():
        # Add the title to the story with center alignment
        story.append(Paragraph(title, title_style))
        story.append(Paragraph("<br/>", paragraph_style))

        # Split the paragraph into lines and add each line to the story
        lines = paragraph.split("\n")
        for line in lines:
            story.append(Paragraph(line, paragraph_style))
        story.append(PageBreak())

    # Add the story to the PDF template and build the PDF
    pdf_template.build(story)


def dict_to_mul_pdf(data):
    # Define the directory name for PDF files
    directory_name = "Editorials"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Define the file name and document size
    for title, paragraph in data.items():
        file_name = f"{directory_name}/{title}.pdf"

        # Create a new SimpleDocTemplate object
        pdf_template = SimpleDocTemplate(file_name, pagesize=A4)

        # Define the title style and center alignment
        title_style = getSampleStyleSheet()["Title"]
        title_style.alignment = 1

        # Define the paragraph style and justify alignment
        paragraph_style = getSampleStyleSheet()["Normal"]
        paragraph_style.alignment = 4

        # Define the story list to hold the title and paragraphs
        story = []

        # Add the title to the story with center alignment
        story.append(Paragraph(title, title_style))
        story.append(Paragraph("<br/>", paragraph_style))

        # Split the paragraph into lines and add each line to the story
        lines = paragraph.split("\n")
        for line in lines:
            story.append(Paragraph(line, paragraph_style))
        story.append(Paragraph("<br/>", paragraph_style))

        # Add the story to the PDF template and build the PDF
        pdf_template.build(story)
