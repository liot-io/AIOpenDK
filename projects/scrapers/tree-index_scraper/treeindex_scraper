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
    if path_segments:
        filename = path_segments[-1]
    else:
        filename = parsed_url.netloc  # Use domain name as filename if no path segments
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

    visited_urls = set()  # Track visited URLs to avoid duplicate downloads

    for page_url in pages:
        download_page(page_url, base_dir, visited_urls)

    print("All pages have successfully been scraped and saved hierarchically.")

    return base_dir

def download_page(page_url: str, base_dir: str, visited_urls: set) -> None:
    """Download the HTML content from a page and recursively download its subpages."""
    parsed_url = urlparse(page_url)
    page_url_without_fragment = parsed_url._replace(fragment='').geturl()  # Remove fragment identifier
    if page_url_without_fragment in visited_urls:
        return

    session = HTMLSession()
    response = session.get(page_url_without_fragment, timeout=30)

    dir_path = os.path.join(base_dir, parsed_url.netloc, *parsed_url.path.strip("/").split("/"))
    os.makedirs(dir_path, exist_ok=True)

    download_and_save_in_markdown(page_url_without_fragment, dir_path)
    visited_urls.add(page_url_without_fragment)

    subpages = extract_urls_from_html(response.text, page_url_without_fragment)
    for subpage_url in subpages:
        if subpage_url.startswith(page_url_without_fragment):
            download_page(subpage_url, base_dir, visited_urls)

if __name__ == "__main__":
    PAGES = [
        "https://Example.dk",
    ]
    download(PAGES)
