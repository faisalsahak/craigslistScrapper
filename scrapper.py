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
	def __init__(self, location, item, postal=""
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
	

	