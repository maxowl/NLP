#!/usr/bin/python
import pandas as pd
import re
import urllib.request
from bs4 import BeautifulSoup

link = "http://www.imdb.com/search/title?release_date=2016"
for i in range(1,200):
    print("page: " + str(i) + "link: " + link)
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, "html.parser")
#k = soup.find_all("h3", class_="lister-item-header")
    m = soup.select(".lister-item-header > a")
    for j in m:
        movie_country_list = list()
        movie_language_list = list()
        movie_genres_list = list()
        movie_title = j.get_text()
        link_movie = "http://www.imdb.com"+j.get("href")
        movie_id = re.sub(r'\D',"", link_movie)
        print(movie_title+" "+movie_id)
        page_movie = urllib.request.urlopen(link_movie)
        soup_movie = BeautifulSoup(page_movie, "html.parser")
        movie_rating_score = soup_movie.find(itemprop = "ratingValue").get_text()
        movie_description = soup_movie.select_one(".summary_text").get_text(strip=True)
        movie_temp = soup_movie.select(".txt-block a")
        movie_temp2 = soup_movie.select(".canwrap a")
        #movie_temp2 = movie_temp2.get("href")
        for m in movie_temp2:
            if "genre" in m.get("href"):
                movie_genres_list.append(m.get_text(strip=True))
        ''' if(m.a != None):
                movie_genres_list.append(m.a.get_text(strip = True))'''
        for k in movie_temp:
            temp1 = k.get("href")
            if "country" in temp1:
                movie_country_list.append(k.get_text(strip = True))
            elif "language" in temp1:
                movie_language_list.append(k.get_text(strip = True))
        movie_runtime  = soup_movie.select("time")
        print(movie_runtime[0].get_text(strip=True))
            #elif "genres" in temp1:
            #    movie_genres_list.append(k.get_text())
        #print(movie_country_list)
        #print(movie_language_list)
        print(movie_genres_list)

    link = "http://www.imdb.com/search/title"+soup.select_one(".next-page").get("href")
'''for i in m:
    print(i.a.get_text())'''
#j = 1
'''for i in k:
    #print(str(j) + ". " + i.a.get_text())
    #print(str(j) + ". " + i.a.get_text()+": http://www.imdb.com"+i.a.get("href"))
    j += 1'''
