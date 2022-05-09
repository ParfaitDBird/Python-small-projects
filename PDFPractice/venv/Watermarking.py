import PyPDF2

guardado = PyPDF2.PdfFileWriter()
with open ('Super.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    with open('wtr.pdf','rb') as new_file:
        marca = PyPDF2.PdfFileReader(new_file)
        for pag in range(reader.getNumPages()):
            pag_doc = reader.getPage(pag)
            pag_doc.mergePage(marca.getPage(0))
            guardado.addPage(pag_doc)
        with open('salida.pdf','wb') as marcado:
            guardado.write(marcado)