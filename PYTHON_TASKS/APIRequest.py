#The API works onyl for Anime ID 1 and Anime ID 5114 because for the rest of the indexes, we dont have any content from the database
import requests

def fetch_anime_data(anime_id):
    api_url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        title = data.get('data', {}).get('title', 'N/A')
        synopsis = data.get('data', {}).get('synopsis', 'No synopsis available.')
        episodes = data.get('data', {}).get('episodes', 'Unknown')
        
        print(f"Title: {title}")
        print(f"Synopsis: {synopsis}")
        print(f"Number of Episodes: {episodes}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404: print(f"No anime found for ID {anime_id}. Please try a different ID.")
        else: print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e: print(f"Error fetching anime data: {e}")
anime_id = input("Enter the anime ID: ")
fetch_anime_data(anime_id)




















#https://github.com/jikan-me/jikan -> Public API