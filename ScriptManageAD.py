import ldap3
import time
import sys

# definition du serveur
srvAD = ldap3.Server('srvAD.projet6.oc')

try:
    # création de l'objet contenant l'AD et sur lequel s'éffecturont les modifications
    ObjetAD = ldap3.Connection(srvAD, user='cn=franck hebert,ou=ServiceTechnique,ou=SocieteX,dc=projet6,dc=oc', password='ZAR_&"kan', auto_bind=True)
    print("connecté")
    time.sleep(5)
except ldap3.core.exceptions.LDAPException as e:
    print("echec connexion :", e)
    time.sleep(5)

choix_util = input("1 - Ajouter un utilisateur \n2 - Modifier un utilisateur")


ObjetAD.unbind()