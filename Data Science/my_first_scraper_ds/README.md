# Welcome to My First Scraper Ds
"My First Scraper" is an introductory project designed to familiarize you with the fundamentals of web scraping. Whether you are a budding data scientist, a software engineer, or simply curious about how data can be gathered from the web, this project serves as a perfect starting point.

## Task
The task is to create a web scraper that collects actionable data from GitHub Trending repositories. The challenge lies in navigating the HTML structure, extracting relevant information, and presenting it in a structured format like CSV.

## Description
We used Python with the requests and BeautifulSoup libraries to solve this problem. The scraper performs the following steps:
Sends a request to the GitHub Trending page.
Parses the HTML to extract repository data such as developer names, repository names, and the number of stars.
Transforms the extracted data into a structured format i.e list of dictionaries.
Outputs the data as a CSV file for easy readability and further processing.
This scraper is efficient, reusable, and can handle changes in HTML structure by updating the extraction logic.

## Installation
How to install your project?
Clone this repository:
Install the required dependencies:
Ensure you have Python installed version 3.6 or above.
## Usage
How does it work?
Run the scraper script to generate a CSV file containing the top 25 trending repositories from GitHub.
python scraper.py
After execution, you will find a trending_repos.csv file in the project directory.
The CSV file will contain columns:
Developer
Repository Name
Number of Stars

### The Core Team
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
