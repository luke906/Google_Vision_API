import io
import os

from google.cloud import vision
from google.cloud.vision import types
from gtts import gTTS

import pygame

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_vision_api.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'apple.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

"""
for label in labels:
    print(label.description)
"""
def play_music(music_file):
    pygame.init()
    pygame.display.set_mode((200, 100))
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


if __name__ == "__main__":
    speech_file = "speech.mp3"

    print(labels[0].description)
    tts = gTTS(text=labels[0].description, lang='en')
    tts.save(speech_file)
    play_music(speech_file)

