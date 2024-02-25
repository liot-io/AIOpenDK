import os
from typing import List
import html2text
from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
import re

def extract_filename_from_url(url: str) -> str:
    """Extract the filename from the URL."""
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split("/")
    filename = path_segments[-1] if path_segments[-1] else path_segments[-2]
    filename = filename.split(".")[0]  # Remove extension if present
    return filename + ".md"

def extract_urls_from_html(html_content: str, base_url: str) -> List[str]:
    """Extract URLs from HTML content."""
    urls = re.findall(r'href=["\'](.*?)["\']', html_content)
    absolute_urls = [urljoin(base_url, url) for url in urls]
    return absolute_urls

def download_and_save_in_markdown(url: str, dir_path: str) -> None:
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
    filename = os.path.join(dir_path, filename)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)

def download(pages: List[str]) -> str:
    """Download the HTML content from the pages and save them as markdown files."""
    # Create the content/foedevarestyrelsen directory if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, "content", "foedevarestyrelsen")
    os.makedirs(dir_path, exist_ok=True)
    
    processed_urls = set()  # To track processed URLs and avoid duplicates
    while pages:
        current_url = pages.pop(0)
        if current_url not in processed_urls:
            download_and_save_in_markdown(current_url, dir_path)
            processed_urls.add(current_url)
            
            session = HTMLSession()
            response = session.get(current_url, timeout=30)
            subpages = extract_urls_from_html(response.text, current_url)
            
            # Extracting subpages within the root URL
            subpages = [link for link in subpages if link.startswith(current_url) and not link.endswith(('.ico', '.png', '.jpg', '.jpeg', '.gif'))]
            pages.extend(subpages)
    
    return dir_path

PAGES = [
    "https://foedevarestyrelsen.dk/",
]

if __name__ == "__main__":
    download(PAGES)
