#!/usr/bin/env python

import os

from faster_whisper import WhisperModel

model = None
input_folder = "input_files"

def start_whisper(model_size="large-v2"):
    global model
    if not os.path.exists(input_folder):
        os.mkdir(input_foler)

    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")
    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

def transcribe(path, segmented=False):
    segments, info = model.transcribe(path, beam_size=5)
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    output = ""
    for segment in segments:
        output += segment.text
    return output

def transcribe_segments(path):
    segments, info = model.transcribe(path, beam_size=5)
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    output = map(lambda s: ({
        "text": s.text,
        "start": s.start,
        "end": s.end
    }), segments)
    return output
