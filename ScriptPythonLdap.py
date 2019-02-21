import ldap
import time
import sys

# definition du serveur
srvAD = 'srvAD.projet6.oc'

dictLDAP = {
    'srvAD':'srvAD.projet6.oc',
    'admin':'cn=franck hebert,ou=ServiceTechnique,ou=SocieteX,dc=projet6,dc=oc',
    'mdp':'ZAR_&"kan'
}

def Connexion (dictLDAP) :
    try:
        ObjetAD = ldap.initialize(dictLDAP.get('srvAD'))
        connex = ObjetAD.simple_bind_s(dictLDAP.get('admin'), dictLDAP.get('mdp'))
        print(connex)
    except ldap.LDAPError as e:
        print("echec connexion :", e)

# capture argument ligne de commande

# déclaration du help pour afficher les choix possibles

Connexion(dictLDAP)