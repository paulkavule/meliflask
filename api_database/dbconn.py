import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
import urllib

try:
    # ApiSQLEngine  = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn_str))
    engine  = create_engine('sqlite:///appdb.db', echo=True)
    appConn = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    ApiDb = declarative_base()
    # appconn = engine.connect()

    print("Passed")
except:
    print("Failed!")


# def getDatabase():

#     try:
#         db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

#         yield db
#     except Exception as ex:
#         print(ex.args[0])
#     finally:
#         db.close()
