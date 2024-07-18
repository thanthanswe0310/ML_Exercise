#importing libraries

import pandas as pd 
import numpy as np 

from bs4 import BeautifulSoup
import requests

print("Web Scrapping !")

source=requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M").text

soup=BeautifulSoup(source,'lxml')

table=soup.find('table')

post_code_can=pd.read_html(table.prettify(),header=None,skiprows=0)[0]

print(post_code_can.head())