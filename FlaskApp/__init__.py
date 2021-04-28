from flask import Flask, request, Markup, url_for
from flask import render_template as rt
import mysql.connector
import boto3
import os

app = Flask(__name__)

@app.route("/")
def home():
    return rt("Home.html")

@app.route("/<nav>")
def nav(nav):
    return rt("{}".format(nav))

@app.route("/mydb", methods=["POST"])
def db():
    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")
        comment = request.form.get("comment")

        mydb = mysql.connector.connect(
        host="localhost",
        user="######",
        password="######",
        database="mydatabase"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO comments VALUES (%s, %s, %s)"
        val = (name, time, comment)

        mycursor.execute(sql, val)
        mydb.commit()
        texttospeech(comment, time)
        return select()

@app.route("/getdata")
def getdata():
    return select()
  
def select():
    mydb = mysql.connector.connect(host="localhost", user="######", password="######", database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM comments")
    myresult = mycursor.fetchall()
    output = "<h3>Comments will show up here</h3>"
    myresult.reverse()
    usericon = url_for('static',filename='img/profile.png')
    soundicon = url_for('static',filename='img/sound.jpg')

    for row in myresult:
        name, time, comment = row
        output += """<div id='box'><img id='uicon' src='{0}'/><text id='name'>{1}</text><text id='time'>{2}</text>
        <img id='sicon' src='{3}' onclick="speech('{2}')"/><p id='comment'>{4}</p></div><br>""".format(usericon,name,time,soundicon,comment)
    output = Markup(output)
    return rt("dboutput.html", output = output)

def texttospeech(comment, time):
    po = boto3.client('polly', aws_access_key_id="######", aws_secret_access_key="##########", region_name='ap-south-1')
    res = po.synthesize_speech(Text=comment, OutputFormat='mp3', VoiceId='Aditi')
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
    filepath = "static/speech/{}.mp3".format(time)
    json_url = os.path.join(PROJECT_ROOT, filepath)
    with open(json_url, 'wb') as file:
        file.write(res['AudioStream'].read())
    
 if __name__ == "__main__":
    app.run(host="0.0.0.0")
