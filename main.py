from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eeeeee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
    <form method="post">
        <label>Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <br><br>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query"/>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_text = rotate_string(text, rot)
    return "<h1>" + form.format(encrypted_text) + "</h1>"
@app.route("/")
def index():
    return form.format('')

app.run()
