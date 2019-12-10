# ARQUIVO PARA DEFINIR A INSERÇÃO E EXCLUSÃO DE CLIENTES

from banco import Banco

class Placas(object):
    def __init__(self, placa = "", d_entrada = "", h_entrada = "", d_saida = "", h_saida ="",
                     v_pago = "", nv_uti = ""):
        self.placa = placa
        self.d_entrada = d_entrada
        self.h_entrada = h_entrada
        self.d_saida = d_saida
        self.h_saida = h_saida
        self.v_pago = v_pago
        self.nv_uti = nv_uti

    #////////////////////// INSERIR ///////////////////////////////#
    def inserirPlaca(self):
        banco = Banco()
        c = banco.conexao.cursor()

        c.execute("insert into placas (placa, d_entrada, h_entrada, d_saida, h_saida, v_pago, nv_uti) values('"+ self.placa +"','" + self.d_entrada +"','" + self.h_entrada +"','" + self.d_saida +"','" + self.h_saida +"','" + self.v_pago +"','"+ self.nv_uti +"')")

        banco.conexao.commit()
        c.close()


    # ////////////////////// EXCLUIR ///////////////////////////////#
    def deletePlaca(self):
        banco = Banco()
        c = banco.conexao.cursor()

        c.execute("delete from placas where placa = " + self.placa + " ")

        banco.conexao.commit()
        c.close()
