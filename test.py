from sqlalchemy import create_engine

# Replace the placeholders with your actual database credentials
username = 'sa'
password = 'MyPass@1'
server = 'localhost,1433'
dbname = 'imageDB'

engine = create_engine(f'mssql+pymssql://{username}:{password}@{server}/{dbname}')

# Test the connection by executing a simple query
with engine.connect() as connection:
    result = connection.execute('SELECT 1')
    print(result.fetchone())
