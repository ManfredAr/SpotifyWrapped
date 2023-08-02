from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
from collections import Counter
load_dotenv()
import os


class genres:

    @staticmethod
    def getGenres(request):
         # Get the access token from the session
        access_token = request.session.get("access_token")

        # Create a Spotipy client using the access token
        sp = spotipy.Spotify(auth=access_token)

        if request.method == "GET":
            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_artists(limit=50, offset=0, time_range="long_term")
        elif request.method == "POST":
            time = request.POST.get("fil")
            amount = request.POST.get("quantity")

            if (not time):
                time = "medium_term"

            # Make the HTTP GET request to the Spotify API
            response = sp.current_user_top_artists(limit=50, offset=0, time_range=time)
        else: 
            return "error"

        # Extract the top tracks from the response
        tracks = response["items"]

         # Create a list of dictionaries representing the top tracks
        genres = {}
        for track in tracks:
            genre = track["genres"]
            for i in genre:
                if i in genres:
                    genres[i] = genres.get(i) + 1
                else:
                    genres[i] = 1
        


        if request.method == "GET":
            top_genres = Counter(genres).most_common(10)
            return render(request, 'spotify/genre.html', {'genres':top_genres})
        elif request.method == "POST":
            amount = request.POST.get("quantity")
            if amount:
                top_genres = Counter(genres).most_common(int(amount))
                return JsonResponse({'genres': top_genres});
         
            top_genres = Counter(genres).most_common(10)
            return JsonResponse({'genres': top_genres});