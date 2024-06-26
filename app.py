# app.py
from flask import Flask, render_template
from modules.module1.routes import module1
from modules.module2.routes import module2
from modules.module3.routes import module3
from modules.module4.routes import module4
from modules.module5.routes import module5
from modules.module6.routes import module6
from modules.module7.routes import module7
from modules.module8.routes import module8
from modules.chatbot import chatbot_bp

from navutils import register_context_processors


app = Flask(__name__)

app.register_blueprint(module1)
app.register_blueprint(module2)
app.register_blueprint(module3)
app.register_blueprint(module4)
app.register_blueprint(module5)
app.register_blueprint(module6)
app.register_blueprint(module7)
app.register_blueprint(module8)

app.register_blueprint(chatbot_bp)

register_context_processors(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data-exploration')
def data_exploration():
    # Add your data exploration logic here
    return render_template('data_exploration.html')

if __name__ == '__main__':
    app.run()
