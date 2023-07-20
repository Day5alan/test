from sqlalchemy import create_engine
import os

db_connection= os.environ['DB_DETAILS']

engine = create_engine(db_connection,
                      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
