import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

def get_top_tracks(year):
    query = f"year:{year}"
    results = sp.search(q=query, type="track", limit=50, market="US")
    
    tracks = []
    while len(tracks) < 50:
        for track in results["tracks"]["items"]:
            track_name = track["name"]
            artist_name = ", ".join(artist["name"] for artist in track["artists"])
            popularity = track["popularity"]
            album_name = track["album"]["name"]
            duration_ms = track["duration_ms"] // 1000  # Convertendo para segundos
            track_id = track["id"]
            release_date = track["album"]["release_date"]
            album_id = track["album"]["id"]
            
            # Buscar gêneros musicais do álbum
            album_info = sp.album(album_id)
            genres = album_info.get("genres", [])
            genre_str = ", ".join(genres) if genres else "Unknown"
            
            tracks.append([year, track_name, artist_name, album_name, duration_ms, genre_str, track_id, release_date, popularity])
        
        if len(tracks) < 50 and results["tracks"].get("next"):
            results = sp.next(results["tracks"])
        else:
            break
    
    tracks = tracks[:50]
    tracks.sort(key=lambda x: x[8], reverse=True)  # Ordenar por popularidade
    
    return tracks

def save_tracks_to_csv(start_year, end_year, filename="top_tracks.csv"):
    all_tracks = []
    for year in range(start_year, end_year + 1):
        all_tracks.extend(get_top_tracks(year))
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Track", "Artist", "Album", "Duration (s)", "Genres", "Track ID", "Release Date", "Popularity"])
        writer.writerows(all_tracks)
    
    print(f"Top 50 tracks de {start_year} até {end_year} foram salvas em {filename}")
