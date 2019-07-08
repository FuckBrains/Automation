import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook=xlsxwriter.Workbook("indeed.xlsx")
worksheet=workbook.add_worksheet("scraped2")

#worksheet.write("A1","name")
#worksheet.write("B1","place")
#worksheet.write("C1","salary")

num=1

for page in range(10,500,10):
	url="https://www.indeed.co.uk/jobs?q=chief+engineer&l=england&start={}".format(page)
	request=requests.get(url)
	soup=BeautifulSoup(request.text,"html.parser")
	for item in soup.findAll("div",{"class":"row"}):
			try:
				jobtitle=item.findAll("h2",{"class":"jobtitle"})[0].text
			except:
				jobtitle="NONE"
			try:
				name = item.findAll("span",{"class":"company"})[0].text
			except:
				name="NONE"
			try:
				place = item.findAll("span",{"class":"location"})[0].text
			except:
				place="NONE"
			worksheet.write("A"+str(num),jobtitle)
			worksheet.write("B"+str(num),name)
			worksheet.write("C"+str(num),place)
			num+=1
	print("done"+str(num))
workbook.close()