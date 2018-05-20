import urllib.request
import shutil, os
from PyPDF2 import PdfFileReader, PdfFileWriter

shutil.rmtree('mml/', ignore_errors=True)
os.makedirs('mml/')

for year in reversed(range(2003,2017)):
	for month in [10,11,12,1,2,3]:

		mont_str = "{0:0=2d}".format(month)

		url = 'http://www.mathmeets2.com/mml_2017_2018/archived_meets/mml_{}_{}/{}{}_mml.pdf'.format(year, year + 1, year if month > 3 else year + 1, mont_str)

		print(url)

		directory = "mml/{}_{}/".format(year if month > 3 else year + 1, mont_str)
		os.makedirs(directory)

		pdf = directory + 'file.pdf'

		response = urllib.request.urlretrieve(url, pdf)

		inputpdf = PdfFileReader(open(pdf, "rb"))

		for i in range(inputpdf.numPages):
		    output = PdfFileWriter()
		    output.addPage(inputpdf.getPage(i))
		    with open(directory + "{}.pdf".format(i), "wb") as outputStream:
		        output.write(outputStream)

print("Completed")	
