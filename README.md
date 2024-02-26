# AIOpenDK - simple webscraper services


# Web Page to Markdown Converter

This Python script allows you to download the HTML content from a target web page and save it as a Markdown (.md) file. It utilizes the `requests_html` library to fetch web content and the `html2text` library to convert HTML to Markdown format.

## Features

- Downloads HTML content from a target web page
- Converts HTML content to Markdown format
- Saves Markdown content as a .md file
- Handles non-HTML pages gracefully

## Installation

1. **Clone the Repository**: Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/web-page-to-markdown.git
    ```

2. **Install Dependencies**: Install the required dependencies using pip:

    ```bash
    pip install requests-html html2text
    ```

## Usage

1. **Set Target Page**: Define the target web page URL in the `TARGET_PAGES` list within the script.

2. **Run the Script**: Execute the Python script to download and save the target web page as a Markdown file:

    ```bash
    python convert_to_markdown.py
    ```

## Code Explanation

- **extract_filename_from_url**: Extracts the filename from the URL by parsing the domain name and adding the .md extension.

- **download_and_save_in_markdown**: Downloads the HTML content from the web page, converts it to Markdown format, and saves it as a .md file.

- **download_target_page**: Downloads the HTML content from the target page specified in `TARGET_PAGES` and saves it as a Markdown file.

## Configuration

- **TARGET_PAGES**: Define the target web page URLs in the `TARGET_PAGES` list. The script will download and save each page as a Markdown file.

## Example

Suppose we want to convert the web page https://example.dk/ to Markdown format:

```python
TARGET_PAGES = [
    "https://example.dk/",
]


----------------------------------


# AIOpenDK - TreeIndexing Webscraper

This Python script is designed to scrape web pages from a specified domain and save their content as Markdown files. It follows a recursive approach to navigate through the website, ensuring all linked pages within the domain are visited and processed. Additionally, it organizes the saved Markdown files into a folder structure that mirrors the website's subdirectory hierarchy.

## Installation

Before running the script, ensure you have Python installed on your system. You can download Python from the official website.

To install the required dependencies, use pip:
pip install requests-html html2text

## How to Use
Clone this Repository: Clone this repository to your local machine using the following command:


git clone https://github.com/liot-io/AIOpenDK/tree/main.git

### Execute the Python Script: Execute the Python script with the following command:

python treeindex_scraper.py

## Script Explanation

### Imported Libraries
The script imports the necessary libraries for web scraping, such as os, html2text, requests_html, urllib, and re.

### Function Definitions
extract_filename_from_url: Extracts the filename from a given URL and formats it as a Markdown file.

extract_urls_from_html: Extracts all URLs from the HTML content of a web page.

download_and_save_in_markdown: Downloads the HTML content from a web page, converts it to Markdown format, and saves it as a file.

download: Main function responsible for crawling the website, downloading, and saving pages recursively.

## Main Execution

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
