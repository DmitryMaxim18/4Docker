from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@mydb/music', echo=True)
