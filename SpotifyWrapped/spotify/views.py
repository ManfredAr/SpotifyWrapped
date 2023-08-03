from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import spotipy
from backend.albums import album
from backend.Songs import songs
from backend.artist import artists
from backend.genre import genres
from backend.recommendation import recommendations
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
import os

# Create your views here.
def authorise(request):
    scope = "user-read-private playlist-read-private playlist-modify-private playlist-modify-public user-top-read"

    # Getting a spotify object
    sp = SpotifyOAuth(client_id=str(os.getenv('CLIENT_ID')), client_secret= str(os.getenv('CLIENT_SECRET')), redirect_uri=str(os.getenv('REDIRECT_URI')), scope=scope)

    # Getting the user to authorise their account
    url = sp.get_authorize_url()

    return HttpResponseRedirect(url)

def home(request):
    scope = "user-read-private playlist-read-private playlist-modify-private playlist-modify-public user-top-read"
        
    # Create a SpotifyOAuth object
    sp = SpotifyOAuth(client_id=str(os.getenv('CLIENT_ID')), client_secret= str(os.getenv('CLIENT_SECRET')), redirect_uri=str(os.getenv('REDIRECT_URI')), scope=scope)
    
    # Get the authorization code from the query parameters
    code = request.GET.get("code")

    # Request an access token using the authorization code
    token_info = sp.get_access_token(code)

    # Extract the access token
    access_token = token_info["access_token"]

    # Storing the access tokens
    request.session["access_token"] = access_token

    # Redirect the user to the top tracks page
    return HttpResponseRedirect("/tracks/")

def recent(request):
    return songs.getSongs(request)

def albums(request):
    return album.getAlbums(request)

def artist(request):
    return artists.getArtist(request)

def genre(request):
    return genres.getGenres(request, False)

def recommendation(request):
    return recommendations.getRecommendation(request)
    