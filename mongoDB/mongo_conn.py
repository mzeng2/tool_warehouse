import pymongo
import pandas as pd

def get_connect_db(conn,db_name):
    """建立 mongoDB 连接"""
    myclient = pymongo.MongoClient(conn)

    db_list = myclient.list_database_names()

    for dbnames in db_list:
        if dbnames == db_name:
            db_connect = myclient.get_database(dbnames)
            print ('connected to -->',dbnames)

            return db_connect

def mongo2df(cols,value,table_name,conn):
    """mongoDB返回结果转成数据框"""
    search_key = {}
    search_key[cols] = value
    res = conn[table_name].find(search_key)
    
    df_out = pd.DataFrame(list(res))
    print('read data complete>>>>>')
    print(df_out.head())
    return df_out
