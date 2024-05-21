from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

blog_objects = []
response = requests.get(blog_url)
data = response.json()

for post in data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_objects.append(post_obj)



@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_objects)

@app.route('/post/<int:index>')
def show_post(index):
    blog_post_id = None
    for blog_post in blog_objects:
        if blog_post.post_id == index:
            blog_post_id = blog_post
    return render_template("post.html", post=blog_post_id)

if __name__ == "__main__":
    app.run(debug=True)
