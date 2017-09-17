import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/kiev/q-samsung/?page=1"


def get_html(url):
	r = requests.get(url)
	return r.text


def get_page_count(html):
	soup = BeautifulSoup(html, "lxml")
	pages = soup.find("div", class_="pager rel clr").find_all("span", class_="item fleft")[-1].find("span").text
	return int(pages)

def write_csv(data):
	with open("olx.csv", 'a', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow( (data['title'],
						 data['price'],
						 data['date'],
						 data['url']) )

def get_page_data(html):
	soup = BeautifulSoup(html, "lxml")
	ads = soup.find("table", {"id": "offers_table"}).find_all("tr", class_="wrap")
	#return len(ads)
	for item in ads:
		try:
			title = item.find("a", class_="marginright5 link linkWithHash detailsLink").find("strong").text.replace('n', "")
		except:
			title = ""
		try:
			price = item.find("p", class_="price").find("strong").text.strip()
		except: 
			price = ""
		try:
			url = item.find("a", class_="marginright5 link linkWithHash detailsLink").get("href")
		except: 
			url = ""
		try:
			date = item.find("p", class_="color-9 lheight16 marginbott5 x-normal").text.strip()
		except:
			date = ""

		data = {"title": title,
				"price": price,
				"url": url,
				"date": date}
		write_csv(data)


def main():
	base_url = "https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/kiev/"
	query_part = "q-samsung/"
	page_part = "?page="
	total_pages = get_page_count(get_html(URL))
	for i in range(1, total_pages+1):
		url_gen = base_url + query_part + page_part + str(i) 
		html = get_html(url_gen)
		get_page_data(html)
		#print(url_gen)
# if __name__ == "main":
# 	main()
# 	
main()