from sqlalchemy import create_engine, text, select
url="mysql+pymysql://t99w2dtbc0d55x11y68f:pscale_pw_Li8gaYzYmvnq7cXXo5AD19SHKofq4B8MmVYWFH7okLU@aws.connect.psdb.cloud/career_openings?charset=utf8mb4"

engine=create_engine(url,connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    })

def load_job_from_db():
    jobs=[]
    with engine.connect() as conn:
        result=conn.execute(text("select * from jobs"))
        for row in result.mappings().all():
            jobs.append(dict(row))
    return jobs

def load_jobs_from_db(id):
    with engine.connect() as conn:
        query="SELECT * FROM jobs WHERE id ="
        selection_value=str(id)
        query=query+selection_value
        result=conn.execute(text(query))
        rows=result.mappings().all()
        if len(rows)==0:
            return None
        else:
            return dict(rows[0])