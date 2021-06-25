#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[3]:


from bs4 import BeautifulSoup
import requests
import re


# In[4]:


Page = requests.get("https://bookpage.com/reviews")
Page


# In[5]:


Page.content


# In[6]:


soup = BeautifulSoup(Page.content)
soup


# In[29]:


first_title=soup.find('div',class_="flex-article-content")
first_title


# In[32]:


first_title.text


# In[31]:


first_author=soup.find('div',class_="flex-article-content")
first_author


# In[33]:


first_author.text


# In[34]:


first_genre=soup.find('div',class_="genre-links hidden-phone")
first_genre


# In[52]:


first_genre.text


# In[51]:


first_review=soup.find('a',class_="reviews?book_genre=fiction&amp;page=1")
first_review


# In[50]:


first_review.text


# In[72]:


titles=soup.find_all('div',class_="article-list-left")
titles


# In[76]:


book_titles=[]
for i in titles:
    book_titles.append (i.text)
book_titles


# In[77]:


book_titles=[]
for i in titles:
    book_titles.append(i.text.replace("\n",''))
book_titles


# In[78]:


len(book_titles)


# In[15]:


authors=soup.find_all('div',class_="bp-block article-info")
authors


# In[16]:


book_authors=[]
for i in authors:
    book_authors.append (i.text)
book_authors


# In[18]:


book_authors=[]
for i in authors:
    book_authors.append (i.text.replace("\n",''))
book_authors   


# In[19]:


len(book_authors)


# In[28]:


genres=soup.find.all('div',class_="genre-links hidden-phone")
genres


# In[112]:


book_genres=[]
for i in titles:
    book_genres.append(i.text.strip())
book_genres


# In[113]:


book_genres=[]
for i in titles:
    book_genres.append(i.text.replace("\n",''))
book_genres


# In[45]:


reviews=soup.find.all('a',class_="reviews?book_genre=nonfiction&amp;page=1")
reviews


# review_titles=
# for i in titles:
#     review_titles.append(i.text)
# review_titles

# In[38]:


book_reviews=[]
for i in titles:
    book_reviews.append(i.text.replace("\n",''))
book_reviews


# In[37]:


import pandas as pd
books=pd.DataFrame({})
books['title']=book_titles
books['author']=book_authors
books['genre']=book_genres
books['review']=book_reviews


# In[53]:


books


# In[ ]:




