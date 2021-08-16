from flask import Flask, render_template

from controllers.Admin_controller import admin_blueprint
from controllers.admin_actions_controller import admin_actions_blueprint


app = Flask(__name__)

app.register_blueprint(admin_blueprint)
app.register_blueprint(admin_actions_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)