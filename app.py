from flask import Flask, render_template
from modules.module1.routes import module1
from modules.module2.routes import module2
from modules.module3.routes import module3
from modules.module4.routes import module4
from modules.module5.routes import module5

app = Flask(__name__)

app.register_blueprint(module1)
app.register_blueprint(module2)
app.register_blueprint(module3)
app.register_blueprint(module4)
app.register_blueprint(module5)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data-exploration')
def data_exploration():
    # Add your data exploration logic here
    return render_template('data_exploration.html')

if __name__ == '__main__':
    app.run()
