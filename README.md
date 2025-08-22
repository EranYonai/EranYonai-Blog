# Eranyonai's Flask Blog

This is a sleek, modern personal blog built with the Flask web framework. It features a clean user interface with both light and dark themes.

## Project Setup

This project uses `uv` for package management, which is a fast, modern alternative to `pip` and `venv`.

### 1. Install uv

If you don't have `uv` installed, you can install it with the following command:

**macOS / Linux:**
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

Windows:

powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"

For other installation methods, please refer to the official uv documentation.
```

### Sync dependencies, and run project
Navigate to root project, and just `uv sync && uv run src/app.py` to start the local server.

## Project Structure
.
├── app.py              # Main Flask application file
├── templates/
│   ├── base.html       # Base template with header, footer, and theme logic
│   ├── index.html      # Home page template (lists all posts)
│   └── post.html       # Single post page template
├── static/             # (Optional) For CSS, JS, and image files
├── pyproject.toml      # Project metadata and dependencies
└── README.md           # This file
