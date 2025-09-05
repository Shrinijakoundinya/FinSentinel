from flask import Flask, request, jsonify
import re
app = Flask(__name__)

def classify_message(msg: str):
    score = 0
    text = (msg or '').lower()
    keywords_scam = ['guaranteed','guarantee','get rich','multibagger','insider','buy now','urgent']
    for kw in keywords_scam:
        if kw in text:
            score += 2
    if re.search(r'\b(\d{2,3}%|\d+x)\b', text):
        score += 2
    if score >= 5:
        verdict = 'HIGH_RISK'
    elif score >= 3:
        verdict = 'MEDIUM_RISK'
    else:
        verdict = 'LOW_RISK'
    return verdict, score

@app.route('/analyze', methods=['POST'])
def analyze():
    payload = request.get_json() or {}
    message = payload.get('message','')
    verdict, score = classify_message(message)
    return jsonify({'verdict': verdict, 'score': score, 'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
