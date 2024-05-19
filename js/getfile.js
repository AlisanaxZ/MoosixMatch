document.getElementById('uploadForm').addEventListener('change', function(event) {
    event.preventDefault(); 

    let fileInput = document.getElementById('file-upload');
    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append('files', file);

    axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
           'Content-Type': 'multipart/form-data',
           withCredentials: true
        }
    })
    .then(function (response) {
        console.log(response);
        axios.get('http://127.0.0.1:5000/get-music', {
            params: {
                location: response.data,
            }
        })
        .then(function (response) {
            console.log(response);

            if (response.result == null) {
                window.location.href = 'http://' + window.location.hostname + '/test/errorfile.html'
            }
        })
        .catch(function (error) {
            console.log(error);
        });


        let redirect = new URL('http://' + window.location.hostname + '/test/find.html');
        redirect.searchParams.append('location', response.data);
        // window.location.href = redirect;
    })
    .catch(function (error) {
        console.log(error);
    });
});