from json import load


def load_cctxt(e):
    global indice_ultima
    global ccs
    global count_cc

    if e == 'a':
        ccss = open("cc.txt", "r+")
        ccs = ccss.readlines()        
        indice_ultima = len(ccs) 
        count_cc = indice_ultima
        ccss.close()

    elif e == 'd':
        ccs = open("cc.txt", "r+")
        ccs = ccs.readlines()        
        indice_ultima = len(ccs) 
        count_cc = indice_ultima
        ccs.close()

def crearlinea():
    global count_cc
    file = [s.rstrip() for s in ccs]
    index_cc = indice_ultima - count_cc
    cc = file[index_cc].split("|")
    cc1 = cc[0]
    print(cc1)
    mes = cc[1] 
    anio = cc[2]
    try:
        cvv = cc[3]
    except:
        cvv = 000
    count_cc -= 1
    print(cc1 + mes + anio + cvv)
    '''try:
        file = [s.rstrip() for s in ccs]
        index_cc = indice_ultima - count_cc
        cc = file[index_cc].split("|")
        cc1 = cc[0]
        mes = cc[1] 
        anio = cc[2]
        try:
            cvv = cc[3]
        except:
            cvv = 000
        count_cc -= 1
        print(cc1 + mes + anio + cvv)
    except IndexError:
        finish = True'''


load_cctxt('a')
crearlinea()