window.onSpotifyWebPlaybackSDKReady = () => {
  const playlistDiv = document.getElementById('playlist_uri');
  const playlistUri = playlistDiv.getAttribute('data-playlist-uri');

  const spotifyEmbedContainer = document.getElementById('playlist_uri');

  const iframe = document.createElement('iframe');
  iframe.title = 'Spotify Playlist Embed';
  iframe.src = `https://open.spotify.com/embed/playlist/${playlistUri}`;
  iframe.width = '350px';
  iframe.height = '380px'; // Adjust the height as needed
  iframe.frameBorder = '0';
  iframe.allow = 'encrypted-media *';

  spotifyEmbedContainer.appendChild(iframe);
};