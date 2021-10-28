#!/usr/bin/env python
# coding: utf-8

# # Header Print

# In[2]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
s=BeautifulSoup('en.wikipedia.org/wiki/Main_Page','html.parser')
print(s.headers)


# # IMDB Top 100 Movie

# In[3]:


import re 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
 
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
 
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]
 
votes = [b.attrs.get('data-value')
         for b in soup.select('td.ratingColumn strong')]
 
list = []
 
# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, 100):
     
    # Separating  movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "rating": ratings[index],
           }
    list.append(data)
    
    df = pd.DataFrame(list)
    print(df)
 
# printing movie details with its rating.
#for movie in list:
 #   print(movie['movie_title'], '('+movie['year'] +
  #        ') -',  movie['rating'])


# In[4]:


import re 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
 
movies = soup.select('td.titleColumn')

 
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]
 

 
# create a empty list for storing
# movie information
list = []

 
# Iterating over movies to extract
# each movie's details
for index in range(0, 100):
   
     
    # Separating  movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
           "rating": ratings[index],
          }
    list.append(data)
     
    df = pd.DataFrame(list)
print(df)
    


# # Top 100 Indian Movies in IMDB

# In[5]:


import re 
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
 
movies = soup.select('td.titleColumn')

 
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]
 

 
# create a empty list for storing
# movie information
list = []

 
# Iterating over movies to extract
# each movie's details
for index in range(0, 100):
   
     
    # Separating  movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
           "rating": ratings[index],
          }
    list.append(data)
     
    df = pd.DataFrame(list)
print(df)
    


# # Write a python program to scrape weather details for last 24 hours 

# In[40]:


import warnings
import re
url = 'https://en.tutiempo.net/delhi.html?data=last-24-hours'

response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
soup1=soup.find('div',class_='last24 thh')
#S=soup1.find_all("td")

#WC1=soup1.find('span',class_='thhip ico i0530 u303').text

for row in soup1.find_all('tr'):
    for col in row.find_all('td'):
        info= col.text
        print(info)
    print(' ')

#for report in soup1:
    
       # WC1=col.find('span',class_='thhip ico i0530 u303').text
  #  Temp=report.find('td',class_='t Temp').text
   # win=report.find('td',class_='wind').text
 #   Press=report.find('td',class_='prob').text
  #  Hum=report.find('td',class_='hr').text
    
      #  print(f'''
            #Hour:{hour}
            #Weather Condition:{col.find('span',class_='thhip ico i0530 u303').text}
            #Temeperature:{Temp}
            #Wind:{win}
            #Humidity:{Hum}
            #Pressure:{Press}
            #''')
#print(' ')


# # Write a python program to scrape mentioned details from ‘https://www.dineout.co.in/delhi-restaurants/buffet-special’ :

# In[46]:


import requests
import re
url = 'https://www.dineout.co.in/delhi-restaurants/buffet-special'

response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
#print(soup)
Restaurant=soup.find_all('div',class_='restnt-card restaurant')
 
    
for index in Restaurant:
    
    Name=index.find('div',class_='restnt-info cursor').a.text
    Location=index.find('div',class_='restnt-loc ellipsis').a.text
    Cuisine=index.find('span',class_='double-line-ellipsis').a.text
    Ratings=index.find('div',class_='restnt-rating rating-4 hide').text
   # Image=[b.attrs.get('src') for b in Restaurant.select('div.RestaurantImageClick img[data-gatype=RestaurantImageClick]')]
   
    #img=index.find('img')
    #Image=print(img['src']) 
    Image=img.attrs.get("data-src")                                                          

#ratings = [b.attrs.get('data-value')
            #for b in soup.select('td.posterColumn span[name=ir]')] 
#print(Name)
    
 #   data={
    #"Restaurant Name":Name[index]}
    
   # list.append(data)
    #print(list)
    
    print(f'''
       Name:{Name}
       Location:{Location}
       Cuisine:{Cuisine}
       Image:{Image}''')


# # To display Top 10 ODI men batsman rankings

# In[49]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url ='https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
Team1=soup.find('div',class_='rankings-block__banner--player-info')
Team=soup.find('div',class_='rankings-block__container')
Player_1=Team1.find('div',class_='rankings-block__banner--name').text
Team_1=Team1.find('span',class_='rankings-block__banner--nation').text
Rank_1=Team1.find('div',class_='rankings-block__banner--rating').text

Information_1={"Player Name":Player_1,"Team":Team_1,"Rating":Rank_1}
print(Information_1)

list=[]

for index in range(0,9):

    Player=Team.find_all('td',class_='table-body__cell name')
    Player1=Player[index].a.get_text()
    TeamName=Team.find_all('span',class_='table-body__logo-text')
    Team1=TeamName[index].get_text()
    #Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    Rating1=Rating[index].get_text()
    
    
    Information={"Player Name":Player1,"Team":Team1,"Rating":Rating1}
    #list.append(Information)
    
    #df = pd.DataFrame(list)
    #print(df)
    print(Information)
    


# # Top 10 ODI bowlers along with the records of their team andrating.

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url ='https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
#Team1=soup.find('div',class_='rankings-block__banner--player-info')
#TeamB=soup.find_all('tr',class_='table-body',data-cricket-role='bowling')
TeamB=soup.find(attrs={'data-cricket-role':'bowling'})

Player_1=TeamB.find('div',class_='rankings-block__banner--name').text
Team_1=TeamB.find('span',class_='rankings-block__banner--nation').text
Rank_1=TeamB.find('div',class_='rankings-block__banner--rating').text

Information_1={"Player Name":Player_1,"Team":Team_1,"Rating":Rank_1}
print(Information_1)

print(Team_1)


list=[]

for index in range(0,9):

    Bowler=TeamB.find_all('td',class_='table-body__cell name')
    Bowler1=Bowler[index].a.get_text()
    TeamNameB=TeamB.find_all('span',class_='table-body__logo-text')
    Team1B=TeamNameB[index].get_text()
    #Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    RatingB=TeamB.find_all('td',class_='table-body__cell u-text-right rating')
    Rating1B=RatingB[index].get_text()
    
    
    InformationB={"Player Name":Bowler1,"Team":Team1B,"Rating":Rating1B}
    #list.append(Information)
    
    #df = pd.DataFrame(list)
    #print(df)
    print(InformationB)
    
    


# # Top 10 Women Batsman

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url ='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
Team1=soup.find('div',class_='rankings-block__banner--player-info')
Team=soup.find('div',class_='rankings-block__container')
Player_1=Team1.find('div',class_='rankings-block__banner--name').text
Team_1=Team1.find('span',class_='rankings-block__banner--nation').text
Rank_1=Team1.find('div',class_='rankings-block__banner--rating').text

Information_1={"Player Name":Player_1,"Team":Team_1,"Rating":Rank_1}
print(Information_1)

list=[]

for index in range(0,9):

    Player=Team.find_all('td',class_='table-body__cell name')
    Player1=Player[index].a.get_text()
    TeamName=Team.find_all('span',class_='table-body__logo-text')
    Team1=TeamName[index].get_text()
    #Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    Rating1=Rating[index].get_text()
    
    
    Information={"Player Name":Player1,"Team":Team1,"Rating":Rating1}
    #list.append(Information)
    
    #df = pd.DataFrame(list)
    #print(df)
    print(Information)


# # Top 10 ODI Women All rounders

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url ='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
#Team1=soup.find('div',class_='rankings-block__banner--player-info')
#Team=soup.find('div',class_='rankings-block__container')
TeamB=soup.find(attrs={'data-cricket-role':'all_round'})

Player_1=TeamB.find('div',class_='rankings-block__banner--name').text

Team_1=TeamB.find('div',class_='rankings-block__banner--nationality').text
Rank_1=TeamB.find('div',class_='rankings-block__banner--rating').text

Information_1={"Player Name":Player_1,"Team":Team_1,"Rating":Rank_1}
print(Information_1)

list=[]

for index in range(0,9):

    Player=TeamB.find_all('td',class_='table-body__cell name')
    Player1=Player[index].a.get_text()
    TeamName=TeamB.find_all('span',class_='table-body__logo-text')
    Team1=TeamName[index].get_text()
    #Rating=Team.find_all('td',class_='table-body__cell u-text-right rating')
    Rating=TeamB.find_all('td',class_='table-body__cell u-text-right rating')
    Rating1=Rating[index].get_text()
    
    
    Information={"Player Name":Player1,"Team":Team1,"Rating":Rating1}
    #list.append(Information)
    
    #df = pd.DataFrame(list)
    #print(df)
    print(Information)


# # Top 10 Women Team rating in ODI
