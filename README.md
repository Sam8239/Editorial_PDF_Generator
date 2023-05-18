
# Editorial PDF Generator 

This Python script aims to extract **editorials from the Hindustan Times website** and generate PDF files based on the extracted content.  
The script utilizes Selenium, BeautifulSoup, and other libraries to scrape the web pages and convert the data into PDF format.
## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- Selenium
- BeautifulSoup
- ReportLab

Additionally, you will need to download the **ChromeDriver executable** compatible with your system and provide its file path in the driver_path variable.

ChromeDriver can be dowloaded from this website:
[ChromeDriver](https://chromedriver.chromium.org/downloads)

**Note: Download the chrome driver for your version of google chrome.**
## Run Locally

Clone the project

```bash
  git clone https://github.com/Sam8239/Editorial_PDF_Generator.git
```

Go to the project directory

```bash
  cd Editorial_PDF_Generator
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the script

```bash
  python Editorials.py
```


## Usage

The script provides a **command-line interface** to select the desired options for generating PDF files. It continuously prompts the user for an option until they choose to exit. The options are:
        
    1. Generate a single PDF file containing all the editorials
    2. Generate separate PDF files for each editorial
    3. Exit


## Limitations

- Website Dependency: The code relies on scraping the Hindustan Times website to extract editorials. If the structure or layout of the website changes, it may break the scraping functionality, resulting in incorrect or incomplete data extraction.

- Fragile Parsing: The code uses BeautifulSoup to parse the HTML content of the website. If the HTML structure of the website changes, it may affect the accuracy of the data extraction. The code assumes specific HTML elements and classes, so any changes to those may require adjustments in the code.

- Stability and Error Handling: The code does not include robust error handling or exception management. If any errors occur during the scraping process, the code may terminate abruptly, leading to an incomplete extraction or unexpected behavior.

- Performance Considerations: The code scrapes the web pages sequentially, which may not be efficient for large volumes of data or if there are delays in retrieving each web page. Considerations such as implementing parallel processing or handling network-related issues could improve the performance and reliability of the extraction process.

- Maintenance and Updates: The code may require updates and maintenance to adapt to changes in the target website or to improve its functionality. As websites evolve over time, it's important to regularly review and update the code to ensure its continued effectiveness.

- Browser Dependency: The code is designed to work with the ChromeDriver executable, indicating a dependency on the Google Chrome browser. It may not be compatible or work as intended with other web browsers. If you need to run the code with a different browser, you would need to modify the code accordingly and ensure compatibility with the chosen browser.

Efforts will be made to address and overcome the mentioned limitations in order to enhance the code's functionality and adaptability.
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.


## Support

For support, email samanta.shubham99@gmail.com

