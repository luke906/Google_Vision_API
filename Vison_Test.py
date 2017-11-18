import io
import os

from google.cloud import vision
from google.cloud.vision import types
from gtts import gTTS
from pygame import mixer

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

mixer.init()

for label in labels:
    print(label.description)
    tts = gTTS(text=label.description, lang='en')
    tts.save("good.mp3")
    mixer.music.load("good.mp3")
    mixer.music.play()

