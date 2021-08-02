from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/c4d50ae6bc52af72fb0b"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html", posts=all_posts, blog_id=id)


if __name__ == "__main__":
    app.run(debug=True)


