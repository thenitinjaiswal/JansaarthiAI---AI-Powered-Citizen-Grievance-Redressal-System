from flask import Flask, request, jsonify, render_template
from ibm_watson import NaturalLanguageUnderstandingV1, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, SentimentOptions

app = Flask(__name__)

# Add API KEY here 



# Add API key above 

stt_auth = IAMAuthenticator('')
speech_to_text = SpeechToTextV1(authenticator=stt_auth)
speech_to_text.set_service_url('')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio = request.files['audio']
    stt_result = speech_to_text.recognize(audio=audio, content_type='audio/flac').get_result()

    results = stt_result.get('results', [])
    if not results or not results[0]['alternatives']:
        return jsonify({'error': 'No speech detected'}), 400

    transcript = results[0]['alternatives'][0]['transcript']

    nlu_result = nlu.analyze(
        text=transcript,
        features=Features(emotion=EmotionOptions(), sentiment=SentimentOptions())
    ).get_result()

    emotion = nlu_result['emotion']['document']['emotion']
    sentiment = nlu_result['sentiment']['document']
    srs = int(emotion['anger'] * 40 + emotion['sadness'] * 30 + sentiment['score'] * -30)

    return jsonify({
        'transcript': transcript,
        'emotion': emotion,
        'sentiment': sentiment,
        'srs': srs
    })

if __name__ == '__main__':
    app.run(debug=True)
