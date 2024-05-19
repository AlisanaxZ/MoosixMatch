let title = document.querySelector(".music_name");
// let artist = document.querySelector(".artist");
let image = document.querySelector(".artwork");

// let preview = document.querySelector(".preview");

let amLink = document.querySelector(".apple_music");
let spLink = document.querySelector(".spotify");
let moreLink = document.querySelector(".more_platform");

let formData = new FormData();

let url = new URL(window.location.href);

console.log(formData);

axios.get('http://127.0.0.1:5000/get-music', {
    params: {
        location: url.searchParams.get('location'),
    }
})
.then(function (response) {
    music = response.data.result;
    console.log(music);
    
    title.innerText = music.title;
    // artist.innerText = music.artist;

    let artwork = music.spotify.album.images[0].url;
    // artwork = artwork.replace('{w}', '315') //height of artwork
    // artwork = artwork.replace('{h}', '560') //weight of artwork
    console.log(artwork);
    image.src = artwork;

    // let audio_el = "<audio controls> <source src='" + music.music.spotify.preview_url + "' class='preview' type='audio/mpeg'> Your browser does not support the audio element. </audio>";
    // preview.innerHTML = audio_el; 

    amLink.href = music.apple_music.url;
    spLink.href = music.spotify.external_urls.spotify;
    moreLink.href = music.song_link;                
})
.catch(function (error) {
    console.log(error);
});