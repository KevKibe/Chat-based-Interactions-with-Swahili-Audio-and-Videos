from get_audio import YouTubeAudioDownloader
from transcribe_translate import AudioTranscription
from transcribe_translate import TextTranslator
from conversation_chain import ConversationChain
import whisper

class MyApp:
    def __init__(self):
        self.whisp_model = whisper.load_model("base")
        self.url = ""
        self.apikey = ""

    def get_user_input(self):
        self.url = input("Enter the YouTube URL: ")
        self.apikey = input("Enter OpenAI API Key")

    def run(self):
        downloader = YouTubeAudioDownloader(self.url)
        downloader.download_audio()
        
        audio_file = "audio.mp3"
        model = AudioTranscription(self.whisp_model)
        transcription = model.transcribe_audio(audio_file)
        
        translator = TextTranslator()
        translated_text = translator.translate_text(transcription, dest='en')
        
        conversation = ConversationChain(translated_text, self.apikey)
        conversation.run_chat()

if __name__ == "__main__":
    app = MyApp()
    app.get_user_input()
    app.run()
