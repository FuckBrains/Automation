import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook=xlsxwriter.Workbook("reed.xlsx")
worksheet=workbook.add_worksheet("scraped1")

#worksheet.write("A1","name")
#worksheet.write("B1","place")
#worksheet.write("C1","salary")

num=1

for page in range(1,50):
	url="https://www.reed.co.uk/jobs/england?cached=True&pageno={}&keywords=head+chefs".format(page)
	request=requests.get(url)
	soup=BeautifulSoup(request.text,"html.parser")
	for item in soup.findAll("div",{"class":"details"}):
			try:
				jobtitle=item.findAll("h3",{"class":"title"})[0].text
			except:
				jobtitle="NONE"
			try:
				tem=item.findAll("div",{"class":"posted-by"})[0]
				name = tem.findAll("a")[0].text
			except:
				name="NONE"
			try:
				place = item.findAll("li",{"class":"location"})[0].text
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