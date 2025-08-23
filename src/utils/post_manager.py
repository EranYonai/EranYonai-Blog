import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import frontmatter
import markdown
from dateutil import parser as date_parser

# TODO: exception handling.
BASE_DIR = Path(__file__).parent.parent

class Post:
    def __init__(self, filename: str, metadata: dict, content: str):
        self.filename = filename
        self.metadata = metadata
        self.content = content
        self.html_content = markdown.markdown(content, extensions=["codehilite", "fenced_code"])

    @property
    def id(self) -> str:
        """Generate a URL-friendly ID from filename"""
        return os.path.splitext(self.filename)[0]

    @property
    def title(self) -> str:
        return self.metadata.get("title", "Untitled")

    @property
    def author(self) -> str:
        return self.metadata.get("author", "Unknown")

    @property
    def date_posted(self) -> str:
        date_str = self.metadata.get("date", "")
        if date_str:
            try:
                date_obj = date_parser.parse(date_str)
                return date_obj.strftime("%B %d, %Y")
            except:
                return date_str
        return "Unknown"

    @property
    def date_obj(self) -> datetime:
        """Return datetime object for sorting"""
        date_str = self.metadata.get("date", "")
        if date_str:
            try:
                return date_parser.parse(date_str)
            except:
                pass
        return datetime.min

    @property
    def tags(self) -> List[str]:
        return self.metadata.get("tags", [])

    @property
    def excerpt(self) -> str:
        excerpt = self.metadata.get("excerpt", "")
        if excerpt:
            return excerpt
        # Generate excerpt from content (first 150 chars)
        return self.content[:150] + "..." if len(self.content) > 150 else self.content


class PostsManager:
    def __init__(self, posts_directory: str = None):
        if posts_directory is None:
            # Default to posts directory relative to this file's parent directory
            self.posts_directory = BASE_DIR / "posts"
        else:
            self.posts_directory = Path(posts_directory)
        
        self._posts_cache = None
        self._last_modified = None

    def _needs_refresh(self) -> bool:
        """Check if posts directory has been modified since last cache"""
        if not self.posts_directory.exists():
            return False

        try:
            md_files = list(self.posts_directory.glob("*.md"))
            if not md_files:
                return True
                
            current_modified = max(
                file.stat().st_mtime for file in md_files
            )
            return self._last_modified != current_modified
        except (ValueError, OSError):
            return True

    def _load_posts(self) -> List[Post]:
        """Load all markdown posts from the posts directory"""
        posts = []

        if not self.posts_directory.exists():
            print(f"Posts directory {self.posts_directory} does not exist")
            return posts

        for filepath in self.posts_directory.glob("*.md"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    post_data = frontmatter.load(f)

                post = Post(filename=filepath.name, metadata=post_data.metadata, content=post_data.content)
                posts.append(post)

            except Exception as e:
                print(f"Error loading post {filepath.name}: {e}")
                continue

        # Sort posts by date (newest first)
        posts.sort(key=lambda p: p.date_obj, reverse=True)

        # Update cache
        self._posts_cache = posts
        try:
            md_files = list(self.posts_directory.glob("*.md"))
            if md_files:
                self._last_modified = max(
                    file.stat().st_mtime for file in md_files
                )
            else:
                self._last_modified = datetime.now().timestamp()
        except (ValueError, OSError):
            self._last_modified = datetime.now().timestamp()

        return posts

    def get_all_posts(self) -> List[Post]:
        """Get all posts, using cache if available and fresh"""
        if self._posts_cache is None or self._needs_refresh():
            return self._load_posts()
        return self._posts_cache

    def get_post_by_id(self, post_id: str) -> Optional[Post]:
        """Get a specific post by its ID"""
        posts = self.get_all_posts()
        for post in posts:
            if post.id == post_id:
                return post
        return None

    def get_posts_by_tag(self, tag: str) -> List[Post]:
        """Get all posts with a specific tag"""
        posts = self.get_all_posts()
        return [post for post in posts if tag.lower() in [t.lower() for t in post.tags]]
