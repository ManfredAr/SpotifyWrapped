from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
import os


class album:

    def getAlbums(request):
         # Get the access token from the session
        access_token = request.session.get("access_token")

        # Create a Spotipy client using the access token
        sp = spotipy.Spotify(auth=access_token)

        if request.method == "GET":
            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_tracks(limit=30, offset=0, time_range="short_term")
        elif request.method == "POST":
            time = request.POST.get("fil")
            amount = request.POST.get("quantity")

            if (not time):
                time = "medium_term"
            
            if (not amount):
                amount = 10

            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_tracks(limit=amount, offset=0, time_range=time)
        else: 
            return "error"

        # Extract the top tracks from the response
        top_tracks = response["items"]

         # Create a list of dictionaries representing the top tracks
        tracks = []
        for track in top_tracks:
            track_info = {
                "artist": track["artists"][0]["name"],
                "image": track["album"]["images"][0]["url"],
                "album": track["album"]["name"],
                "release": track["album"]["release_date"],
                "link": track["album"]["external_urls"]['spotify']
            }
            tracks.append(track_info)
            
        if request.method == "GET":
            return render(request, 'spotify/album.html', {'tracks':tracks})
        elif request.method == "POST":
            return JsonResponse({'tracks': tracks});