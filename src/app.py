from flask import Flask, abort, render_template

from utils.post_manager import PostsManager

app = Flask(__name__)
posts_manager = PostsManager()


@app.route("/")
@app.route("/home")
def home():
    """Renders the home page with all blog posts."""
    posts = posts_manager.get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/tag/<tag>')
def posts_by_tag(tag):
    posts = posts_manager.get_posts_by_tag(tag)
    return render_template('tag.html', posts=posts, tag=tag)


@app.route('/post/<post_id>')
def post(post_id):
    post = posts_manager.get_post_by_id(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
