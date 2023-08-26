
from flask import Flask,redirect,url_for,render_template,request,jsonify
from flaskext.mysql import MySQL as mysql
import os
app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306  # Change the port if needed
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] = 'testing'

@app.route('/')
def welcome():
    return render_template('index.html')

img=os.path.join('static','images')

@app.route('/')
def home():
    file=os.path.join(img,'logoChatMuse-modified.png')
    return render_template('index.html', image=file)

@app.route('/store_user_input/<string:user_id>', methods=['POST'])
def store_user_input(user_id):
    if request.method == 'POST':
        input_text = request.form.get('user_input')

        if input_text:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (user_id, input_text) VALUES (%s, %s)", (user_id, input_text))
            mysql.connection.commit()
            cur.close()
            return jsonify({"message": "User input saved successfully"})

    return jsonify({"message": "Invalid request"}), 400

if __name__=='__main__':
    app.run(debug=True)