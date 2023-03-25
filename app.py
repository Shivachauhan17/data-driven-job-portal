from flask import Flask,render_template,request,jsonify
#__name__ refers to how a particular script is invoked
app=Flask(__name__)

Jobs=[
    {
    "id":1,
    "title":"data scientist",
    "location":"hydrabad",
    "salary":"10,00,000"
    },
    {
    "id":2,
    "title":"data analyst",
    "location":"Noida",
    "salary":"9,00,000"
    },
    {
    "id":3,
    "title":"software engineer",
    "location":"remote",
    "salary":"11,00,000"
    }
]
#to contructing  a url and if that pertucular url accessed then the function 
# below decorator will be executed
@app.route('/')
def hello():
    return render_template('index.html',jobs=Jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(Jobs)
if __name__== "__main__":
    app.run(debug = True,port=8000,use_reloader=False)
