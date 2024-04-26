# AIOpenDK - simple scraper services

-----------------------------------

# AIOpenDK - Web Page to Markdown Scraper

This Python script allows you to download the HTML content from a target web page and save it as a Markdown (.md) file. It utilizes the `requests_html` library to fetch web content and the `html2text` library to convert HTML to Markdown format.

## Features

- Downloads HTML content from a target web page
- Converts HTML content to Markdown format
- Saves Markdown content as a .md file
- Handles non-HTML pages gracefully

## Installation

1. **Clone the Repository**: Clone this repository to your local machine:

    ```bash
    git clone https://github.com/liot-io/AIOpenDK.git
    ```

2. **Install Dependencies**: Install the required dependencies using pip:

    ```bash
    pip install requests-html html2text
    ```


## Function Definitions

- **extract_filename_from_url**: --> Extracts the filename from the URL by parsing the domain name and adding the .md extension.

- **download_and_save_in_markdown**: --> Downloads the HTML content from the web page, converts it to Markdown format, and saves it as a .md file.

- **download_target_page**: --> Downloads the HTML content from the target page specified in `TARGET_PAGES` and saves it as a Markdown file.
  

## Configuration

- **TARGET_PAGES**: Define the target web page URLs in the `TARGET_PAGES` list. The script will download and save each page as a Markdown file.
  

## Example

Suppose we want to convert the web page https://example.dk/ to Markdown format:

Upon running the script, the HTML content of the target page will be downloaded, converted to Markdown, and saved as example.dk.md in the content directory.


## Running the Script

1. **Set Target Page**: Define the target web page URL in the `TARGET_PAGES` list within the script.

2. **Run the Script**: Execute the Python script to download and save the target web page as a Markdown file:

    ```bash
    python web_scraper.py
    ```


## Notes

Ensure that you have proper permissions to write files in the specified directory.

The script will skip non-HTML pages and handle errors gracefully.

Adjust the timeout parameters in the script if you encounter connection issues or timeouts with certain websites.

You can modify the script to customize the directory structure or filename as per your requirements.



----------------------------------


# AIOpenDK - TreeIndexing Webscraper

This Python script is designed to scrape web pages from a specified domain and save their content as Markdown files. It follows a recursive approach to navigate through the website, ensuring all linked pages within the domain are visited and processed. 

Additionally, it organizes the saved Markdown files into a folder structure that mirrors the website's subdirectory hierarchy.


## Installation

Before running the script, ensure you have Python installed on your system. You can download Python from the official website.

To install the required dependencies, use pip:


    pip install requests-html html2text



## How to Use
Clone this Repository: Clone this repository to your local machine using the following command:


    git clone https://github.com/liot-io/AIOpenDK/tree/main.git

    

## Script Explanation


### Imported Libraries


The script imports the necessary libraries for web scraping, such as os, html2text, requests_html, urllib, and re.


### Function Definitions


**extract_filename_from_url**: --> Extracts the filename from a given URL and formats it as a Markdown file.


**extract_urls_from_html**: --> Extracts all URLs from the HTML content of a web page.


**download_and_save_in_markdown**: --> Downloads the HTML content from a web page, converts it to Markdown format, and saves it as a file.


**download**: --> Main function responsible for crawling the website, downloading, and saving pages recursively.


## Main Execution

The script defines a list of URLs (PAGES) to start the scraping process.
It creates a base directory (content/example) to store the Markdown files.

The download function is called to initiate the scraping process, which traverses through the web pages, extracts links, and saves Markdown files accordingly.


## Configuration

- **PAGES**: Define the target web page URLs in the `TARGET_PAGES` list. The script will download and save each page as a Markdown file.


## Example

Suppose we want to scrape the website https://example.dk/:

All pages from the root domain (https://example.dk/) will be saved in the folder content/example.

Pages from subdirectories like https://example.dk/folder will be saved in content/example/folder.

Similarly, pages from deeper subdirectories like https://example.dk/folder/kontrol will be saved in content/example/folder/kontrol.


## Running the Script

1. **Set Page**: Define the target web page URL in the `PAGES` list within the script.

2. **Run the Script**: Execute the Python script to download and save the target web page as a Markdown file:

    ```bash
    python treeindex_scraper.py
    ```



## Notes
Ensure you have proper permissions to write files in the specified directory.
The script may take some time to execute, depending on the size of the website and the number of pages to be scraped.
Adjust the timeout parameter in the script if you encounter connection issues or timeouts with certain websites.

----------------------------------------------------

# AIOpenDK - PDF Text Scraper

This Python script scrapes text from all PDF files in a specified directory and saves them as Markdown files.


## Prerequisites

- Python 3.x
- pdfminer.six library (Install via pip install pdfminer.six)


## Usage

1. Clone the repository or download the script file (pdf_text_scraper.py).
2. Ensure that Python and the required dependencies are installed.
3. Place your PDF files in the specified directory (content/example.dk/src_pdf).
4. Run the script pdf_text_scraper.py.
5. The scraped text will be saved as Markdown files in the output directory (content/example.dk/pdfs).


## How It Works

- The script iterates through all PDF files in the specified directory.
- For each PDF file:
  1. It checks if the file has been processed before to avoid duplicates.
  2. It extracts text from the PDF using the extract_text function from pdfminer.high_level.
  3. The extracted text is saved as a Markdown file in the output directory.
- If an error occurs during the scraping process, the script prints an error message.


## Definitions

**pdf_text_scraper.py**: --> Main Python script.

**content/example.dk/src_pdf**: --> Directory containing input PDF files.

**content/example.dk/pdfs**: --> Directory where Markdown files will be saved.


## Running the Script


    python pdf_scraper.py

