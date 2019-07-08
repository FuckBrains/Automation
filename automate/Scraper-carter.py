import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook=xlsxwriter.Workbook("carter.xlsx")
worksheet=workbook.add_worksheet("scraped3")

#worksheet.write("A1","name")
#worksheet.write("B1","place")
#worksheet.write("C1","salary")

num=1

for page in range(30,50):
	url="https://www.caterer.com/jobs/food-and-beverage?page={}".format(page)
	request=requests.get(url)
	soup=BeautifulSoup(request.text,"html.parser")
	for item in soup.findAll("div",{"class":"job"}):
			try:
				jobtitle=item.findAll("div",{"class":"job-title"})[0].text
				if "waiter" or "staff" or "supervisor" or "part time" or "assistant" in jobtitle:
					pass
			except:
				jobtitle="NONE"
			try:
				name = item.findAll("li",{"class":"company"})[0].text
			except:
				name="NONE"
			try:
				place = item.findAll("span",{"property":"address"})[0].text
			except:
				place="NONE"
			try:
				salary= item.findAll("li",{"class":"salary"})[0].text
			except:
				salary="NONE"
			print(jobtitle)
			worksheet.write("A"+str(num),jobtitle)
			worksheet.write("B"+str(num),name)
			worksheet.write("C"+str(num),place)
			worksheet.write("D"+str(num),salary)
			num+=1
	print("done"+str(num))
workbook.close()