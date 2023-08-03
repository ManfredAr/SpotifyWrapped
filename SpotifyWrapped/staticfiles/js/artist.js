document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(event.target); // 'this' refers to the form element with ID 'search'
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/artist/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText); // Parse the JSON response
                    const artists = response.artists; // Extract the 'tracks' array from the response

                    // Clear any existing content on the screen
                    const resultsContainer = document.getElementById('tracks');
                    resultsContainer.innerHTML = '';

                    for (const artist of artists) {
                        const artistElement = document.createElement('div');
                        artistElement.classList.add('artist');
                    
                        const cardElement = document.createElement('div');
                        cardElement.classList.add('card');
                        cardElement.style.width = '18rem';
                    
                        const imgElement = document.createElement('img');
                        imgElement.classList.add('card-img-top');
                        imgElement.src = artist.image;
                        imgElement.alt = 'Artist image cap';
                    
                        const cardBodyElement = document.createElement('div');
                        cardBodyElement.classList.add('card-body');
                    
                        const titleElement = document.createElement('h5');
                        titleElement.classList.add('card-title');
                        titleElement.textContent = artist.name;
                    
                        const cardTextElement = document.createElement('div');
                        cardTextElement.classList.add('card-text');
                    
                        const linkElement = document.createElement('a');
                        linkElement.href = artist.url;
                        linkElement.textContent = 'Link to artist';
                    
                        cardTextElement.appendChild(linkElement);
                    
                        cardBodyElement.appendChild(titleElement);
                        cardBodyElement.appendChild(cardTextElement);
                    
                        cardElement.appendChild(imgElement);
                        cardElement.appendChild(cardBodyElement);
                    
                        artistElement.appendChild(cardElement);
                    
                        resultsContainer.appendChild(artistElement);
                    }
                }
            }
        };

        xhr.send(formData);
    });
});




