document.addEventListener('DOMContentLoaded', function() {
  const playlistDiv = document.getElementById('playlist_uri');
  const playlistUri = playlistDiv.getAttribute('data-playlist-uri');

  const iframe = document.createElement('iframe');
  iframe.title = 'Spotify Embed: Recommendation Playlist';
  iframe.src = `https://open.spotify.com/embed/playlist/${playlistUri}?utm_source=generator&theme=0`;
  iframe.width = '100%';
  iframe.height = '100%';
  iframe.style.minHeight = '360px';
  iframe.frameBorder = '0';
  iframe.allow = 'autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture';
  iframe.loading = 'lazy';

  document.getElementById('embed-iframe').appendChild(iframe);
});