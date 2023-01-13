#!/usr/bin/env python3

import sys
from pytube import YouTube
from moviepy.editor import *


def main():
    stream = sys.argv[1]

    yt = YouTube(stream)

    video = yt.streams.filter(only_audio=True).first().download()
    audio = video.split('.')[0] + '.mp3'

    AudioFileClip(video).write_audiofile(audio)


if __name__ == '__main__':
    main()
