import requests, json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    my_object = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = my_object, headers = HEADER)
    
    failure_response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
            }
    # Error handling:
    if response.status_code == 400:
        return failure_response
    try:
        formatted_response = json.loads(response.text)
        print('response formatted.')
    except json.JSONDecodeError:
        return failure_response
    if 'emotionPredictions' not in formatted_response or not formatted_response['emotionPredictions']:
        return failure_response
                
    filtered_response = formatted_response['emotionPredictions'][0]['emotion']   # extracting all emotions key-value pairs
    # efficient 2nd approach using max():
    dominant_emotion = max(filtered_response, key = filtered_response.get)   
    filtered_response.update({ "dominant_emotion": dominant_emotion })

    return filtered_response





"""
First Aproach for emotion_detector

    response = requests.post(URL, json = my_object, headers = HEADER)
    formatted_response = json.loads(response.text)
    print("response formatted.")
    
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    filtered_response = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            }
    
    # 1st approach for obtaining dominant emotion value
    dominant_emotion = ""
    dominant_score = 0
    for key, value in filtered_response.items():
        if dominant_score < value:
            dominant_score = value
            dominant_emotion = key
            
    filtered_response.update({ "dominant_emotion": dominant_emotion })
    return filtered_response

--------------------------------------------------------------
(Raw JSON response from Watson NLP)

  "emotionPredictions": [
    {
      "emotion": {
        "anger": 0.0132405795,
        "disgust": 0.0020517302,
        "fear": 0.009090992,
        "joy": 0.9699522,
        "sadness": 0.054984167
      },
      "target": "",
      "emotionMentions": [
        {
          "span": {
            "begin": 0,
            "end": 26,
            "text": "I love this new technology"
          },
          "emotion": {
            "anger": 0.0132405795,
            "disgust": 0.0020517302,
            "fear": 0.009090992,
            "joy": 0.9699522,
            "sadness": 0.054984167
          }
        }
      ]
    }
  ],
  "producerId": {
    "name": "Ensemble Aggregated Emotion Workflow",
    "version": "0.0.1"
  }
}
"""
