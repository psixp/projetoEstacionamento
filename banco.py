import sqlite3

class Banco:
    def __init__(self):
        self.conexao = self.createBanco()
        #self.conexao = self.createTable()

    def createBanco(self):
        conn = sqlite3.connect('Banco_estacionamento.db').close()
        conn.close()
        return conn

    def createTable(self):
        c = self.conexao.cursor()
        # tabela de placas e controle (uma para dois )
        c.execute("""create table if not exists uso_diaria(
                    id text autoincrement,
                    placa text message_text primary key,
                    d_entrada text,
                    h_entrada text,
                    d_saida text,
                    h_saida text,
                    v_pago text,
                    bx_utilizado text,
                    nv_uti text)""")

        c.execute("""create table if not exists uso_diaria(
                    id text autoincrement,
                    placa text,
                    d_entrada text,
                    h_entrada text,
                    d_saida text,
                    h_saida text,
                    v_pago text,
                    bx_utilizado text primary key)""")

# tabela de fidelidade de clinetes
        #c.execute("""create table if not exists fidel(
        #             n_card_fidel message_text primary key,
        #             placa text,
        #             nome_user text,
        #             cpf text,
        #             cod_fidel int)""")

# tabela de nivel de fidelidade
        #c.execute("""create table if not exists nivel_fidel(
        #             tipo message_text primary key,
        #             perc_desc text,
        #             cod_fidel int)""")

        self.conexao.commit()
        c.close()