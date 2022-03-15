#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
import pandas as pd
import certifi

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def scrape_all():
    


    #creating path for scraping
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars = {}
    # ### Scraping NASA Mars News




    #designating url to visit
    url = 'https://redplanetscience.com/'
    browser.visit(url)


   


    #obtaining the results from our research
    soup = BeautifulSoup(browser.html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


   


    #Collect the latest news article
    recent_article = soup.select_one("div.list_text")
    one_article=recent_article.find("div", class_="content_title").text
    one_article
    mars["title"] = one_article

   

    article_p = recent_article.find("div", class_ ="article_teaser_body").text
    #print(article_p)
    mars["paragraph"] = article_p

    # ### Scraping for JPL Mars Space Images

   


    #designating url to visit
    image_url = 'https://spaceimages-mars.com'
    browser.visit(image_url)
    html = browser.html

    #creating html object
    picture_soup = BeautifulSoup(html, 'html.parser')
    picture_soup.title.text


   


    #find image url for the featured image
    image_url2 = picture_soup.find("img",class_="headerimage fade-in")["src"]
    
    

    


    #feature_image_url assignment
    featured_image_url = image_url + image_url2
    
    mars["featured_image"] = featured_image_url

    # ### Scraping for Mars Facts

  


    #designating url to visit
    url = 'https://galaxyfacts-mars.com'


    


    #reading the table to be scraped
    tables = pd.read_html(url)
    


    


    #converting the table as a Pandas dataframe
    mars_df=tables[0]
    

    
    


    #renaming the columns
    mars_df.columns=['Description', 'Mars', 'Earth']

    #reseting the index
    mars_df2 = mars_df.reset_index(drop=True)
    


   


    #dropping the first row
    mars_clean = mars_df2.drop([0])
    mars_clean.head()


    # In[99]:


    #converting the dataframe to an HTML file
    mars_html_table = mars_clean.to_html()

    #cleaning the HTML table
    mars_html_table.replace('\n', " ")


    


    #saving HTML table to a file
    mars_clean.to_html('mars_table.html')

    mars["fact"]=mars_html_table
    # ### Scraping Information for Mars Hemisphere

    


    #designating url to visit
    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)
    html2 = browser.html


    


    #find image url for the Valles Marineris Hemipshere
    image_results = browser.find_by_css('a.product-item img')
    image_results
    hemisphere_image_url = []

    #looping through results to obtain images
    for x in range(len(image_results)):
        #scrape the title
        browser.find_by_css('a.product-item img')[x].click()
        title= browser.find_by_css('h2.title').text
        
        #scrape the image
        element=browser.find_by_text('Sample').first
        image_url= element['href'] 

        #appending results to mars_hemi dictionary
        mars_dictionary= {
            'title': title,
            'img_url': image_url,
        }
        hemisphere_image_url.append(mars_dictionary)
        
        browser.back()
        
    #printing the dictionary
    #print(hemisphere_image_url)
    mars["hemispheres"] = hemisphere_image_url
    return mars
if __name__=="__main__":
    print(scrape_all())

    




