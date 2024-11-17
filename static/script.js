document.getElementById('analyzeButton').addEventListener('click', function() {
    const sequence = document.getElementById('sequenceInput').value;
    const position = parseInt(document.getElementById('mutationPosition').value);
    const mutation = document.getElementById('mutationType').value.toUpperCase();

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sequence: sequence,
            position: position,
            mutation: mutation
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('originalSequence').innerText = data.original;
        document.getElementById('editedSequence').innerText = data.edited;
        document.getElementById('originalProtein').innerText = data.original_protein;
        document.getElementById('editedProtein').innerText = data.edited_protein;
    })
    .catch(error => console.error('Error:', error));
});
