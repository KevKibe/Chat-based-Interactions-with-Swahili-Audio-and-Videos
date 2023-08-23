## Description

This is an application that enables a chat-based conversation in English with Swahili videos/audio files using Python.  <br>
The application also works for other [languages](https://platform.openai.com/docs/guides/speech-to-text/supported-languages) but I am farmiliar with Swahili hence why I picked the language.<br>
This is made possible by:
- **Pytube** which is a library used to retrieve audio files from Youtube Videos.
- **Whisper API** from OpenAI which is used to transcribe Swahili audio files to Swahili text.
- **Google Translate API** to translate Swahili text to English. 
- **Langchain and OpenAI**  enables the application to generate dynamic responses and engage in chat-based conversations in English.



## Limitations
- Takes a while to transcribe Swahili audio files to text specifically 2mins for a 9min-long audiofile and 13mins for a 46min-long audiofile as shown in the [notebook](https://github.com/KevKibe/Querying-Transcribed-Text/blob/main/yt_audio_to_chat_swahili.ipynb).
- Google Translate API for translation is not that accurate.
- OpenAI API has a token and request limit and for free trial users. It would be better to use a paid account.
- The transcription part of the application requires alot of computation. I used a Tesla P100 GPU and it was running at maximum when transcribing the 46min-long audio

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


## Deploying and Containerizing Your Application with Docker

Before you start, make sure you have [Docker](https://www.docker.com/get-started) installed on your system. 

1. **Clone the Repository:** First, clone the repository for your application to your local machine or cloud instance using the following commands:
   ```sh
   git clone https://github.com/KevKibe/Chat-based-Interactions-with-Swahili-Audio-and-Videos.git
   cd Chat-based-Interactions-with-Swahili-Audio-and-Videos
2.**Build the Docker Image:** Replace your-app-name with a suitable name for your application.
   ```
   docker build -t your-app-name .

 ```

## To deploy on an AWS EC2 instance
- Setup an EC2 instance and SSH to the instance.Use this as a [guide](https://www.machinelearningplus.com/deployment/deploy-ml-model-aws-ec2-instance/).
- Run
   ```
  git clone https://github.com/KevKibe/Chat-based-Interactions-with-Swahili-Audio-and-Videos.git
  ```
- Start up [Docker](https://docs.docker.com) and run
  ```
  docker build -t dockerfile .
  ```
- run
  ```
  docker run -e PORT=8080 dockerfile
  ```
- You can now get predictions from
  ```
  http://<ec2-public-IP>:8080/transcribe
  ```

**:zap: I'm currently open for roles in Data Science, Machine Learning, NLP and Computer Vision.**
