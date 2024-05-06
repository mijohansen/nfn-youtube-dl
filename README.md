Det oppdaterte finner man her

``` 
https://github.com/yt-dlp/yt-dlp
```

```bash
flask --app hello run
```

Laste ned disse pb-filene

```bash
wget -q  https://essentia.upf.edu/models/feature-extractors/discogs-effnet/discogs-effnet-bs64-1.pb
wget -q  https://essentia.upf.edu/models/classification-heads/genre_discogs400/genre_discogs400-discogs-effnet-1.pb
```

```bash
pipx install flask
pipx install yt_dlp
pipx install urllib3
pipx install functions-framework
pipx install google-cloud-storage

pipx install essentia
pipx install essentia-tensorflow
```

mac os x

```bash 
brew install pipx
brew install ffmpeg
brew install ffprobe
brew install black
pipx ensurepath
```

```bash
yt-dlp --audio-format mp3 -o "test.mp3" https://www.youtube.com/watch?v=7E-cwdnsiow
```

### Analyse

Eksempel her: https://github.com/cobanov/audio-genre-detection/tree/main

### Deployment

From a starting point this service seems.

https://github.com/GoogleCloudPlatform/functions-framework-python


