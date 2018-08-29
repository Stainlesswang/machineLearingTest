# _*_ coding : UTF-8 _*_
'''
Created on 2018年7月10日
使用数据库连接池来实现数据库工具类
@author: Allen Wong
'''
from dbConnection import Config
import importlib
from DBUtils.PooledDB import PooledDB
class MySql():
    '''
    Mysql数据库对象,负责产生连接池,并且可以释放连接资源等
    '''
    #连接池对象
    _pool = None
    
    def __init__(self):
        #数据库构造函数,从连接池取出对象,并且 返回游标cursor\
        self._conn=MySql.__getConn(self)
        self._cursor = self._conn.cursor()
        
    @staticmethod
    def __getConn(self):
        '''
        @summary: 静态方法,从连接池中取出连接
        @return:  pymysql.connections.Connection
        '''
        db_creator = importlib.import_module("pymysql")
        if MySql._pool==None:
            _pool=PooledDB(creator=db_creator, mincached=1, maxcached=20,
                              host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPASSWORD,
                              db=Config.DBNAME, use_unicode=False, charset=Config.DBENCODE)
        return _pool.connection()
    
    def getAll(self,sql,param=None):
        if param is None:
            count=self._cursor.execute(sql)
        else:
            count=self._cursor.execute(sql,param)
        if count>0:
            result=self._cursor.fatchall()
        else:
            result=False
        return result
    
    def getOne(self,sql,param=None):
        if param is None:
            count=self._cursor.execute(sql)
        else:
            count=self._cursor.execute(sql,param)
        if count>0:
            result=self._cursor.fatchone()
        else:
            result=False
        return result
    
    def getMany(self,sql,num,param=None):
        if param is None:
            count=self._cursor.execute(sql)
        else:
            count=self._cursor.execute(sql,param)
        if count>0:
            result=self._cursor.fatchMany(num)
        else:
            result=False
        return result
    
    def insertOne(self,sql,value):
        self._cursor.insert(sql,value)
        return self.__getInsertId()
    
    def insertMany(self, sql, values):
        
        count = self._cursor.executemany(sql, values)
        
        return count
 
    def __getInsertId(self):
        """ 
                                获取当前连接最后一次插入操作生成的id,如果没有则为０ 
        """
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']
 
    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count
 
    def update(self, sql, param=None):
        """ 
        @summary: 更新数据表记录 
        @param sql: ＳＱＬ格式及条件，使用(%s,%s) 
        @param param: 要更新的  值 tuple/list 
        @return: count 受影响的行数 
        """
        
        return self.__query(sql, param)
 
    def delete(self, sql, param=None):
        """ 
        @summary: 删除数据表记录 
        @param sql: ＳＱＬ格式及条件，使用(%s,%s) 
        @param param: 要删除的条件 值 tuple/list 
        @return: count 受影响的行数 
        """
        return self.__query(sql, param)
 
    def begin(self):
        """ 
        @summary: 开启事务 
        """
        self._conn.autocommit(0)
 
    def end(self, option='commit'):
        """ 
        @summary: 结束事务 
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()
 
    def dispose(self, isEnd=1):
        """ 
        @summary: 释放连接池资源 
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self._cursor.close()
        self._conn.close()
