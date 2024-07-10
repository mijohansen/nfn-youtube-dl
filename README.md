Det oppdaterte finner man her

``` 
https://github.com/yt-dlp/yt-dlp
```

```bash
flask --app hello run
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
brew install killport
pipx ensurepath
```

```bash
yt-dlp --audio-format mp3 -o "test.mp3" https://www.youtube.com/watch?v=7E-cwdnsiow
```

### Analyse

Eksempel her: https://github.com/cobanov/audio-genre-detection/tree/main

### Run cloud functions locally

On mac `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`

```bash
killport 7475 && functions-framework --target=handler --port=7475
```

### Deployment

From a starting point this service seems.

https://github.com/GoogleCloudPlatform/functions-framework-python

```bash
gcloud functions deploy handler --gen2 --runtime python312 --trigger-http --memory 1024 --project notefornote
gcloud functions call handler --project notefornote
```

### vendored deps

FML moment
https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python38

```bash
python3 -m pip download -r requirements.txt --only-binary=:all: \
-d deps \
--python-version 3.12.3 \
--platform manylinux2014_x86_64 \
--implementation cp
```

### Architecture

The analysis service is booted with a token that make it possible to talk with a sentral server.

#### Download service

* written in python.
* could be dumb, that is orchestrated from a sentral point
* sentral server could hit this server with all it need to 