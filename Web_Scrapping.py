import requests
from bs4 import BeautifulSoup


def fetch(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch data from:", url)
            return None
    except Exception as e:
        print("Error fetching data:", e)
        return None

def extract_data(response_text):
    if not response_text:
        return []
    try:
        soup = BeautifulSoup(response_text, 'html.parser')
        movie_data = []
        for movie in soup.find_all('div', class_='movie-item'):
            movie_name = movie.find('h2', class_="blog-entry-title entry-title")
            name = movie_name.text.strip() if movie_name else "Unknown"
            img = movie.find('img')
            image = img.get('src') if img else "No Image"
            details_preview = movie.find('p', class_='movie-details')
            detail = details_preview.text.strip() if details_preview else "No Details"
            link = movie.find('a')
            url = link.get('href') if link else "No URL"
            movie_data.append((name, image, url, detail))
        return movie_data
    except Exception as e:
        print("Error extracting data:", e)
        return []


