import requests
from bs4 import BeautifulSoup
import unittest

# Part 0: Request
def request_github_trending(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response  # Return the full response object

# Part 1: Extract
def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')  # Use page.text to get the HTML content
    return soup.find_all('article', class_='Box-row')

# Part 2: Transform
def transform(html_repos):
    repositories = []
    for repo in html_repos:
        # Extract developer and repository name
        title_element = repo.h1.find('a') if repo.h1 and repo.h1.find('a') else None
        if title_element and '/' in title_element.text:
            title = title_element.text.strip().split('/')
            developer = title[0].strip()
            repository_name = title[1].strip()
        else:
            developer = "Unknown"
            repository_name = "Unknown"

        # Extract the number of stars
        stars_element = repo.find('a', class_='Link--muted d-inline-block mr-3')
        nbr_stars = stars_element.text.strip().replace(',', '') if stars_element else '0'

        # Append the data as a dictionary
        repositories.append({
            'developer': developer,
            'repository_name': repository_name,
            'nbr_stars': nbr_stars
        })
    return repositories

# Part 3: Format
def format(repositories_data):
    output = "Developer,Repository Name,Number of Stars\n"
    for repo in repositories_data:
        line = f"{repo['developer']},{repo['repository_name']},{repo['nbr_stars']}\n"
        output += line
    return output

# Test case
class TestGitHubScraper(unittest.TestCase):
    def test_request_github_trending(self):
        url = 'https://storage.googleapis.com/qwasar-public/track-ds/trending_14_06_2022'
        page = request_github_trending(url)

        # Check if the returned object is an instance of requests.Response
        self.assertTrue(isinstance(page, requests.Response))

# Run the tests
if __name__ == "__main__":
    unittest.main()
