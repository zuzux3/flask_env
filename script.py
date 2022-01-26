from flask import Flask

app = Flask(__name__)

@app.route('/Zuzu')

def index():
    return "Zuzanna Tarazewicz, IST3, 116954, Grupa IV"

if __name__ == '__main__':
    app.run(debug = True)