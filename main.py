import threading
from Web_Scrapping import extract_data, fetch
from db import insert_data


def main():
    base_url = "https://nkiri.com/category/international/"
    n = range(1, 2)
    
    all_movie_data = []
    for num in n:
        url = f'{base_url}page/{num}/'  
        print("Fetching data from:", url)
        response_text = fetch(url)
        if response_text:
            print("Extracting data...")
            movie_data = extract_data(response_text)
            all_movie_data.extend(movie_data)
        else:
            print("Failed to fetch data from:", url)
    
    print("Inserting data into database...")
    insert_data(all_movie_data)
    print("Data insertion complete.")
    

def run_async_with_threading():
    try:
        thread = threading.Thread(target=main)
        thread.start()
        thread.join()
    except Exception as e:
        print("Error running thread:", e)

if __name__ == "__main__":
    run_async_with_threading()
    main()