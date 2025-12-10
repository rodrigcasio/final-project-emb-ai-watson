"""
Executing this server, it deploys the web application using flask.
It recieves the response from the service of Watson NLP Library 
with the imported "emotion_detector". 
This service is used by obtaning the input from the user in the client side, 
and place this input as an argument for "emotion_detector()". 
Lastly, we parse the obtained data into a list from 
the dict returned by the "emotion_detector()" function
Pylint test grade: 9.52/10.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_to_analyze():
    """
    Function to obtain the input from the user, using it within the emotion_detectr() 
    function to make use of the emotion detector app with Watson NLP library. 
    Getting this response, we extract the specific data and sending it to the client.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == '':
        return "Invalid text! Please try again!."
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.pop("dominant_emotion")
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    formatted_scores = []
    for key, value in response.items():
        formatted_scores.append(f"'{key}': {value}")
    # or formatted_scores = [f"'{emotion}': {score}" for emotion, scores in response.items()]
    scores_string = ', '.join(formatted_scores)
    final_string = f"For the given statement, the system response is {scores_string}. The dominant emotion is {dominant_emotion}"
    return final_string

@app.route('/')
def render_index_page():
    """
    This function renders the the main application over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
