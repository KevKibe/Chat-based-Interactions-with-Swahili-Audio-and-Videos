from get_audio import YouTubeAudioDownloader
from transcribe import AudioTranscription
from transcribe import TextTranslator
from conversation_chain import ConversationChain
import whisper
whisp_model = whisper.load_model("base")

url = "https://youtu.be/graduE4S9Og?t=439"
downloader = YouTubeAudioDownloader(url)
downloader.download_audio()

audio_file = "/kaggle/working/audio2.mp3"
model = AudioTranscription(whisp_model)
transcription= model.transcribe_audio(audio_file)

translator = TextTranslator()
translated_text= translator.translate_text(transcription, dest='en')

translated_text = translated_text
conversation = ConversationChain(translated_text)
conversation.run_docbot()
