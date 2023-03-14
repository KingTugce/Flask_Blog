from flask import Blueprint
from flask import render_template

from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

# localhost:5000/blog/
@posts.route('/')
def posts_list():
    return render_template('posts/posts.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('post/post_detail.html', post=post)
