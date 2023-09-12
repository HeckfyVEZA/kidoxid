import aspose.pdf as pdf

# Load the license
# license = pdf.License()
# license.set_license("Aspose.Total.lic")

# Create a Document class object
document = pdf.Document('C:\\Users\\novikov.rn\\Downloads\\15233.pdf')

# Convert PDF to XML
document.save("PDFtoXML.xml" , pdf.SaveFormat.PDF_XML)

print("PDF to XML Converted Successfully")
 
# if __name__ == '__main__':
#     print(extract_text_from_pdf('C:\\Users\\novikov.rn\\Downloads\\15233.pdf'))