from flask import Flask,render_template,request
import os
import json
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads' # Or os.path.join(app.instance_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task: CAPTURE & POST & FETCH & SAVE
@app.route("/t2")
def t2():
    filePath = "files/p5Data.json"
    last = None
    if os.path.exists(filePath):
        with open(filePath, "r") as jsonFile:
            theList = json.load(jsonFile)
            if len(theList) > 0:
                last = theList[-1]
    return render_template("t2.html", last=last)

# Exercise - 4 fetch request
@app.route("/postDataFetch", methods=['POST'])
def postDataFetch():
    hour = request.form.get("hour")
    moon = request.form.get("moon")
    app.logger.info(hour)
    app.logger.info(moon)
    filePath = "files/p5Data.json"

# Exercise - 6 send data to JSON
    with open(filePath, "w") as jsonFile:
        json.dump([{"hour": hour, "moon": moon}], jsonFile, indent=4)

# Exercise - 5 send data to the text file
    with open("files/data.txt", "w") as textFile:
        textFile.write(f"hour: {hour}\nmoon: {moon}\n")

    return {"inFile": "data written"}


# route to update live
@app.route("/latestHour")
def latestHour():
    filePath = "files/p5Data.json"
    if os.path.exists(filePath):
        with open(filePath, "r") as jsonFile:
            theList = json.load(jsonFile)
            if len(theList) > 0:
                return theList[-1]
    return {"hour": "—", "moon": "—"}

#*************************************************
#run
app.run(debug=True)