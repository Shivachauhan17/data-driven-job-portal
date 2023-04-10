from flask import Flask,render_template,request,jsonify
from database import engine, load_jobs_from_db, load_job_from_db 
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



@app.route("/jobs/<id>/")
def  show_jobs(id):
    job=load_jobs_from_db(id)
    if not job:
        return "not found",404
    return render_template("jobpage.html",job=job)

if __name__== "__main__":
    app.run(debug = True,port=8800,use_reloader=False)
