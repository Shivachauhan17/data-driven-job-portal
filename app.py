from flask import Flask,render_template,request
#__name__ refers to how a particular script is invoked
app=Flask(__name__)

#to contructing  a url and if that pertucular url accessed then the function 
# below decorator will be executed
@app.route('/')
def hello():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug = True,port=8080,use_reloader=False)
