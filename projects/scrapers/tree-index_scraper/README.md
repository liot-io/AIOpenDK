This Python script is designed to scrape HTML content from web pages and save them as Markdown files. It uses the requests_html library to fetch HTML content from URLs and the html2text library to convert HTML to Markdown format.

Features
Scraping HTML Content: The script extracts HTML content from web pages and converts it into Markdown format.
Downloading Subpages: It recursively downloads subpages linked from the main page.
Handling Fragment Identifiers: The script handles URLs with fragment identifiers (#) by removing them before processing the URL.
Avoiding Duplicate Downloads: It tracks visited URLs to avoid duplicate downloads of the same page.
Organized File Structure: The downloaded Markdown files are organized hierarchically based on the URL structure.
How to Use
Install Dependencies: Ensure you have Python installed on your system. Install the required dependencies using pip:

    ´´´pip install requests-html html2text
    ´´´
    
Clone the Repository: Clone this repository to your local machine.

Run the Script: Modify the PAGES list in the script to include the URLs you want to scrape. Then, run the script using Python:

Copy code
python web_scraper.py
Check Output: The script will create a content directory in the same location as the script. Inside the content directory, you will find the downloaded Markdown files organized based on the URL structure.

Code Structure
extract_filename_from_url(url: str) -> str: Extracts a filename from the URL to use as the name for the Markdown file.
extract_urls_from_html(html_content: str, base_url: str) -> List[str]: Extracts URLs from HTML content.
download_and_save_in_markdown(url: str, base_dir: str) -> None: Downloads HTML content from a URL, converts it to Markdown, and saves it as a file.
download(pages: List[str]) -> str: Downloads HTML content from a list of pages and their subpages, saving them as Markdown files.
download_page(page_url: str, base_dir: str, visited_urls: set) -> None: Downloads HTML content from a single page and its subpages recursively.
Example
Here's an example of how to use the script to scrape a website:

python
Copy code
PAGES = [
    "https://Example.dk",
    "https://Example.dk/about",
    "https://Example.dk/contact",
]
download(PAGES)
This will download the main pages (Example.dk, Example.dk/about, Example.dk/contact) and all their subpages, saving them as Markdown files in the content directory.
