from json import *

# Question 1:
# Proposition de réponse 1
def est_base(c): 
    
    """
    Retourne `True` si ce caractère correspond à une base de l'ADN (est un des caractères `A`, `T`, `G`, `C`), 
    et `False` sinon. 
    
    """
    if c in ["A", "T", "G", "C"]: 
        return True 
    else:
        return False
    
# Proposition de réponse 2
def est_base(c): 
    tab = ["A", "T", "G", "C"]
    i = 0
    while i < len(tab): 
        if c == tab[i]: 
            return True
        i += 1
    
    return False
#*********************************************#
    



def est_adn(chaine):
    
    """
     Retourne`True` si la chaîne correspond à un ADN (est constituée uniquement des caractères `A`, `T`, `G`, `C`),
     et `False` sinon.
     
    """
    i = 0
    while i < len(chaine): 
        if est_base(chaine[i]) == False: 
            return False
        i += 1
        
    return True


def arn(adn): 
    
    """
    Retourne la séquence ARN associée à une séquence d'ADN.
    
    """
    
    if est_adn(adn) == False: 
        return None
    
    i = 0
    s = ""
    while i < len(adn): 
        if adn[i] == "T": 
            s += "U"
        else: 
            s += adn[i]
        i += 1
            
    return s


def arn_to_codons(arn): 
    
    """
    Retourne un tableau contenant la liste des codons.
    
    """
    i = 0
    s = ""
    codons = []
    while i < len(arn): 
        s += arn[i]
        if len(s)%3 == 0: 
            codons.append(s)
            s = ""
        i += 1
        
    return codons       


def load_dico_codons_aa(fichier): 
    
    """
    Retourne la structure de données chargée en mémoire à partir du JSON.
    
    """
    strjson = fichier.read()
    fichier.close()
    dic = loads(strjson)
    
    return dic


def codons_stop(dic):
    
    """
    Retourne un tableau contenant l'ensemble des codons stop, 
    c'est-à-dire l'ensemble des codons possibles avec les caractères `AUGC` qui ne sont pas des clés du dictionnaire.

    """
    codons = dic.keys()
    
    fichier = open ("./data/codons_aa.json","r")
    liste_codons = load_dico_codons_aa(fichier)
    
    codons_stop = []
    
    i = 0 
    while i < len(codons): 
        j = 0
        while j < len(liste_codons) and codons[i] != liste_codons[j]: 
            j += 1
        if j == len(liste_codons): 
            stop.append(codons[i])
        i += 1
        
    
    return codons_stop


def codons_to_aa(tab_codons, dic_codons): 
    
    """
    Retourne un tableau contenant les acides aminés correspondant aux codons.
    
    """
    tab_codons_stop = codons_stop(dic_codons)
    tab_ret = []
    
    i = 0
    while i < len(tab_codons): 
        j = 0
        while j < len(tab_codons_stop) and tab_codons[i] != tab_codons_stop[j]:
            j += 1
        if j == len(tab_codons_stop): 
            tab_ret.append(dic_codons[tab_codons[i]])
        else:
            return tab_ret
        i += 1
        
    return tab_ret




def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
