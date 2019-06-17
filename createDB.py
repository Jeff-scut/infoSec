import pymysql

def get_db():
    connect=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='YES',
        database='db_final',
        charset='utf8'
    )
    return connect
    # 建立一个到mysql的连接，存储在g中