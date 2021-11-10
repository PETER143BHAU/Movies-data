from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint as pp
import time,os
import json
import requests
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

driver=webdriver.Chrome('/home/peter/chromedriver_linux (1)/chromedriver')
movie_linking = 'http://cinemacity.live:9090/Hindi%20Movie%20HD/'
driver_url = driver.get(str(movie_linking))
html=driver.execute_script('return document.documentElement.outerHTML;')
soup=BeautifulSoup(html,'html.parser')
driver.close()


movie_urls = []
movie_names = []
movie_full_url = []
movie_pic_full_url_list = []
movie_mp4_full_url_list = []
df  = pd.read_excel('/home/peter/Documents/Cinemacity.xlsx' , engine = 'openpyxl')

def movie_url_and_name():
	Main_link = soup.find('tbody')
	movie = Main_link.find_all('div' , class_ = 'forumlink fileLink')
	count = 1
	for url in movie:

		movie_url = url.find('a')['href']
		movie_urls.append(movie_url)
		movie_name = url.find('a').get_text()
		movie_names.append(movie_name)
		full_url = str(movie_linking + movie_url)
		movie_full_url.append(full_url)
		movie_pic_url1 = str(movie_url.replace('/' , '.jpg'))
		movie_mp4_url1 = str(movie_url.replace('/' , '.mp4'))

		movie_pic_full_url=str(full_url+movie_pic_url1)
		movie_pic_full_url_list.append(movie_pic_full_url)
		movie_mp4_full_url1=str(full_url+movie_mp4_url1)
		movie_mp4_full_url_list.append(movie_mp4_full_url1)
		print(movie_name,'          ',movie_mp4_full_url1)


		all_df = {
		'Movie Name': movie_names[1:],
		'Movie Link' : movie_urls [1:],
		'Full_url':movie_full_url[1:],
		'Movie_pic_url':movie_pic_full_url_list[1:],
		'Movie_mp4_url':movie_mp4_full_url_list[1:]

		}
	dataframe = pd.DataFrame(all_df)
	to_excel = dataframe.to_excel('/home/peter/Documents/Cinemacity.xlsx',sheet_name  = 'Sheet1')

movie_url_and_name()