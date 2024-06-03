import os
from flask import Flask

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'El ordenador se está apagando...'

def shutdown_server():
    if os.name == 'nt':
        os.system('shutdown /s /t 1')
    else:
        os.system('sudo shutdown -h now')

if __name__ == '__main__':
    app.run(debug=True)
