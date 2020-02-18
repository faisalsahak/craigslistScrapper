from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox')
# browser = webdriver.Firefox(firefox_binary=binary)

from bs4 import BeautifulSoup
import urllib.request

class CraigslistScrapper(object):
	def __init__(self, location, item, postal="", radius="", max_price="", min_price="0", area="",typeOfSearch="sss", min_bedrooms=""): #parameters when creating the instance of the class
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius
		self.item = item
		self.area = area
		self.typeOfSearch = typeOfSearch
		self.min_price = min_price
		self.min_bedrooms = min_bedrooms

		self.url = ""
		if postal != "" and max_price!= "" and radius != "":
			print("============>>> if running")
			#search query by all the parameters
			self.url = f"https://{location}.craigslist.org/search{area}/{typeOfSearch}?query={item}&search_distance={radius}&postal={postal}&min_price={min_price}&max_price={max_price}"

		elif postal == "" and radius== "":
			print("============>>> elif running")
			self.url = f"https://{location}.craigslist.org/search{area}/{typeOfSearch}?query={item}&min_price={min_price}&max_price={max_price}{min_bedrooms}"			
		else:
			print("============>>> else running")
			self.url = f"https://{location}.craigslist.org/search{area}/{typeOfSearch}?query={item}&search_distance={radius}&postal={postal}&min_price={min_price}&max_price={max_price}"





		self.driver = webdriver.Firefox() #this instantiates our browser, the link will be opened in firefox
		self.delay = 3 # amount of time that will delay to make sure the script works properly

	def load_craigslist_url(self):
		self.driver.get(self.url)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform")))
			print("page is ready")
		except TimeoutException:
			print("Loading took too long") #if this is printed, increase the delay time above
	

	def extract_post_information(self):
		all_posts = self.driver.find_elements_by_class_name("result-row")# gets all the items on the page that has the css class result-row
		
		dates = []
		titles = []
		prices = []

		# post_title_list = [] #stores all the page item titles in this list
		for post in all_posts:
			title = post.text.split("$")

			if title[0] == '': #something the title is the first index, other times the second index
				title = title[1]
			else:
				title = title[0]

			title = title.split("\n") #spliting the title by the new line
			price = title[0] #getting the price, which is the first element of the array
			title = title[-1] #getting the title, which is the last element in the array
			title = title.split(" ")

			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + " " + day

			# print("PRICE: " + price)
			# print("TITLE: " + title)
			# print("Date: " + date)
			# int_price = int(price)
			# print(type(int_price))
			# if int_price < 5:
			# 	continue

			titles.append(title)
			prices.append(price)
			dates.append(date)

		return titles, prices, dates


		# return post_title_list




	def extract_post_urls(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		for link in soup.findAll("a", {"class": "result-title hdrlnk"}): #finds all the a tags that have the class "result-title hdrlnk"
			print(link['href'])
			url_list.append(link["href"])
		return url_list


	def quit(self):#closes the browser when finished loading the links
		self.driver.close()

# van areas => burnaby/newwest => "/bnc"  delta/surrey/langley => "/rds"  north Shore => "/nvn"
# richmond => "/rch"   tricities/pitt/maple => "/pml"  vancouver => "/van"
areas = ["/bnc", "/rds", "/nvn", "/rch", "/pml", "/van"]

#for sale => sss, housing => hhh, jobs=> jjj, resume=> rrr,  services => bbb, , gigs => ggg,
typeOfSearch =["sss", "hhh", "jjj", "rrr", "bbb", "ggg"]
item = "5 bedroom"
location = "vancouver"
postal = "v3j2s1"
max_price = "2200"
min_price = "500"
radius = "5"
min_bedrooms = "&min_bedrooms=3"

scrapper = CraigslistScrapper(location, item,"","", max_price,min_price, areas[0], typeOfSearch[1])

scrapper.load_craigslist_url()
titles, prices, dates = scrapper.extract_post_information()
print(titles)
# scrapper.extract_post_urls()
# scrapper.quit()










