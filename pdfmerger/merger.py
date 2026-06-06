import PyPDF2
pdfFiles = ['pdfmerger/sample.pdf', 'pdfmerger/sample2.pdf']
pdfMerge = PyPDF2.PdfMerger()
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)
    pdfFile.close()
    pdfMerge.write('pdfmerger/pdfmerged.pdf')