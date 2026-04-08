import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP URL
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input jason
    Input_jason = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request
    response = requests.post(URL, json=Input_jason, headers=Headers)

    # Convert response text into a dictionary
    df_response = json.loads(response.text)
    
    # Extract the required set of emotions and scores
    emotions = df_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the required format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }