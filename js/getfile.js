document.getElementById('uploadForm').addEventListener('change', function(event) {
    event.preventDefault(); 

    let fileInput = document.getElementById('file-upload');
    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append('files', file);

    document.querySelector('.title2').remove();
    document.querySelector('.button2').remove();
    document.querySelector('.ortitle').remove();

    document.querySelector('body').insertAdjacentHTML('afterend',
    `<div class="boxes">
      <div class="box">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
      </div>
      <div class="box">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
      </div>
      <div class="box">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
      </div>
      <div class="box">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
      </div>
    </div>
    <div class="title2">Hãy kiên nhẫn chờ một chút trong lúc chúng tôi đang tìm bản nhạc dành cho bạn...</div>`)

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

            if (response.data.result == null) {
                console.log('null');
                window.location.href = 'http://' + window.location.hostname + '/test/errorfile.html';
            } else {
                localStorage.setItem('music_info', JSON.stringify(response.data));

                let redirect = new URL('http://' + window.location.hostname + '/test/find.html');
                window.location.href = redirect;
            }
        })
        .catch(function (error) {
            console.log(error);
        });


        
    })
    .catch(function (error) {
        console.log(error);
    });
});