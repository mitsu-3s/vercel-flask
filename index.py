from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/next', methods=['GET'])
def next():
   return render_template('next.html')

# if __name__ == '__main__':
#     app.run()