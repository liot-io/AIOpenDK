import os
import html2text
from requests_html import HTMLSession
from urllib.parse import urlparse

def extract_filename_from_url(url: str) -> str:
    """Extract the filename from the URL."""
    parsed_url = urlparse(url)
    filename = parsed_url.netloc  # Extract domain name from URL
    return filename + ".md"  # Add .md extension

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

def download_target_page(url: str) -> None:
    """Download the HTML content from the target page and save it as a markdown file."""
    # Create the content directory if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, "content")
    os.makedirs(dir_path, exist_ok=True)
    
    # Download and save the target page
    download_and_save_in_markdown(url, dir_path)
    print("Target page has been successfully downloaded!")

# Define the target page
TARGET_PAGES = [
    "https://Example.dk/",
]

if __name__ == "__main__":
    for target_page in TARGET_PAGES:
        download_target_page(target_page)
