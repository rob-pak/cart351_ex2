from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task-1: GET REQUEST
@app.route("/t1")
def t1():
    return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():
    #fill me in :
    #replace the empty space to be url encoded
    imgFromNasa = request.args["query"]
    imgFromNasa = imgFromNasa.replace(' ', '%20')

    # api request, limit to first image
    url = f"https://images-api.nasa.gov/search?q={imgFromNasa}&media_type=image&page_size=1"
    response = requests.get(url)
    data = response.json()
    description = ""
    images = data["collection"]["items"]
    print(images)
    if images:
        description = images[0]["data"][0]["description"]
        imgFromNasa = images[0]["links"][0]["href"]
    
    return render_template("t1.html",
                              have_results = True,
                              description=description,
                              imgPath = imgFromNasa
                           )
    pass

#*************************************************
# #Task-2: GET REQUEST
# @app.route("/t2")
# def t2():
#     return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():
 #fill me in :
#  return render_template("t2.html",images=encodedImageLinks)
    pass
#*************************************************

#run
app.run(debug=True)