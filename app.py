from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

def check_website(url):
    try:
        # S'assurer que l'URL commence par http:// ou https:// pour éviter les plantages
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        response = requests.get(url, timeout=5)
        # Vérifie si le code de statut indique un succès (200 OK)
        return response.status_code == 200
    except requests.RequestException:
        # Capture spécifiquement les erreurs réseau, de timeout ou de DNS
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    # Récupérer l'adresse soumise par l'utilisateur dans l'interface graphique
    target_url = request.args.get('url', '')
    
    if not target_url:
        return jsonify({"online": False, "error": "URL manquante"})
        
    status = check_website(target_url)
    return jsonify({"online": status})

if __name__ == '__main__':
    app.run(debug=True, port=5001)