from flask import Flask, render_template, requests
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route('/emotiondetector')
def sent_to_analyze():
    """
    Function to obtain the input from the user, using it within the emotion_detectr() function
    to make use of the emotion detector app with Watson NLP library. Getting this response
    we extract the specific data and sending it to the client.
    """
    text_to_analyze = requests.args.get('TextToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    
    if dominant_emotion is None:
        return 'Invalid input! Try again.'
    return f"For the given statement, the system response is {response[0:6]}. The dominant emotion is {dominant_emotion}"


@app.route('/')
def render_index_page():
    """
    This function renders the the main application over the Flask channel
    """
    return render_template("index.html")

if __main__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

