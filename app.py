from flask import Flask,render_template,request,jsonify
from database import engine
from sqlalchemy import text
#__name__ refers to how a particular script is invoked
app=Flask(__name__)


#to contructing  a url and if that pertucular url accessed then the function 
# below decorator will be executed

def load_job_from_db():
    jobs=[]
    with engine.connect() as conn:
        result=conn.execute(text("select * from jobs"))
        for row in result.mappings().all():
            jobs.append(dict(row))
    return jobs
@app.route('/')
def hello():
    jobs=load_job_from_db()
    return render_template('index.html',jobs=jobs)

"""@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)"""
if __name__== "__main__":
    app.run(debug = True,port=8800,use_reloader=False)
