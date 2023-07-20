from sqlalchemy import create_engine
import os

db_connection= os.environ("db_details")

engine = create_engine(db_connection,
                      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
