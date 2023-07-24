# Whisper Server

Runs a server in `localhost:5000` that hosts a faster_whisper instance. I recommend you use docker to avoid installing cuda drivers and so on.

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

