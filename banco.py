import sqlite3



class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('bancoEstacionamento.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists placas( placa char , d_entrada char, h_entrada char, d_saida date , h_saida date , v_pago char , nv_uti char )""")


        self.conexao.commit()
        c.close()


