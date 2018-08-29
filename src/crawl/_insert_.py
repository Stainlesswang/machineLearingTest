'''
新建一个数据库连接,由于多次的打开关闭数据连接,已经弃用
'''
import pymysql
def insert(ops=[]):
        # 打开数据库连接
    db = pymysql.connect("10.10.160.5","java_admin","GeHa5MT3I4tyqS0oRV30SVP3","knowledge_manage" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    n=len(ops)
    cursor.executemany('insert into ent_people_info (name, photo) values (%s, %s)', ops[0:n])
    cursor.close()
    db.commit()
    db.close()
    print ('成功'+str(ops)+' success')
