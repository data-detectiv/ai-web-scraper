
# AI Web Scraper

## Overview
This AI-powered web scraper leverages **Selenium**, **Streamlit**, and **Llama3.1** to automate content extraction, cleaning, and processing. Designed for accessibility and efficiency, this tool enables users to scrape structured or unstructured data while offering multiple export options for enhanced usability.

## Features
- **Automated Web Scraping**: Uses Selenium for dynamic content extraction.
- **AI-Powered Data Processing**: Llama3.1 enhances text cleaning and summarization.
- **User-Friendly Interface**: Built with Streamlit for seamless interactions.
- **Multi-Format Data Export**: Supports JSON, CSV, Word, PDF, and Excel.
- **Cloud Deployment**: Optimized for accessibility via Streamlit Cloud.

## Installation
Ensure you have Python 3.8+ installed. Then, clone the repository and install dependencies:

```sh
git clone <repo-url>
cd ai-web-scraper
pip install -r requirements.txt
```

## Usage
Run the scraper via Streamlit:

```sh
streamlit run app.py
```

Users can input target URLs, configure scraping parameters, and download processed data in preferred formats.

## Dependencies
- `streamlit`
- `selenium`
- `llama3.1`
- `pandas`
- `openpyxl`
- `python-docx`
- `pdfkit`

Install required packages with:

```sh
pip install streamlit selenium llama3.1 pandas openpyxl python-docx pdfkit
```

## Deployment
To deploy on **Streamlit Cloud**:
1. Upload the project to GitHub.
2. Configure dependencies in `requirements.txt`.
3. Deploy via Streamlit’s cloud hosting service.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.
