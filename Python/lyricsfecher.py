import requests
from bs4 import BeautifulSoup

def get_lyrics(song_title, artist):
    base_url = 'https://www.lyrics.com/'
    search_url = f'{base_url}lyrics/{artist.replace(" ", "%20")}/{song_title.replace(" ", "%20")}'

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the lyrics are found
    lyrics_container = soup.find('pre', {'class': 'lyric-body'})
    
    if lyrics_container:
        lyrics = lyrics_container.get_text('\n', strip=True)
        return lyrics
    else:
        return "Lyrics not found."

# Example usage
song_title = "lovely by Billie Eilish and Khalid"
artist = "Billie Eilish"

lyrics = get_lyrics(song_title, artist)
print(lyrics)
