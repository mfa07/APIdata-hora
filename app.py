from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/get_datetime', methods=['GET'])
def get_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"A data e hora atual do sistema são: {current_datetime}"

if __name__ == '__main__':
    app.run(debug=True)
