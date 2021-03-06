# Web Scraping - Mission to Mars

Built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

## Step 1 - Web Scraping using Python

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of the scraping and analysis tasks. 

* Scraped the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. 

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.



## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

* Stored the return value in Mongo as a Python dictionary.

![image](https://user-images.githubusercontent.com/90559756/163394000-e13be3c6-c4aa-42ca-9870-51ab37271f33.png)

* Created a root route `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and display all of the data in the appropriate HTML elements. 

![image](https://user-images.githubusercontent.com/90559756/163393746-ce5574e4-3b83-4fd8-875b-66bfd07feea6.png)


