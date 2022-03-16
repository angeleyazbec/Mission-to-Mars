#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

#scrape all function
def scrape_all():
    #set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #goal is to return a json containing all necessary data to be loaded into MongoDB

    #get information form the news page
    one_article, article_p = scrape_news(browser)

    #building a dictionary using the information from the scrapes
    marsData ={
        "newsTitle" : one_article,
        "newsParagraph" : article_p,
        "featuredImage" : scrape_featured_image(browser),
        "facts" : scrape_facts_page(browser),
        "hemispheres" : scrape_hemispheres (browser),
        "lastUpdated" : dt.datetime.now()
    }

    #stop webdriver
    browser.quit()

    #display data
    return marsData

#scrape the mars news page
def scrape_news(browser):
    #go to the Mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    soup = BeautifulSoup(browser.html, 'html.parser')
    recent_article = soup.select_one("div.list_text")
    #grabs the news title
    one_article=recent_article.find("div", class_="content_title").text
    #grads the corresponding paragraph
    article_p = recent_article.find("div", class_ ="article_teaser_body").text

    #return the news title and paragraph
    return one_article, article_p 


#scrape through the featured image page
def scrape_featured_image(browser):
    #visit the URL
    image_url = 'https://spaceimages-mars.com'
    browser.visit(image_url)
    html = browser.html

    #parsing the results with soup
    picture_soup = BeautifulSoup(html, 'html.parser')
    picture_soup.title.text

    #image url
    image_url2 = picture_soup.find("img",class_="headerimage fade-in")["src"]
    #full image url
    featured_image_url = image_url + image_url2

    return featured_image_url

#scrape through the facts page
def scrape_facts_page(browser):
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)

    #prase the resulting html with soup
    html = browser.html
    fact_soup = BeautifulSoup(html, 'html.parser')

    #find the facts location
    factsLocaton = fact_soup.find('div', class_='diagram mt-4')
    factTable = factsLocaton.find('table')

    #create an empty string
    facts = ""

    #add the text to the empty string then return
    facts += str(factTable)

    return facts

#scrape through the hemispheres page
def scrape_hemispheres(browser):
    #base url
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    #creating list of image urls
    hemisphere_image_urls = []

    #set up the loop
    for x in range(4):
        #loops through all 4 pages
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
        hemisphere_image_urls.append(mars_dictionary)
        
        browser.back()

    #return the hemisphere urls with the titles
    return hemisphere_image_urls

#set up as flask app
if __name__ == "__main__":
    print(scrape_all())