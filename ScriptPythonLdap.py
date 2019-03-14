import ldap
import ldap.modlist as Modlist
import time
import sys
import yaml

dictLDAP = yaml.load(open('Connexion.yaml'))['Connexion']
dictUser = yaml.load(open('AddUser.yaml'))['UtilisateurAjout']
userDN = yaml.load(open('AddUser.yaml'))['CheminUtil']

# définition de la fonction de connexion
def Connexion (dictLDAP) :
    try:
        ObjetAD = ldap.initialize(dictLDAP['srvAD'])
        connex = ObjetAD.simple_bind_s(dictLDAP['admin'], dictLDAP['mdp'])
        print(connex)
    except ldap.LDAPError as e:
        print("echec connexion :", e)
        sys.exit(1)
    return ObjetAD

ldif = Modlist.addModlist(dictUser)

# definition de la fonction d'ajout d'utilisateur
def AjoutUtil (ObjetAD, dictUser, ldif) :
    try:
        ObjetAD.add_s(userDN['user_dn'], ldif)
        print('Insertion du nouvel utilisateur')
    except ldap.LDAPError as e:
        sys.stderr.write('Erreur insertion utilisateur ')
        sys.stderr.write('Message: ' + str(e) + '\n')
        sys.exit(1)

# definition d'une fonction de modification d'utilistateu

# definition pour supprimer un util

# definir fonction de verification des droits (en fonction d'un utilisateur type) avec remonter anomalie

# fonction d'aide appellé si le script n'a pas d'argument ou un mauvais argument
def aideScript():
    aide = """ 
    Remplir le fichier YAML.
    liste des arguments :
        c   appel la connexion à l'AD
        a   appel l'ajout d'utilisateur
        s   appel la suppression d'utilisateur
        m   appel la modification d'utilisateur
    """
    print(aide)

# definition du main qui servira à gerer le déroulé du script        

def main():

    print(dictLDAP)

    if len(sys.argv) < 2:
        aideScript()
        sys.exit(1)

    argument = sys.argv[1]

    if argument == "c":
        Connexion(dictLDAP)
    elif argument == "a":
        connex = Connexion(dictLDAP)
        AjoutUtil(connex, dictUser, ldif)
        connex.unbind()
    elif argument == "s":
        # fonction supprutil
        print("en cour de dev")
    elif argument == "m":
        # fonction modifutil
        print("en cour de dev")
    else:
        print("choix incorrect")
        aideScript()

main()