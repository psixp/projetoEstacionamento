import sqlite3



conexao = sqlite3.connect('bancoEstacionamento.db')
c = conexao.cursor()

c.execute("""
CREATE TABLE if NOT EXISTS placas(
            placa TEXT primary key,
            d_entrada TEXT,
            h_entrada TEXT,
            d_saida TEXT,
            h_saida TEXT,
            v_pago TEXT,
            bx_utilizado TEXT,
            nv_uti TEXT);
            """)

c.execute("""
CREATE TABLE if NOT EXISTS uso_diaria(
           id TEXT,
           placa TEXT,
           d_entrada TEXT,
           h_entrada TEXT,
           d_saida TEXT,
           h_saida TEXT,
           v_pago TEXT,
           bx_utilizado text primary key);
           """)

conexao.commit()
c.close()
