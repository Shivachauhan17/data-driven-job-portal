from sqlalchemy import create_engine, text
url="mysql+pymysql://t99w2dtbc0d55x11y68f:pscale_pw_Li8gaYzYmvnq7cXXo5AD19SHKofq4B8MmVYWFH7okLU@aws.connect.psdb.cloud/career_openings?charset=utf8mb4"

engine=create_engine(url,connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    })


with engine.connect() as conn:
    jobs=[]

    result=conn.execute(text("select * from jobs"))
    #print(type(result))
    #print(type(result.all()))
    for row in result.mappings().all():
        jobs.append(dict(row))
print(jobs)
