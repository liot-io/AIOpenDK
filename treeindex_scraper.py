import os
from typing import List
import html2text
from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
import re

def extract_filename_from_url(url: str) -> str:
    """Extract the filename from the URL."""
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.strip("/").split("/")
    filename = path_segments[-1] if path_segments[-1] else path_segments[-2]
    filename = filename.split(".")[0]  # Remove extension if present
    return filename + ".md"

def extract_urls_from_html(html_content: str, base_url: str) -> List[str]:
    """Extract URLs from HTML content."""
    urls = re.findall(r'href=["\'](.*?)["\']', html_content)
    absolute_urls = [urljoin(base_url, url) for url in urls]
    return absolute_urls

def download_and_save_in_markdown(url: str, base_dir: str) -> None:
    """Download the HTML content from the web page and save it as a markdown file."""
    # Extract a filename from the URL
    filename = extract_filename_from_url(url)
    print(f"Downloading {url} into {filename}...")

    session = HTMLSession()
    response = session.get(url, timeout=30)

    # Check if the content type is HTML
    content_type = response.headers.get('content-type', '')
    if 'text/html' not in content_type:
        print(f"Skipping {url} as it is not an HTML page")
        return

    # Render the page, which will execute JavaScript
    response.html.render(timeout=60)  # Increased timeout to 60 seconds

    # Convert the rendered HTML content to markdown
    h = html2text.HTML2Text()
    markdown_content = h.handle(response.html.raw_html.decode("utf-8"))

    # Write the markdown content to a file
    filename = os.path.join(base_dir, filename)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)

def download(pages: List[str]) -> str:
    """Download the HTML content from the pages and save them as markdown files."""
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
    os.makedirs(base_dir, exist_ok=True)
    
    for page_url in pages:
        session = HTMLSession()
        response = session.get(page_url, timeout=30)
        dir_path = os.path.join(base_dir, urlparse(page_url).netloc, *urlparse(page_url).path.strip("/").split("/"))
        os.makedirs(dir_path, exist_ok=True)
        download_and_save_in_markdown(page_url, dir_path)
        
        subpages = extract_urls_from_html(response.text, page_url)
        for subpage_url in subpages:
            if subpage_url.startswith(page_url):
                sub_dir_path = os.path.join(base_dir, urlparse(subpage_url).netloc, *urlparse(subpage_url).path.strip("/").split("/"))
                os.makedirs(sub_dir_path, exist_ok=True)
                download_and_save_in_markdown(subpage_url, sub_dir_path)

    return base_dir

PAGES = [
    "https://foedevarestyrelsen.dk/",
]

if __name__ == "__main__":
    download(PAGES)
