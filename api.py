from flask import Flask, request, jsonify
from main import MyApp

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "Invalid data. Missing 'url' parameter."}), 400

    app_instance = MyApp()
    result = app_instance.process_url(url)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))