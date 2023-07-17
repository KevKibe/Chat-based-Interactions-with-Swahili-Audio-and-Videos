import whisper
from googletrans import Translator
import time


class AudioTranscription:
    def __init__(self, whisp_model):
        self.whisp_model = whisp_model

    def transcribe_audio(self, audio_file):
        audio = whisper.load_audio(audio_file)
        result = self.whisp_model.transcribe(audio)
        transcription = result['text']

        return transcription
    
class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, dest='en'):
        translation = self.translator.translate(text, dest=dest).text
        return translation

