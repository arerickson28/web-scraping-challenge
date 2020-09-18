import scrape_mars
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

mongo = PyMongo(app)

# mongo = PyMongo(app, uri=“mongodb://localhost:27017/mars_app”)


@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars_data)



@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

    mars_info = scrape_mars.scrape()

    mars.update({}, mars_info, upsert = True)

    return redirect("/", code = 302)
    # return "scraping successful"



if __name__ == "__main__":
    app.run(debug=True)