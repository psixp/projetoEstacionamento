import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.createTable()
        self.setPlacaDB = ""
        self.setDEntradaDB = ""
        self.setHEntradaDB = ""
        self.setBoxDB = 0


    def createTable(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS diaria (
                                            id        INTEGER PRIMARY KEY AUTOINCREMENT,
                                            placa     CHAR,
                                            d_entrada DATE,
                                            h_entrada DATE,
                                            box_util  INT
                                                        );""")
        c.execute("""CREATE TABLE IF NOT EXISTS logg (
                                            id        INTEGER PRIMARY KEY AUTOINCREMENT,
                                            placa     CHAR,
                                            d_entrada DATE,
                                            h_entrada DATE,
                                            d_saida   DATE,
                                            h_saida   DATE,
                                            v_pago    CHAR,
                                            nv_uti    CHAR,
                                            box_util  INT
                                                        );""")
        #c.commit()
        c.close()

    def getBoxsUso(self):
        db = self.conn.cursor()
        db.execute("""SELECT box_util FROM diaria""")
        row = db.fetchall()
        listbox = []
        for x in range(len(list(row))):
            listbox.append(row[x][0])
        #db.commit()
        db.close()

        return listbox

    def getDadosRow(self, placaorbox):
        db = self.conn.cursor()
        db.execute("SELECT * FROM diaria WHERE placa = ?", (str(placaorbox),))
        row = db.fetchall()
        self.setPlacaDB = row[0][1]
        self.setDEntradaDB = row[0][2]
        self.setHEntradaDB = row[0][3]
        self.setBoxDB = row[0][4]
        #db.commit()
        db.close()

    def updateDadosSaida(self, dt):
        db = self.conn.cursor()
        db.execute("""UPDATE diaria
                           SET 
                               d_saida = ?,
                               h_saida = ?
                         WHERE  
                               placa = ? """, (dt[0], dt[1], dt[2]))

        db.commit()
        db.close()



    def deletarDados(self, itensDicio):
        db = self.conn.cursor()
        db.execute("DELETE FROM diaria WHERE placa = ?", (itensDicio['placa']))

        db.commit()
        db.close()

    def insertDadosLogg(self,itensDicio):
        db = self.conn
        db.cursor()
        db.execute("""INSERT INTO logg (
                                     placa,
                                     d_entrada,
                                     h_entrada,
                                     d_saida,
                                     h_saida,
                                     v_pago,
                                     box_util
                                 )
                                 VALUES (?, ?, ?, ?, ?, ?, ?)
                                 """,
                   #(itensDicio.values))
                   (itensDicio['placa'], itensDicio['d_entrada'], itensDicio['h_entrada'],itensDicio['d_saida'], itensDicio['h_saida'], itensDicio['v_pago'], itensDicio['box']))
        db.commit()
        db.close()

    def insertDadosDiaria(self, itensDicio):
        db = self.conn
        db.cursor()
        db.execute("""INSERT INTO diaria (
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

