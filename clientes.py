# ARQUIVO PARA DEFINIR A INSERÇÃO E EXCLUSÃO DE CLIENTES

from banco import Banco

class Placas(object):
    def __init__(self, placa = "", h_entrada = "", h_saida = "",
                     d_entrada = "", d_saida = "", v_pago = 0.00, nv_uti = ""):
        self.placa = placa
        self.h_entrada = h_entrada
        self.h_saida = h_saida
        self.d_entrada = d_entrada
        self.d_saida = d_saida
        self.v_pago = v_pago
        self.nv_uti = nv_uti

    #////////////////////// INSERIR ///////////////////////////////#
    def inserirPlaca(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into placas (placa, h_entrada, h_saida, d_entrada, d_saida,"
                      "v_pago, nv_uti) values('" + self.placa +"','"+ self.h_entrada +"',"
                      "'"+ self.h_saida +"','"+ self.d_entrada +"',"
                      "'"+ self.d_saida +"','" + self.v_pago +"','"+ self.nv_uti +"')")

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

    # ////////////////////// SELECIONAR ///////////////////////////#
    def selecionaPlaca(self, placa):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from placas where placa = " + placa + "  ")

            for linha in c:
                self.placa = linha[0]
                self.h_entrada = linha[1]
                self.h_saida = linha[2]
                self.d_entrada = linha[3]
                self.d_saida = linha[4]
                self.v_pago = linha[5]
                self.nv_uti = [6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"

    def selecionaBox(self, box):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from placas where nv_uti = " + box + "  ")

            for linha in c:
                self.placa = linha[0]
                self.h_entrada = linha[1]
                self.h_saida = linha[2]
                self.d_entrada = linha[3]
                self.d_saida = linha[4]
                self.v_pago = linha[5]
                self.nv_uti = [6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"