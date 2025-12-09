import requests, json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    my_object = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json = my_object, headers = HEADER)
    formatted_response = json.loads(response.text)
       
    filtered_response = formatted_response['emotionPredictions'][0]['emotion']
    
    # efficient approach:
    dominant_emotion = max(filtered_response, key = filtered_response.get)
    """
    1st approach: (works)
    dominant_emotion = ""
    dominant_score = 0
    for key, value in filtered_response.items():
        if dominant_score < value:
            dominant_score = value
            dominant_emotion = key
    """
    filtered_response.update({ "dominant_emotion": dominant_emotion })
    return filtered_response

"""
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
