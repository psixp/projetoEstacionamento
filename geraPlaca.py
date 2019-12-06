import random
import string
#
def hm_gen():
    from datetime import datetime
    data_comp_atual = datetime.now()
    dh_atual = data_comp_atual.strftime("%X")
    return str(dh_atual)


def dt_gen():
    from datetime import date
    d_atual = date.today()
    return str(d_atual)

# PROCURA UM BOX ALEATORIO ENTRE OS VAGOS
# ARRUMAR PARA BUSCAR NO BANCO / ERA UTILIZADO EM UM DICIONARIO


def box_gen():
    box_rand = random.randint(1, 40)
    #x_it = ent_veiculos.items()
    #for k, v in x_it:
    #    if str(box_rand) == v[0]:
    #        return box_gen()
    #    else:
    #        pass
    return str(box_rand)

def placa_gen():
# RETORNA 1 LETRA DO ALFABETO EM UPPERCASE
    def letter_gen():
        letter = random.choice(string.ascii_uppercase)
        return str(letter)

    # RETORNA 1 NUMERO DE 0 A 9
    def number_gen():
        number = random.choice("0123456789")
        return str(number)

    # GERADOR PLACA MERCOSUL
    def placa_gen_merc():
        pl = []
        for x in range(7):
            if len(pl) <= 1 or len(pl) == 2:
                pl.append(letter_gen())
            elif len(pl) == 3:
                pl.append(number_gen())
            elif len(pl) == 4:
                pl.append(letter_gen())
            elif len(pl) > 4:
                pl.append(number_gen())
        return ''.join(pl)

    # GERADOR PLACA ANTIGA
    def placa_gen_ant():
        pl = []
        for x in range(7):
            if len(pl) <= 1 or len(pl) == 2:
                pl.append(letter_gen())
            elif len(pl) > 2:
                pl.append(number_gen())
        return ''.join(pl)

    # ESCOLHE PLACA ANTIGA OU MERCOSUL
    gerpl = (placa_gen_merc(), placa_gen_ant())
    return random.choice(gerpl)
