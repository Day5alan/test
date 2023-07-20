from sqlalchemy import create_engine


db_connection="mysql+pymysql:// tvl0a0ivi6kdmnl2waja:pscale_pw_tQ8dkUKS4DsuTyJbV7NQCDYL0SwPtI1d8Mh7hzdFJ2l@aws.connect.psdb.cloud/narutooo?charset=utf8mb4"

engine = create_engine(db_connection, 
                      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
        })


