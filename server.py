''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emot_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion scores
        and dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': "
        f"{anger_score}, 'disgust': {disgust_score}, 'fear': "
        f"{fear_score}, 'joy': {joy_score} and 'sadness': "
        f"{sadness_score}. The dominant emotion is {dominant_emotion}"
    )

if __name__ == "__main__":
    # Executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0",port=5000)
