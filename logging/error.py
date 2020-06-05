from flask import *
from logging import FileHandler,WARNING

app = Flask(__name__)

file_handler = FileHandler('erroring.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

@app.route('/')
def index():
    return 1/0

if __name__ == '__main__':
    app.run()