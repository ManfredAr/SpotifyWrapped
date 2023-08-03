document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(event.target); // 'this' refers to the form element with ID 'search'
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/genre/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText); // Parse the JSON response
                    const genres = response.genres; // Extract the 'tracks' array from the response

                    // Clear any existing content on the screen
                    const genresContainer = document.getElementById('genres');
                    genresContainer.innerHTML = '';

                    for (const genre of genres) {
                        const genreElement = document.createElement('div');
                        genreElement.classList.add('genre');
                      
                        const titleElement = document.createElement('h1');
                        titleElement.textContent = genre[0];
                      
                        genreElement.appendChild(titleElement);
                      
                        genresContainer.appendChild(genreElement);
                    }
                }
            }
        };

        xhr.send(formData);
    });
});




