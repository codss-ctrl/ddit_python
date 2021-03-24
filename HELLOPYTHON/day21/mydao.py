import cx_Oracle

class MyDao:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        
    def myselect(self):
        rs = self.cs.execute('select col01,col02,col03 FROM sample')
        list = []
        for record in rs:
            list.append({'col01':record[0],'col02':record[1],'col03':record[2]})
        return list

        
    def myinsert(self,col01,col02,col03):
        sql = "insert into sample (col01,col02,col03) values (:1,:2,:3)"
        self.cs.execute(sql,(col01,col02,col03))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,col01,col02,col03):
        sql = "update sample set col02=:1,col03=:2 where col01=:3"
        self.cs.execute(sql,(col02,col03,col01))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def mydelete(self,col01):
        sql = "delete from sample where col01 = :1"
        self.cs.execute(sql,(col01,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def __del__(self):
        self.cs.close()
        self.conn.close()
        

if __name__ == '__main__':
    dao = MyDao()
    cnt = dao.mydelete('1')
    print("cnt",cnt)
    
#     list = dao.myselect()
#     print(list)

            