import pymysql
import traceback
import time

class mysqlClass():
    db = None
    host = 'localhost'
    usr = 'root'
    pwd = ''
    dbname = 'pythondb'
    port = 3306
    charset = 'utf8'

    def showVersion(self):
        db = pymysql.connect(self.host, self.usr, self.pwd, self.dbname)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("version: %s" % data)
        db.close()

    def openDB(self):
        self.db = pymysql.connect(
            host = self.host,
            user = self.usr,
            passwd = self.pwd,
            db = self.dbname,
            charset = self.charset
        )
    def closeDB(self):
        self.db.close()
    def excuteSQL(self, str_sql):
        self.openDB()
        try:
            cursor = self.db.cursor()
            cursor.execute(str_sql)
            cursor.close()
            self.db.commit()
        except:
            self.db.rollback()
            traceback.print_exc()
        self.closeDB()

    def Insert_2345City(self, data_dict):
        self.openDB()

        # 字符串换行 加 '\'
        # 插入数据
        sql_insert = "INSERT INTO 2345city(sName,lName,number)\
         VALUES (\'%s\',\'%s\',%d)"%(data_dict['sName'],data_dict['lName'],data_dict['number'])
        
        try:
            cursor = self.db.cursor()
            cursor.execute(sql_insert)
            cursor.close()

            self.db.commit()
        except:
            print('insert error:',data_dict)
            self.db.rollback()
            traceback.print_exc()
        self.closeDB()

    def Insert_2345history(self, cid, data_dict):
        self.openDB()

        time_str = time.strftime('%Y-%m-%d %H:%M:%S')
        sql_history = "INSERT INTO 2345history(城市编号,ymd,bWendu,yWendu,tianqi,fengxiang,fengli,aqi,aqiInfo,aqiLevel,timeStr)\
         VALUES(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%(cid, data_dict['ymd'],
         data_dict['bWendu'],data_dict['yWendu'],data_dict['tianqi'],data_dict['fengxiang'],data_dict['fengli'],
         data_dict['aqi'],data_dict['aqiInfo'],data_dict['aqiLevel'],time_str)

        try:
            cursor = self.db.cursor()
            cursor.execute(sql_history)
            cursor.close()

            self.db.commit()
        except:
            print('insert error:',data_dict)
            self.db.rollback()
            traceback.print_exc()

        self.closeDB()
        