document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    let fileInput = document.getElementById('fileInput');
    let file = fileInput.files[0];

    if (!file) {
        document.getElementById('result').innerText = 'Chọn file';
        return;
    }

    let formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Có lỗi';
    });
});