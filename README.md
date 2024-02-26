# AIOpenDK - simple webscraper services


# Web Scraper for Generating Markdown Files from Web Pages

This Python script is designed to scrape web pages from a specified domain and save their content as Markdown files. It includes functionalities to handle dependencies, avoid duplicates, and filter out non-HTML content.

## Table of Contents

- [Imported Libraries](#imported-libraries)
- [Function Definitions](#function-definitions)
- [Main Execution](#main-execution)
- [Example Usage](#example-usage)
- [Notes](#notes)

## Imported Libraries

The script utilizes the following libraries:

- `os`: Provides a way to interact with the operating system.
- `html2text`: Converts HTML content to Markdown format.
- `requests_html`: A library for making HTTP requests and rendering JavaScript.
- `urllib.parse`: Provides functions to manipulate URLs.
- `re`: Allows the use of regular expressions for pattern matching.

## Function Definitions

### extract_filename_from_url(url: str) -> str

This function extracts the filename from a URL and formats it as a Markdown file.

### extract_urls_from_html(html_content: str, base_url: str) -> List[str]

This function extracts all URLs from the HTML content of a web page.

### download_and_save_in_markdown(url: str, dir_path: str) -> None

Downloads the HTML content from a web page, converts it to Markdown format, and saves it as a file.

### download(pages: List[str]) -> str

Main function responsible for crawling the website, downloading, and saving pages recursively.

## Main Execution

The script defines a list of URLs (`PAGES`) to start the scraping process. It creates a directory named `content/foedevarestyrelsen` to store the Markdown files. The `download` function is called to initiate the scraping process, which traverses through the web pages, extracts links, and saves Markdown files accordingly.

## Example Usage

To scrape the website [https://foedevarestyrelsen.dk/](https://foedevarestyrelsen.dk/), simply execute the script. All pages from the root domain will be saved in the folder `content/foedevarestyrelsen`. Pages from subdirectories will also be saved in their respective folders within `content/foedevarestyrelsen`.


python your_script.py


## Notes

Ensure you have proper permissions to write files in the specified directory.
The script may take some time to execute, depending on the size of the website and the number of pages to be scraped.
Adjust the timeout parameter in the script if you encounter connection issues or timeouts with certain websites.


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



License
This project is licensed under the MIT License - see the LICENSE file for details.
