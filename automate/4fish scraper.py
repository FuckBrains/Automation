import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook=xlsxwriter.Workbook("4fish.xlsx")
worksheet=workbook.add_worksheet("scraped1")

#worksheet.write("A1","name")
#worksheet.write("B1","place")
#worksheet.write("C1","salary")

num=1

for page in range(1,2):
	url="http://www.fish4.co.uk/searchjobs/?LocationId=233%2c20752050%2c20752010&keywords=bursar&radiallocation=5&countrycode=GB&Page={}&sort=Relevance".format(page)
	request=requests.get(url)
	soup=BeautifulSoup(request.text,"html.parser")
	for item in soup.findAll("li",{"class":"lister__item cf lister__item--display-logo-in-listing"}):
			try:
				jobtitle=item.findAll("h3",{"class":"lister__header"})[0].text
			except:
				jobtitle="NONE"
			try:
				name=item.findAll("span")[2].text
			except:
				name="NONE"
			try:
				place = item.findAll("span",{"class":" pipe"})[0].text
			except:
				place="NONE"
			#try:
				#salary= item.findAll("li",{"class":"salary"})[0].text
			#except:
				#salary="NONE"
			worksheet.write("A"+str(num),jobtitle)
			worksheet.write("B"+str(num),name)
			worksheet.write("C"+str(num),place)
			#worksheet.write("D"+str(num),salary)
			#print(jobtitle)
			num+=1
	print("done"+str(num))
workbook.close()