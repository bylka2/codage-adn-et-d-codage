from biology import *
"""
les tests unitaires des fonctions definies 
"""

#Question 1 :
# Tests unitaires 

def test_est_base(): 
    assert est_base("A") == True
    assert est_base("T") == True
    assert est_base("G") == True
    assert est_base("C") == True #le programme retourne True parce que C se trouve dans la liste.
    assert est_base("U") == False
    assert est_base("a") == False
    assert est_base("t") == False
    assert est_base("g") == False
    assert est_base("c") == False
    assert est_base("z") == False
    assert est_base("b") == False
    print("test ok")
    
test_est_base()    
#----------------------------------------------------------#

#Question 2 : 
# Tests unitaires 
def test_est_adn(): 
    assert est_adn("ATGTCAAA") == True
    assert est_adn("AGCCATTC") == True
    assert est_adn("GGGAACT") == True
    assert est_adn("ATBOAATG") == False
    assert est_adn("AACUTG") == False
    assert est_adn("AZEGGC") == False
    assert est_adn("AGU") == False
    assert est_adn("ACCTG") == True    
    print("test ok")
    
test_est_adn()
#------------------------------------------------------------#

#Question 3 : 
# Tests unitaires 
def test_arn():
    assert arn("ATGTCAAA") == "AUGUCAAA"
    assert arn("GCTAAUUA") == None
    assert arn("GCTAATTA") == "GCUAAUUA"
    assert arn("BEIGGCCTTA") == None
    assert arn("ATCGGCAA") == "AUCGGCAA"   
    print("test ok")
    
test_arn()
#------------------------------------------------------------#

#Question 4 : 
# Tests unitaires 
def test_arn_to_codons(): 
    assert arn_to_codons("CGUUAGGGG") == ["CGU", "UAG", "GGG"]
    assert arn_to_codons("CGUAAU") == ["CGU", "AAU"]
    assert arn_to_codons("CGUAAUGC") == ["CGU", "AAU"]
    assert arn_to_codons("GCCAGCCUAGC") == ["GCC", "AGC", "CUA"]
    print("test ok")
    
test_arn_to_codons()
#------------------------------------------------------------#

#Question 5 : 

# Tests unitaires 1
def test_load_dico_codons_aa(): 
    fichier = open("./data/codons_aa.json","r")
    assert load_dico_codons_aa(fichier) == {
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Methionine",
    "AUG": "Methionine",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "GAU": "Aspartic acid",
    "GAC": "Aspartic acid",
    "GAA": "Glutamic acid",
    "GAG": "Glutamic acid",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AGU": "Serine",
    "AGC": "Serine",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"
    }
    print("test ok")
    
test_load_dico_codons_aa()

# Tests unitaires 2
def test_codons_stop(): 
    dic = {
        "UAA": "ocre",
        "CGA": "Arginine",
        "CGG": "Arginine",
        "AGU": "Serine",
        "AGC": "Serine",
        "UAG": "ambre",
        "UGA": "opale",
        "GGU": "Glycine",
        "GGC": "Glycine"
    }
    assert codons_stop(dic) == ["UAA", "UAG", "UGA"]
    print("test ok")
    

test_codons_stop()
#------------------------------------------------------------#

#Question 6 : 
# Tests unitaires 
def test_codons_to_aa(): 
    fichier = open("./data/codons_aa.json","r")
    codons = load_dico_codons_aa(fichier)
    
    assert codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"], codons) == ["Arginine", "Asparagine"]
    print("test ok")
    
test_codons_to_aa()    

#------------------------------------------------------------#

