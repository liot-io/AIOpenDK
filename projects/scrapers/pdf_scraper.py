from pdfminer.high_level import extract_text
import os

def scrape_all_pdfs():
    """Scrape text from all PDF files in the specified directory and save them as Markdown files."""
    # Define the directory containing PDF files
    pdf_directory = os.path.join("content", "example", "src_pdf")
    
    # Check if the directory exists
    if not os.path.exists(pdf_directory):
        print("PDF directory not found.")
        return
    
    # Create the output directory for Markdown files
    output_dir = os.path.join("content", "example", "pdfs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Track filenames to skip duplicates
    processed_files = set()
    
    # Iterate through PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            try:
                # Check if the file has been processed before
                if filename in processed_files:
                    print(f"Skipping - Duplicate file: '{filename}'")
                    continue
                
                # Mark the file as processed
                processed_files.add(filename)
                
                # Extract text from the PDF file
                text = extract_text(os.path.join(pdf_directory, filename))
                
                # Get the filename without extension
                filename_without_extension = os.path.splitext(filename)[0]
                
                # Define the output file path for the Markdown file
                output_path = os.path.join(output_dir, f"{filename_without_extension}.md")
                
                # Write the text to the Markdown file
                with open(output_path, "w") as md_file:
                    md_file.write(text)
                
                print(f"Scraping successful! Text saved in '{output_path}'.")
            except Exception as e:
                print(f"Error scraping '{filename}': {e}")

if __name__ == "__main__":
    scrape_all_pdfs()
