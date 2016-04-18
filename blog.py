from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_main():
    return 'aloha'
    
    
    
if __name__ == '__main__':
    app.run(port=4000)