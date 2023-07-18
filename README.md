## Description

This is an application that enables a chat-based conversation in English with Swahili videos/audio files using Python. This is made possible by:
- **Pytube** which is a library used to retrieve audio files from Youtube Videos.
- **Whisper API** from OpenAI which is used to transcribe Swahili audio files to Swahili text.
- **Google Translate API** to translate Swahili text to English. 
- **Langchain and OpenAI**  enables the application to generate dynamic responses and engage in chat-based conversations in English.
The application also works for other [languages](https://platform.openai.com/docs/guides/speech-to-text/supported-languages) but I am farmiliar with Swahili hence why I picked the language.

## Limitations
- Takes a while to transcribe Swahili audio files to text specifically 2mins for a 9min audiofile and 13mins for a 46min audiofile as shown in the [notebook](https://github.com/KevKibe/Querying-Transcribed-Text/blob/main/yt_audio_to_chat_swahili.ipynb).
- Google Translate API for translation is not that accurate.
- OpenAI API has a token and request limit and for free trial users. It would be better to use a paid account.

## Usage
You can clone this repository and follow these steps or use a [notebook](https://github.com/KevKibe/Querying-Transcribed-Text/blob/main/yt_audio_to_chat_swahili.ipynb) as demonstrated here. 
- Ensure you have Python installed on your machine (version 3.6 or higher).
- Install the required dependencies by running the following command: `pip install -r requirements.txt`
- Run this  command in your terminal `pip install git+https://github.com/openai/whisper.git ` to get whisper by OpenAI
- Install ffmpeg using instructions from this [site](https://phoenixnap.com/kb/ffmpeg-windows)
- Set up environment variables: Create a `.env` file in the root directory of the project and add your OpenAI API key as follows:
  `OPENAI_API_KEY=your_api_key_here`
- Run the app by running the command `python main.py` in your terminal which will prompt you with the youtube URL input and then proceed to ask for a prompt.
- The application will transcribe the Swahili audio, translate it to English, and engage in a chat-based conversation based on your prompt.
