import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('prueba.pdf')

pdf_combine(inputs)