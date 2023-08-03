document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(event.target); // 'this' refers to the form element with ID 'search'
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/album/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText); // Parse the JSON response
                    const tracks = response.tracks; // Extract the 'tracks' array from the response

                    // Clear any existing content on the screen
                    const resultsContainer = document.getElementById('tracks');
                    resultsContainer.innerHTML = '';

                    for (const album of tracks) {
                        const albumElement = document.createElement('div');
                        albumElement.classList.add('album');
            
                        const cardElement = document.createElement('div');
                        cardElement.classList.add('card');
                        cardElement.style.width = '18rem';
            
                        const imgElement = document.createElement('img');
                        imgElement.classList.add('card-img-top');
                        imgElement.src = album.image;
                        imgElement.alt = 'Album image cap';
            
                        const cardBodyElement = document.createElement('div');
                        cardBodyElement.classList.add('card-body');
            
                        const titleElement = document.createElement('h5');
                        titleElement.classList.add('card-title');
                        titleElement.textContent = album.album;
            
                        const cardTextElement = document.createElement('div');
                        cardTextElement.classList.add('card-text');
            
                        const artistElement = document.createElement('p');
                        artistElement.textContent = `By: ${album.artist}`;
            
                        const releaseElement = document.createElement('p');
                        releaseElement.textContent = `Released: ${album.release}`;
            
                        const linkElement = document.createElement('a');
                        linkElement.href = album.link;
                        linkElement.textContent = 'Go to website';
            
                        cardTextElement.appendChild(artistElement);
                        cardTextElement.appendChild(releaseElement);
            
                        cardBodyElement.appendChild(titleElement);
                        cardBodyElement.appendChild(cardTextElement);
                        cardBodyElement.appendChild(linkElement);
            
                        cardElement.appendChild(imgElement);
                        cardElement.appendChild(cardBodyElement);
            
                        albumElement.appendChild(cardElement);
            
                        resultsContainer.appendChild(albumElement);
                    }
                }
            }
        };

        xhr.send(formData);
    });
});




