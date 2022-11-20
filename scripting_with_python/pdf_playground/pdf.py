import os.path

import PyPDF2
from pathlib import Path


def rotate_pdf(filepath):
    # read binary
    reader = PyPDF2.PdfReader(filepath)
    page = reader.getPage(0)
    page = page.rotate_clockwise(90)

    writer = PyPDF2.PdfWriter()
    writer.addPage(page)
    filepath, _ = os.path.splitext(filepath)
    output_filepath = filepath + '_rotated' + '.pdf'
    print(output_filepath)
    with open(output_filepath, mode="wb") as new_file:
        writer.write(new_file)


def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write("super.pdf")


def merge_watermark(filename, watermark):
    watermark_reader = PyPDF2.PdfReader(watermark)
    watermark_page = watermark_reader.pages[0]

    file_reader = PyPDF2.PdfReader(filename)
    writer = PyPDF2.PdfWriter()
    for page_number in range(len(file_reader.pages)):
        page = file_reader.pages[page_number]
        page.mergePage(watermark_page)
        writer.addPage(page)

    clean_filename, ext = os.path.splitext(filename)
    output_filename = clean_filename + '_with_watermark' + ext
    writer.write(output_filename)


if __name__ == "__main__":
    # To trigger rotate_pdf function
    filepath = Path("pdfs", "dummy.pdf")
    rotate_pdf(filepath)

    # To trigger merge_pdfs function
    # inputs = sys.argv[1:]
    # merge_pdfs(inputs)

    # To trigger merge_watermark function
    merge_watermark("super.pdf", "pdfs/wtr.pdf")
