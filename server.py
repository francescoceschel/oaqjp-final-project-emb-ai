from flask import Flask, request

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detector(textToAnalyze):
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(textToAnalyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = max(result, key = result.get)

    return f'For the given statement, the system response is "anger": {anger}, "disgust": {disgust}, "fear": {fear}, "joy": {joy}, and "sadness": {sadness}. The dominant emotion is {dominant_emotion}'

if __name__ == '__main__':
    app.run(debug = True)