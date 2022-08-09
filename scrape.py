from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = requests.get(start_url)

def scrape():
    soup = BeautifulSoup(browser.text, 'html.parser')

    table = soup.find("table")
    temp_list = []
    
    for tr_tags in table.find_all("tr"):
        td_tags = tr_tags.find_all("td")
        data =  [i.text.rstrip() for i in td_tags]
        temp_list.append(data)   

    name = []
    distance = []
    mass = []
    radius = []
    lum = []  
    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
        lum.append(temp_list[i][7])
    
    df = pd.DataFrame(list(zip(name, distance, mass, radius, lum)),columns=["name", "distance","mass", "radius", "lum"])
    print(df)
    df.to_csv("data.csv")


scrape()