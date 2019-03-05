import ldap
import time
import sys

# definition du dictionnaire contenant les informations de connexion
dictLDAP = {
    'srvAD':'srvAD.projet6.oc',
    'admin':'cn=Franck Hebert,ou=ServiceTechnique,ou=SocieteX,dc=projet6,dc=oc',
    'mdp':'ZAR_&"kan',
    'base':'dc=projet6,dc=oc'
}

# a modif ==> mettre dans fichier YAML
dictUser = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'prenom': '',
    'nomFamille': '',
    'nomAfficher': '',
    'sAMAccountName': '',
    'nomComplet': '',
    'userAccountControl': '',  # 514 will set user account to disabled, 512 is enable but can't create directly
    'nomDeConnexion': '',
    'mail': '',
    'pwdUtil': '',
    'description': ''
}

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
def AjoutUtil (ObjetAD, dictUser) :
    try:
        ObjetAD.add_s(userDN, ldap.modlist.addModlist(dictUser))
    except:

# definition d'une fonction de modification d'utilistateu

# definition pour supprimer un util

# definir fonction de verification des droits (en fonction d'un utilisateur type) avec remonter anomalie

# definir un appel a vide


# definition du main qui servira à gerer le déroulé du script        
def main():
    Connexion(dictLDAP)

main()