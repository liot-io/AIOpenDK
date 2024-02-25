# AIOpenDK - simple webscraper

# Web Scraper for Generating Markdown Files from Web Pages
Overview
This Python script allows you to scrape a domain specified in the PAGES list, download HTML content from its pages, and save them as Markdown files. The script includes functionalities to handle dependencies, avoid duplicates, and filter out non-HTML content.

# Installation
Python: Make sure you have Python installed on your system. You can download it from the official Python website.

Clone the Repository: Clone or download the script from the repository where it's hosted.

Install Dependencies: Install the required dependencies using pip. Run the following command in your terminal:

pip install requests-html html2text

# Usage

Set Pages: Define the URLs of the pages you want to scrape in the PAGES list. You can specify multiple URLs.

Run the Script: Execute the script by running it in your terminal or IDE.

Output: The script will create a directory named content in the same location as the script. Inside the content directory, it will create a subdirectory named after the domain being scraped (e.g., Example). The Markdown files will be saved in this directory.

# Code Explanation

Imported Libraries: The script imports necessary libraries such as:
- os,
- html2text,
- HTMLSession from requests_html,
- urlparse,
- re, etc.

# Functions:

extract_filename_from_url(url): --> Extracts the filename from the URL and saves it as a .md file.

extract_urls_from_html(html_content, base_url): --> Extracts URLs from HTML content.

download_and_save_in_markdown(url, dir_path): --> Downloads HTML content from a webpage, converts it to Markdown, and saves it.

download(pages): --> Downloads HTML content from the specified pages, saves them as Markdown files, and handles subpages within the root URL.

# Execution:

The script checks if it's being run as the main program (if __name__ == "__main__":), then calls the download function with the specified PAGES.
Handling Duplicates

The script uses a set named processed_urls to track processed URLs and avoid duplicates. Before processing a URL, it checks if it's already present in the set. If not, it adds the URL to the set and proceeds with processing. This ensures that each URL is processed only once.

# Filtering Non-HTML Content
The script checks the content type of the response to ensure that it's HTML before proceeding with rendering and conversion to Markdown. If the content type is not HTML, it skips processing that URL.

# Dependencies
requests-html: Used for making HTTP requests and rendering JavaScript.
html2text: Used for converting HTML content to Markdown format.

# Example

PAGES = [
    "https://example.com/",
]
Replace "https://example.com/" with the URLs of the pages you want to scrape.


----------------------------------


# AIOpenDK - TreeIndexing webscraper

This Python script is designed to scrape web pages from a specified domain and save their content as Markdown files. It follows a recursive approach to navigate through the website, ensuring all linked pages within the domain are visited and processed. Additionally, it organizes the saved Markdown files into a folder structure that mirrors the website's subdirectory hierarchy.

# Installation
Before running the script, ensure you have Python installed on your system. You can download Python from the official website.

To install the required dependencies, use pip:

pip install requests-html html2text

# How to Use

Clone this repository to your local machine using the following command:

git clone https://github.com/liot-io/AIOpenDK/tree/main.git

Execute the Python script with the following command:
python treeindex_scraper.py

# Script Explanation

Imported Libraries: The script imports the necessary libraries for web scraping, such as os, html2text, requests_html, urllib, and re.

# Function Definitions:

extract_filename_from_url: --> Extracts the filename from a given URL and formats it as a Markdown file.

extract_urls_from_html: --> Extracts all URLs from the HTML content of a web page.

download_and_save_in_markdown: --> Downloads the HTML content from a web page, converts it to Markdown format, and saves it as a file.

download: --> Main function responsible for crawling the website, downloading and saving pages recursively.
Main Execution:

# The script defines a list of URLs (PAGES) to start the scraping process.

It creates a base directory (content/example) to store the Markdown files.
The download function is called to initiate the scraping process, which traverses through the web pages, extracts links, and saves Markdown files accordingly.
Example Usage
Suppose we want to scrape the website https://example.dk/:

All pages from the root domain (https://example.dk/) will be saved in the folder content/example
Pages from subdirectories like https://example.dk/folder will be saved in content/example/folder.

Similarly, pages from deeper subdirectories like https://example.dk/folder/kontrol will be saved in content/example/folder/kontrol.

# Notes
Ensure you have proper permissions to write files in the specified directory.
The script may take some time to execute, depending on the size of the website and the number of pages to be scraped.
Adjust the timeout parameter in the script if you encounter connection issues or timeouts with certain websites.
