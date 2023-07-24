# Whisper Server

Runs a server in `localhost:5000` that transcribes an audio file with `faster_whisper`. I recommend running `whisper-server` with docker to avoid dealing with cuda, venvs, and so on.

## Running with docker

Build the docker image:
``` sh
docker build -t whisper-server .
```

Run it:
``` sh
docker run --gpus all -it -p 5000:5000 whisper-server
```

Test it:
``` sh
curl -X POST -F "file=@/path/input.wav" http://localhost:5000/upload
```

