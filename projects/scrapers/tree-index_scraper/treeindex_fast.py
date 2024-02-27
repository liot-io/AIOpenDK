import os
from typing import List
import html2text
from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
import re

def download_page(url: str, base_dir: str, visited_urls: set) -> None:
    """Download the HTML content from a page and recursively download its subpages."""
    # Extract a filename from the URL
    parsed_url = urlparse(url)
    page_url_without_fragment = parsed_url._replace(fragment='').geturl()  # Remove fragment identifier
    if page_url_without_fragment in visited_urls:
        return

    session = HTMLSession()
    response = session.get(page_url_without_fragment, timeout=30)

    # Check if the content type is HTML
    content_type = response.headers.get('content-type', '')
    if 'text/html' not in content_type:
        print(f"Skipping {url} as it is not an HTML page")
        return

    # Render the page, which will execute JavaScript
    response.html.render(timeout=60)  # Increased timeout to 60 seconds

    # Extract filename
    path_segments = parsed_url.path.strip("/").split("/")
    filename = path_segments[-1] if path_segments else parsed_url.netloc
    filename = filename.split(".")[0] + ".md"

    # Write the markdown content to a file
    dir_path = os.path.join(base_dir, parsed_url.netloc, *path_segments)
    os.makedirs(dir_path, exist_ok=True)

    # Convert the rendered HTML content to markdown
    h = html2text.HTML2Text()
    markdown_content = h.handle(response.html.raw_html.decode("utf-8"))

    with open(os.path.join(dir_path, filename), "w", encoding="utf-8") as f:
        f.write(markdown_content)

    visited_urls.add(page_url_without_fragment)

    # Extract URLs of subpages
    subpages = re.findall(r'href=["\'](.*?)["\']', response.text)
    absolute_urls = [urljoin(url, subpage) for subpage in subpages if subpage.startswith(url)]
    
    # Recursively download subpages
    for subpage_url in absolute_urls:
        download_page(subpage_url, base_dir, visited_urls)


if __name__ == "__main__":
    PAGES = [
        "https://example.dk",
    ]
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
    os.makedirs(base_dir, exist_ok=True)
    visited_urls = set()
    
    for page_url in PAGES:
        download_page(page_url, base_dir, visited_urls)

    print("All pages have successfully been scraped and saved hierarchically.")
