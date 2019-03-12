import ldap
import time
import sys
import yaml

# definition du dictionnaire qui contiendra les info de connexion du fichier YAML
dictLDAP = {}

# definition du dictionnaire qui contiendra les info de l'utilisateur du fichier YAML
dictUser = {}

# définition de la fonction de connexion
def Connexion (dictLDAP) :
    try:
        ObjetAD = ldap.initialize(dictLDAP.get('srvAD'))
        connex = ObjetAD.simple_bind_s(dictLDAP.get('admin'), dictLDAP.get('mdp'))
        print(connex)
    except ldap.LDAPError as e:
        print("echec connexion :", e)
        sys.exit(1)
    return ObjetAD


# definition de la fonction d'ajout d'utilisateur
#def AjoutUtil (ObjetAD, dictUser) :
#    try:
#        ObjetAD.add_s(userDN, ldap.modlist.addModlist(dictUser))
#    except:

# definition d'une fonction de modification d'utilistateu

# definition pour supprimer un util

# definir fonction de verification des droits (en fonction d'un utilisateur type) avec remonter anomalie

# definir un appel a vide


# definition du main qui servira à gerer le déroulé du script        

def main():
    argument = sys.argv[1]

    if argument == "c":
        Connexion(dictLDAP)
    elif argument == "a":
        # fonction ajoututil
    elif argument == "s":
        # fonction supprutil
    elif argument == "m":
        # fonction modifutil
    else:
        print("choix incorrecte")
        # fonction aide

main()