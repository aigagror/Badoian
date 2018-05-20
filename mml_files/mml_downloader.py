import urllib2

for year in reversed(range(2003,2017)):
	for month in [10,11,12,1,2,3]:

		mont_str = "{0:0=2d}".format(month)

		url = 'http://www.mathmeets2.com/mml_2017_2018/archived_meets/mml_{}_{}/{}{}_mml.pdf'.format(year, year + 1, year if month > 3 else year + 1, mont_str)

		print(url)

		response = urllib2.urlopen(url)

		file = open("mml_{}_{}.pdf".format(year if month > 3 else year + 1, mont_str), 'w')
		file.write(response.read())
		file.close()

print("Completed")	
