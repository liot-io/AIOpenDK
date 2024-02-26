# AIOpenDK - simple webscraper services


# Web Scraper for Generating Markdown Files from Web Pages

This Python script allows you to scrape web pages from a specified domain, download their HTML content, and save them as Markdown files. It includes functionalities to handle dependencies, avoid duplicates, and filter out non-HTML content.

## Installation

1. **Python**: Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the script from the repository where it's hosted.

3. **Install Dependencies**: Install the required dependencies using pip. Run the following command in your terminal:

   ```bash
   pip install requests-html html2text

# Usage

## How to Use
Clone this Repository: Clone this repository to your local machine using the following command:

   ``bash
Copy code
git clone https://github.com/liot-io/AIOpenDK.git

Execute the Python Script: Execute the Python script with the following command:

   ```bash
Copy code
python treeindex_scraper.py

- Set Pages: Define the URLs of the pages you want to scrape in the PAGES list. You can specify multiple URLs.

- Run the Script: Execute the script by running it in your terminal or IDE.

- Output: The script will create a directory named content in the same location as the script. Inside the content directory, it will create a subdirectory named after the domain being scraped (e.g., example). The Markdown files will be saved in this directory.

# Code Explanation
## Imported Libraries

The script imports necessary libraries such as os, html2text, HTMLSession from requests_html, urlparse, re, etc.

## Function Definitions
extract_filename_from_url(url: str) -> str: Extracts the filename from the URL and saves it as a .md file.

extract_urls_from_html(html_content: str, base_url: str) -> List[str]: Extracts URLs from HTML content.

download_and_save_in_markdown(url: str, dir_path: str) -> None: Downloads HTML content from a webpage, converts it to Markdown, and saves it.

download(pages: List[str]) -> str: Downloads HTML content from the specified pages, saves them as Markdown files, and handles subpages within the root URL.

## Execution
The script checks if it's being run as the main program (if __name__ == "__main__":), then calls the download function with the specified PAGES.

## Handling Duplicates
The script uses a set named processed_urls to track processed URLs and avoid duplicates. Before processing a URL, it checks if it's already present in the set. If not, it adds the URL to the set and proceeds with processing. This ensures that each URL is processed only once.

# Filtering Non-HTML Content
The script checks the content type of the response to ensure that it's HTML before proceeding with rendering and conversion to Markdown. If the content type is not HTML, it skips processing that URL.

# Dependencies
- requests-html: --> Used for making HTTP requests and rendering JavaScript.
- html2text: --> Used for converting HTML content to Markdown format.
- 
Example
python
Copy code
PAGES = [
    "https://example.dk/",
]
Replace "https://example.dk/" with the URLs of the pages you want to scrape.

License
This project is licensed under the MIT License - see the LICENSE file for details.
----------------------------------


# AIOpenDK - TreeIndexing Webscraper

This Python script is designed to scrape web pages from a specified domain and save their content as Markdown files. It follows a recursive approach to navigate through the website, ensuring all linked pages within the domain are visited and processed. Additionally, it organizes the saved Markdown files into a folder structure that mirrors the website's subdirectory hierarchy.

## Installation

Before running the script, ensure you have Python installed on your system. You can download Python from the official website.

To install the required dependencies, use pip:

```bash
pip install requests-html html2text
How to Use
Clone this Repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/liot-io/AIOpenDK/tree/main.git
Execute the Python Script: Execute the Python script with the following command:


python treeindex_scraper.py
Script Explanation
Imported Libraries
The script imports the necessary libraries for web scraping, such as os, html2text, requests_html, urllib, and re.

# Function Definitions
extract_filename_from_url: Extracts the filename from a given URL and formats it as a Markdown file.

extract_urls_from_html: Extracts all URLs from the HTML content of a web page.

download_and_save_in_markdown: Downloads the HTML content from a web page, converts it to Markdown format, and saves it as a file.

download: Main function responsible for crawling the website, downloading, and saving pages recursively.

Main Execution
The script defines a list of URLs (PAGES) to start the scraping process.
It creates a base directory (content/example) to store the Markdown files.
The download function is called to initiate the scraping process, which traverses through the web pages, extracts links, and saves Markdown files accordingly.
Example Usage
Suppose we want to scrape the website https://example.dk/:

All pages from the root domain (https://example.dk/) will be saved in the folder content/example.
Pages from subdirectories like https://example.dk/folder will be saved in content/example/folder.
Similarly, pages from deeper subdirectories like https://example.dk/folder/kontrol will be saved in content/example/folder/kontrol.
Notes
Ensure you have proper permissions to write files in the specified directory.
The script may take some time to execute, depending on the size of the website and the number of pages to be scraped.
Adjust the timeout parameter in the script if you encounter connection issues or timeouts with certain websites.

----------------------------------------------------

# PDF Text Scraper

This Python script is designed to extract text from PDF files and save it as Markdown (.md) files. It utilizes the `pdfminer` library to extract text from PDF documents.

## Features

- Extracts text from PDF files
- Saves extracted text as Markdown (.md) files
- Handles errors gracefully
- Can process multiple PDF files in a directory

## Usage

1. **Install Dependencies**: Make sure you have `pdfminer` library installed. You can install it using pip:

   ```bash
   pip install pdfminer.six
Run the Script: Execute the pdf_scraper.py script to extract text from PDF files and save it as Markdown files:

bash
Copy code
python pdf_scraper.py
Ensure that the PDF files you want to scrape are located in the specified directory.

Code Explanation
The script consists of two main functions:

scrape_pdf(filepath)
This function takes a file path to a PDF document as input, extracts text from the PDF using pdfminer.high_level.extract_text, and saves the extracted text as a Markdown file with the same name as the original PDF file.

filepath: Path to the PDF file to be scraped.
scrape_all_pdfs()
This function scrapes text from all PDF files in a specified directory. It iterates through each PDF file in the directory, calls scrape_pdf() function for each file, and handles any errors that occur during the scraping process.

Example Usage
python
Copy code
from pdfminer.high_level import extract_text
import os

def scrape_pdf(filepath):
    try:
        # Extract text from the PDF file
        text = extract_text(filepath)
        
        # Get the filename without extension
        filename = os.path.splitext(os.path.basename(filepath))[0]
        
        # Define the output directory
        output_dir = os.path.join("content", "pdfs")
        os.makedirs(output_dir, exist_ok=True)
        
        # Define the output file path
        output_path = os.path.join(output_dir, f"{filename}.md")
        
        # Write the text to the markdown file
        with open(output_path, "w") as md_file:
            md_file.write(text)
        
        print(f"Scraping successful! Text saved in '{output_path}'.")
    except Exception as e:
        print(f"Error scraping '{filepath}': {e}")

def scrape_all_pdfs():
    # Define the directory containing PDF files
    pdf_directory = os.path.join("content", "pdfs")
    
    # Check if the directory exists
    if not os.path.exists(pdf_directory):
        print("PDF directory not found.")
        return
    
    # Iterate through PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(pdf_directory, filename)
            scrape_pdf(filepath)

if __name__ == "__main__":
    scrape_all_pdfs()
Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
