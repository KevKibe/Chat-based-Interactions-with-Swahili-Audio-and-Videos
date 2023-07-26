import requests

# Replace this URL with the address where your Flask app is running
BASE_URL = "http://127.0.0.1:5000"

def test_transcribe_audio():
    url = "https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID"
    data = {"url": url}

    response = requests.post(f"{BASE_URL}/transcribe", json=data)
    if response.status_code == 200:
        result = response.json()["result"]
        print("Chat conversation result:")
        print(result)
    else:
        print("Error occurred:")
        print(response.json())

if __name__ == "__main__":
    test_transcribe_audio()
