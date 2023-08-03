document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(event.target); // 'this' refers to the form element with ID 'search'
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/song/filter/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText); // Parse the JSON response
                    const tracks = response.tracks; // Extract the 'tracks' array from the response

                    // Clear any existing content on the screen
                    const resultsContainer = document.getElementById('tracks');
                    resultsContainer.innerHTML = '';

                    // Create HTML elements for each track and append them to the 'resultsContainer'
                    for (const track of tracks) {
                        const trackElement = document.createElement('div');
                        trackElement.classList.add('track');

                        const nameElement = document.createElement('p');
                        nameElement.classList.add('h3');
                        nameElement.textContent = track.name;

                        const artistElement = document.createElement('p');
                        artistElement.textContent = `By: ${track.artist}`;

                        const albumElement = document.createElement('p');
                        albumElement.textContent = `Album: ${track.album}`;

                        trackElement.appendChild(nameElement);
                        trackElement.appendChild(artistElement);
                        trackElement.appendChild(albumElement);

                        resultsContainer.appendChild(trackElement);
                    }
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };

        xhr.send(formData);
    });
});




