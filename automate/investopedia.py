import xlsxwriter
from bs4 import BeautifulSoup
import requests
workbook=xlsxwriter.Workbook("investopedia.xlsx")
worksheet=workbook.add_worksheet("dict")
worksheet.write("A1","Word")
worksheet.write("B1","Paragraph")
worksheet.write("C1","Breakdown")
num=2
for i in range(1,14):
	url="http://www.investopedia.com/terms/a/?page={}".format(i)
	request=requests.get(url)
	soup=BeautifulSoup(request.text,"html.parser")
	box=soup.findAll("div",{"class":"box col-2 big-item-title clear"})[0]
	for item in box.findAll("li"):
		baseurl="http://www.investopedia.com"
		added=item.findAll("a")[0].get("href")
		comp=baseurl+added
		req=requests.get(comp)
		soup2=BeautifulSoup(req.text,"html.parser")
		print comp
		contentbox=soup2.findAll("div",{"class":"content-box content-box-term"})[0]
		try:
			word = soup2.findAll("div",{"class":"layout-title only-fontsize-title title-space"})[0].findAll("h1")[0].text
		except:
			word=added
		try:
			paragraph=contentbox.findAll("p")[0].text
		except:
			paragraph="NONE"
		try:
			breakdown=contentbox.findAll("p")[1].text
		except:
			breakdown="NONE"
		worksheet.write("A"+str(num),word)
		worksheet.write("B"+str(num),paragraph)
		worksheet.write("C"+str(num),breakdown)
		
		num+=1
workbook.close()