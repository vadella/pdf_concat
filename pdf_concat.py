from PyPDF2 import PdfFileMerger

input1_name = 'Babyborrelkaartje.pdf'
input2_name ='kaartje 1.pdf'
input3_name = 'kaartje 2.pdf'
output_name = 'kaartjes.pdf'


merger = PdfFileMerger()

with open(input1_name, 'rb')as input1, \
    open(input2_name, 'rb')as input2, \
    open(input3_name, 'rb')as input3, \
    open(output_name, 'wb') as output:
    merger.append(fileobj = input1)
    merger.append(fileobj = input2)
    merger.append(fileobj = input3)
    merger.write(output)
