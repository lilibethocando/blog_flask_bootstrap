from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/39cc79459d330a231db3"

response = requests.get(blog_url)
posts = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")






if __name__ == "__main__":
    app.run(debug=True)
