# ARQUIVO PARA DEFINIR A INSERÇÃO E EXCLUSÃO DE CLIENTES

from banco import Banco

class Placas(object):
    def __init__(self, placa = "", dh_entrada = "", dh_saida = "",
                     v_pago = 0.00, nv_uti = ""):
        self.placa = placa
        self.dh_entrada = dh_entrada
        self.dh_saida = dh_saida
        self.v_pago = v_pago
        self.nv_uti = nv_uti

    #////////////////////// INSERIR ///////////////////////////////#
    def inserirPlaca(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into placas (placa, dh_entrada, dh_saida,"
                      "v_pago, nv_uti) values('" + self.placa +"','"+ self.dh_entrada +"',"
                      "'"+ self.dh_saida +"','" + self.v_pago +"','"+ self.nv_uti +"')")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserçao do usuário!"

    # ////////////////////// EXCLUIR ///////////////////////////////#
    def deletePlaca(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from placas where placa = " + self.placa + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

