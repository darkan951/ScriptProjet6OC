import ldap
import time
import sys

# definition du serveur
srvAD = 'srvAD.projet6.oc'

try:
    # création de l'objet contenant l'AD et sur lequel s'éffecturont les modifications
    ObjetAD = ldap.initialize(srvAD)
    connex = ObjetAD.simple_bind_s('cn=franck hebert,ou=ServiceTechnique,ou=SocieteX,dc=projet6,dc=oc', 'ZAR_&"kan')
    print(connex)
    time.sleep(5)
except ldap.LDAPError as e:
    print("echec connexion :", e)
    time.sleep(5)

# capture argument ligne de commande

# déclaration du help pour afficher les choix possibles
