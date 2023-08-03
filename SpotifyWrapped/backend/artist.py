from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
import os


class artists:

    @staticmethod
    def getArtist(request):
         # Get the access token from the session
        access_token = request.session.get("access_token")

        # Create a Spotipy client using the access token
        sp = spotipy.Spotify(auth=access_token)

        if request.method == "GET":
            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_artists(limit=20, offset=0, time_range="long_term")
        elif request.method == "POST":
            time = request.POST.get("fil")
            amount = request.POST.get("quantity")

            if (not time):
                time = "medium_term"
            
            if (not amount):
                amount = 10

            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_artists(limit=amount, offset=0, time_range=time)
        else: 
            return "error"

        # Extract the top tracks from the response
        artists = response["items"]

         # Create a list of dictionaries representing the top tracks
        singer = []
        for artist in artists:
            artist_info = {
                "name": artist["name"],
                "image": artist["images"][0]["url"],
                "url":artist["external_urls"]
            }
            singer.append(artist_info)
        

        if request.method == "GET":
            print(singer)
            return render(request, 'spotify/artist.html', {'artists':singer})
        elif request.method == "POST":
            print(singer)
            return JsonResponse({'artists': singer});
        else:
            return artists