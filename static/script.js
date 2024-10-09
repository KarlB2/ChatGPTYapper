document.getElementById('speakingButton').addEventListener('click', function() {
    fetch('/listen', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => response.json())
      .then(data => {
          document.getElementById('responseText').textContent = data.response;
      });
});