from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

def check_website(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    target_url = request.args.get('url', '')
    
    if not target_url:
        return jsonify({"online": False, "error": "URL manquante"})
        
    status = check_website(target_url)
    return jsonify({"online": status})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
