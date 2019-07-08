import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook=xlsxwriter.Workbook("new.xlsx")

worksheet=workbook.add_worksheet("scraped")

worksheet.write("A1","Name")
worksheet.write("B1","E-Mail")
global num
num=2
for i in range(1,15):
	url="https://www.atod.net.au/about/member-directory/?p={}&category=0&zoom=15&is_mile=0&directory_radius=100&view=grid&hide_searchbox=0&hide_nav=0&hide_nav_views=0&hide_pager=0&featured_only=0&feature=1&perpage=20&sort=random"\
	.format(i)
	print num
	print(url)
	req=requests.get(url)
	soup=BeautifulSoup(req.text,"html.parser")
	for item in soup.findAll("div",{"class":"sabai-directory-main"}):
		print (num)
		try:
			name=item.findAll("div",{"class":"sabai-directory-title"})[0].text
			name=name.strip("\n\t\r")
		except:
			name="NONE"
		try:
			email=item.findAll("div",{"class":"sabai-directory-contact-email"})[0].text
		except:
			email="NONE"
		worksheet.write("A"+str(num),name)
		worksheet.write("B"+str(num),email)
		num+=1


workbook.close()