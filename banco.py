import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('Banco_estacionamento.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
# tabela de placas e controle (uma para dois )
        c.execute("""create table if not exists placas(
                    placa text message_text primary key,
                    dh_entrada text,
                    dh_saida text,
                    v_pago text,
                    nv_uti text)""")
# tabela de fidelidade de clinetes
        c.execute("""create table if not exists fidel(
                     n_card_fidel message_text primary key,
                     placa text,
                     nome_user text,
                     cpf text,
                     cod_fidel int)""")
# tabela de nivel de fidelidade
        c.execute("""create table if not exists nivel_fidel(
                     tipo message_text primary key,
                     perc_desc text,
                     cod_fidel int)""")


        self.conexao.commit()
        c.close()
