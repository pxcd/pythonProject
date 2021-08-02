from flask import Flask, render_template
import random
from datetime import date
import requests
app = Flask(__name__)


@app.route('/')
def home():
    current_year = date.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year, name="pow")

@app.route('/guess/<string:name>')
def guess(name):
    name = name.title()
    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender = gender_response.json()["gender"]
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age = age_response.json()["age"]
    return render_template("guess.html", n=name, g=gender, a=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c4d50ae6bc52af72fb0b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)

