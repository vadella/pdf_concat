from PyPDF2 import PdfFileMerger, PdfFileReader

output_name = 'kaartjes2.pdf'

input_files = ['kaartje 1.pdf', 'kaartje 2.pdf', 'benefits.pdf',]

merger = PdfFileMerger()

with open(output_name, 'wb') as output:
    for input_filename in input_files:
        with open(input_filename, 'rb') as input_file:
            merger.append(PdfFileReader(input_file))
    merger.write(output)
merger.close()