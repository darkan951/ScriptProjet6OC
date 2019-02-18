import ldap
import sys

# Création du dictionnaire pour stocker les informations de connexion à l'Active Directory

LDAP = {
    """adresse_ad""" : """ldaps://srvad.projet6.oc:636""" ,
    """base_ad""" : """DC=projet6,DC=oc""" ,
    """admin_ad""" : """""" ,
    """passw_ad""" : """ZAR_&"kan"""
}


# Fonction de connexion à l'Active Directory en tant qu'admin du domaine

def connexionAD():

    # connexion à l'AD et création de l'objet AD
    print("initialisation")
    try:
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        AD = ldap.initialize(LDAP["""adresse_ad"""])
    except ldap.LDAPError, e:
        print e
        sys.exit(1)
    
    # définition du protocol
    AD.protocol_version = ldap.VERSION3

    # connexion de l'admin du domaine
    print("connexion")
    try:
        AD.bind_s(LDAP["""admin_ad"""], LDAP["""passw_ad"""])
    except ldap.LDAPError, e:
        print e
        sys.exit(1)
    
    return AD


AD.unbind()