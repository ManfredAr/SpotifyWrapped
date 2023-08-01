from django.http import HttpResponseRedirect
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
import os

# Create your views here.
def authorise(request):
    scope = "user-read-private playlist-read-private playlist-modify-public user-top-read"

    # Getting a spotify object
    sp = SpotifyOAuth(client_id=str(os.getenv('CLIENT_ID')), client_secret= str(os.getenv('CLIENT_SECRET')), redirect_uri=str(os.getenv('REDIRECT_URI')), scope=scope)

    # Getting the user to authorise their account
    url = sp.get_authorize_url()

    return HttpResponseRedirect(url)

def home(request):
    scope = "user-read-private playlist-read-private playlist-modify-public user-top-read"
        
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
    return HttpResponseRedirect("/recent/")

def recent(request):
    if request.method == 'GET':
         # Get the access token from the session
        access_token = request.session.get("access_token")
        print('\n\n ACCESS TOKEN: ', access_token, '\n\n')

        # Create a Spotipy client using the access token
        sp = spotipy.Spotify(auth=access_token)

        # Make the HTTP GET request to the Spotify API
        response = sp.current_user_top_tracks(limit=3, offset=0, time_range="short_term")

        # Extract the top tracks from the response
        top_tracks = response["items"]

         # Create a list of dictionaries representing the top tracks
        tracks = []
        for track in top_tracks:
            track_info = {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
            }
            tracks.append(track_info)

        # print tracks list to console
        print("\n\n\n\nLIST OF TRACKS:",tracks)

        # Return a JSON response containing the top tracks]
        return render(request, 'spotify/recent.html', {'tracks':tracks})
    else:
        error = "An error has occurred"
        return error



        