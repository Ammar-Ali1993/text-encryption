import sqlite3


class DB:
    def __init__(self, dbname="db.sqlite"):
        self.dbname = dbname
        try:
            self.conn = sqlite3.connect(dbname)
        except sqlite3.Error as e:
           print('DB falied to connect sqlite3 error')
        self.setupTable()
        self.setupDefaultProperties()

    def setupTable(self):
        stmt = "CREATE TABLE IF NOT EXISTS settings (id integer PRIMARY KEY, type text not null , value text not null)"
        self.conn.execute(stmt)
        self.conn.commit()

    def addPropery(self, type, value):
        stmt = "INSERT INTO settings (type, value) VALUES (?,?)"
        args = (type, value)
        try:
            self.conn.execute(stmt, args)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print('insert failed, DB error')

    def setupDefaultProperties(self):

        sectionsAvailable = self.getPropery('sections')
        if not sectionsAvailable:
            self.addPropery('sections','10')

        behavriorAvailable = self.getPropery('behavior')
        if not behavriorAvailable:
            self.addPropery('behavior', '1010')

        behavriorAvailable = self.getPropery('behavior')
        if not behavriorAvailable:
            self.addPropery('behavior', '1010')

        mapAvailable = self.getPropery('replace_map')
        if not mapAvailable:
            self.addPropery('replace_map', 'npborcdefyzjlqsuvwghitaxm')

        mapAvailable = self.getPropery('transpose_map')
        if not mapAvailable:
            self.addPropery('transpose_map', '51068139472')

        mapAvailable = self.getPropery('space_replacement')
        if not mapAvailable:
            self.addPropery('space_replacement', '^')

    def getPropery(self,propery):

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM settings where type='"+propery+"'")
        result = cur.fetchall()
        if len(result) == 0:
            return False
        else :
            return result

    def getAllProperies(self):

            cur = self.conn.cursor()
            cur.execute("SELECT * FROM settings")
            result = cur.fetchall()
            if len(result) == 0:
                return False
            else:
                return result

    def updatePropery(self, type, value):
        stmt = "UPDATE settings set value = ? where  type=? )"
        args = (value, type)
        try:
            self.conn.execute(stmt, args)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print('insert failed, DB error')




