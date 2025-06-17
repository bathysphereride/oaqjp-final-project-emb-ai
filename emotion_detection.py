import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)
    response_dict = json.loads(response.text)

    emotion_scores = response_dict['emotionPredictions'][0]['emotion']

    anger = emotion_scores['anger']
    disgust = emotion_scores['disgust']
    fear = emotion_scores['fear']
    joy = emotion_scores['joy']
    sadness = emotion_scores['sadness']

    dominant_emotion = max(
        {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness},
        key=lambda k: {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}[k]
    )

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
