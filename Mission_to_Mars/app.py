from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)
#use flask py mongo to set up the connection to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    #access information from mongodb
    mars_data = mongo.db.marsData.find_one()
    return render_template('index.html', mars=mars_data)

@app.route("/scrape")
def scrape():
    #reference database collection on MongoDB
    marsTable = mongo.db.marsData

    #drop the table if it exists
    mongo.db.marsData.drop()

    # test call to scrape mars script
    mars_data = scrape_mars.scrape_all()

    #load dictionary into mongodb
    marsTable.insert_one(mars_data)
    
    #go back to index route
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
