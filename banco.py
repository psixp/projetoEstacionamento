import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        #self.createTable()

    def createTable(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE placas (
                                            id        INTEGER PRIMARY KEY AUTOINCREMENT,
                                            placa     CHAR,
                                            d_entrada CHAR,
                                            h_entrada CHAR,
                                            d_saida   DATE,
                                            h_saida   DATE,
                                            v_pago    CHAR,
                                            nv_uti    CHAR,
                                            box_util  INT
                                         );""")
        self.conn.commit()
        c.close()

    def getBoxsUso(self):
        db = self.conn.cursor()
        db.execute("""SELECT box_util FROM placas""")
        row = db.fetchall()
        listbox = []
        for x in range(len(list(row))):
            listbox.append(row[x][0])
        db.close()
        return listbox



    def insertDados(self, itensDicio):
        db = self.conn
        db.cursor()
        db.execute("""INSERT INTO placas (
                                  placa,
                                  d_entrada,
                                  h_entrada,
                                  box_util
                              )
                              VALUES (?,?,?,?)
                              """,
                   (itensDicio['placa'], itensDicio['d_entrada'], itensDicio['h_entrada'], itensDicio['box']))
        db.commit()
        db.close()

