from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver 
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

options=webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get(START_URL)

scraped_data=[]
def scrape():
    bright_star_table=BeautifulSoup.find("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')
    for row in table_rows:
            table_cols=row.find_all('td')
            print(table_cols)
            temp_list=[] 
            for col_data in table_cols:
                  #print(col_data.text)
                  data=col_data.text.strip()
                  print(data)
                  temp_list.append(data)
            scraped_data.append(temp_list) 
            ## ADD CODE HERE ##
    browser.find_element(By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



        
# Calling Method    
scrape()

star_data=[]

for i in range (0,len(scraped_data)):
      Star_names = scraped_data[i][1]
      Distance = scraped_data[i][3]
      Mass = scraped_data[i][5]
      Radius = scraped_data[i][6]
      Lum = scraped_data[i][7]

      required_data=[Star_names,Distance,Mass,Radius,Lum]
      star_data.append(required_data)

headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
star_df_1=pd.DataFrame(star_data,columns=headers)

# Convert to CSV
star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")

