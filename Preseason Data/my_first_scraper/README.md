# Welcome to My First Scraper

My First Scraper is an innovative tool designed to fetch and analyze data from GitHub's trending repositories
seamlessly. It simplifies the process of extracting valuable information for developers and data enthusiasts.

## Task
-What is the problem? And where is the challenge?
Web scraping can often be complex, especially when navigating through intricate HTML structures on sites like GitHub.
Many users struggle to extract relevant data efficiently due to the dynamic nature of web content.

-And where is the challenge?

This project addresses the challenge of gathering and organizing data from these repositories for further analysis.


## Description
-How have you solved the problem?
I have developed a Python-based scraper that utilizes the `requests` library to fetch HTML content and
`BeautifulSoup` to parse it effectively. The solution extracts crucial information such as developer names,
repository names, and star counts, transforming it into a user-friendly CSV format that can be easily analyzed 
imported into other applications.


## Installation
-How to install your project? npm install? make? make re?
To get started with My First Scraper, you will need to install the required Python libraries.
Use pip to install them as follows:


## Usage
How does it work?
The scraper sends an HTTP GET request to GitHub's trending repositories page
It retrieves the full HTML content.  

Using BeautifulSoup, it parses the HTML.  

The scraper extracts relevant data like  
developer names, repository names,  
and star counts from the parsed HTML.  

This data is organized into dictionaries  
for each repository for easy access.  

Finally, it formats the data into a  
CSV string for easy analysis and export.
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
