import argparse
import threading
import time
import webbrowser
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


# move this to utils.py ->
def open_browser(url):
    """Opens the browser after a short delay to ensure the server is running."""
    time.sleep(1)  # Wait for the server to start
    webbrowser.open(url)

if __name__ == '__main__':
    # simple argparse to launch server.
    parser = argparse.ArgumentParser(description='Run the EranYonai-Blog Flask application')
    parser.add_argument('--launch-browser', action='store_true', default=False,
                       help='Automatically open the browser when starting the server')
    parser.add_argument('--host', default='127.0.0.1', 
                       help='Host to run the server on (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=5000, 
                       help='Port to run the server on (default: 5000)')
    parser.add_argument('--debug', action='store_true', default=True,
                       help='Run in debug mode (default: True)')
    parser.add_argument('--hot-reload', action='store_true', default=True,
                       help='Enable hot reload (auto-restart on file changes) (default: True)')
    
    args = parser.parse_args()
    
    if args.launch_browser:
        url = f"http://{args.host}:{args.port}"
        threading.Thread(target=open_browser, args=(url,), daemon=True).start()
    
    app.run(host=args.host, port=args.port, debug=args.debug)
