import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from a URL and save it to text and CSV files
def scrape_and_save(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text data and save it to a text file
        with open(r'C:/Users/Dell/Desktop/Project_168/7_Data sets/17_Affiliated colleges.txt', 'w', encoding='utf-8') as f:
            f.write(soup.get_text())

        # Extract tabular data and save it to a CSV file
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')
            with open(r'C:/Users/Dell/Desktop/Project_168/7_Data sets/17_Affiliated colleges.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                    writer.writerow(cells)
        else:
            print("No table found on the page.")

        print("Scraping and saving completed.")
    else:
        print("Failed to retrieve data from the URL.")


# Example usage:
url = 'http://jntuhaac.in/AcademicAuditCell/ViceChancellor'
scrape_and_save(url)