# Eran Yonai's Blog

This is a sleek, modern personal blog built with Flask framework. It features an intelligent markdown-to-website conversion system that automatically transforms markdown files into beautiful web pages, complete with frontmatter parsing, tag organization, and dynamic post management.

## 🚀 Live

The blog is deployed and accessible at: **[https://eranyonaiblog.onrender.com/](https://eranyonaiblog.onrender.com/)**

> **⚠️ Disclaimer:** This site is hosted on Render's free tier. Free instances spin down with inactivity, which can delay requests by 50+ seconds on first load. Additionally, the behavior and availability may change over time as the hosting environment evolves.

## Features

- 📝 **Markdown Posts** - Write posts in Markdown with frontmatter metadata
- 🎨 **Dark/Light Theme** - Toggle between themes with system preference detection
- 🏷️ **Tag System** - Organize and filter posts by tags
- 📱 **Responsive Design** - Mobile-friendly interface
- 🔍 **Syntax Highlighting** - Code blocks with proper highlighting
- ⚡ **Fast Loading** - Cached post loading with automatic refresh detection

## Project Setup

This project uses `uv` for package management, which is a fast, modern alternative to `pip` and `venv`.

### 1. Install uv

If you don't have `uv` installed, you can install it with the following command:

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For other installation methods, please refer to the official uv documentation.

### 2. Sync dependencies and run project

Navigate to root project, and run:
```bash
uv sync && uv run src/app.py
```

### Available Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--launch-browser` | flag | False | Automatically open the browser when starting the server |
| `--host` | string | 127.0.0.1 | Host to run the server on |
| `--port` | integer | 5000 | Port to run the server on |
| `--debug` | flag | True | Run in debug mode |
| `--hot-reload` | flag | True | Enable hot reload (auto-restart on file changes) |
| `--help` | flag | False | Show help message and exit |

## Project Structure

```
.
├── src/
│   ├── app.py                  # Main Flask application file
│   ├── templates/
│   │   ├── base.html          # Base template with header, footer, and theme logic
│   │   ├── index.html         # Home page template (lists all posts)
│   │   ├── post.html          # Single post page template
│   │   └── tag.html           # Tag-filtered posts page
│   ├── static/
│   │   └── assets/
│   ├── utils/
│   │   ├── __init__.py        # Makes utils a Python package
│   │   └── post_manager.py    # Post management system
│   └── posts/                 # Markdown blog posts directory
├── pyproject.toml             # Project metadata and dependencies
└── README.md                  # This file
```

## Writing Posts

Create new blog posts as Markdown files in the `src/posts/` directory. Each post should include frontmatter metadata:

```markdown
---
title: "Your Post Title"
author: "Your Name"
date: "15-01-2025"
tags: ["tag1", "tag2"]
excerpt: "Brief description of your post"
---

# Your Post Content

Write your post content in Markdown here...
```

### Frontmatter Fields

- **title**: The post title (required)
- **author**: Post author name
- **date**: Publication date in DD-MM-YYYY format
- **tags**: Array of tags for categorization
- **excerpt**: Brief post description (optional - auto-generated if not provided)

## Development

The blog includes:
- Automatic post caching and refresh detection
- Hot-reloading in development mode
- Responsive design with Tailwind CSS
- Dark/light theme with localStorage persistence
- Syntax highlighting for code blocks

To add a new post, simply create a new `.md` file in `src/posts/` with proper frontmatter, and it will automatically appear on your blog!
