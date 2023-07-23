from flask import Flask, request, jsonify
from get_audio import YouTubeAudioDownloader
from transcribe_translate import AudioTranscription, TextTranslator
from conversation_chain import ConversationChain
from main import MyApp
import whisper

app = Flask(__name__)


@app.route('/api/process_audio', methods=['POST'])
def process_audio():
    data = request.get_json()
    youtube_url = data.get('youtube_url')

    if youtube_url:
        app_instance = MyApp()
        response = app_instance.process_audio(youtube_url)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request, missing "youtube_url" parameter.'}), 400

if __name__ == "__main__":
    app.run(debug=True)