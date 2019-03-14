import ldap
import ldap.modlist as modlist
import sys
from time import sleep
 
admin_pwd = 'ZAR_&"kan'
LDAP_ADDR = 'ldap://AD2016.projet6.oc:389'
LDAP_BASE = 'DC=projet6,DC=oc'
LDAP_BIND_ADMIN = 'CN=franck.hebert,OU=ServiceTech,OU=SocieteX,DC=AD2016,DC=projet6,DC=oc'
# dn of the new user
user_dn = 'CN=test1,OU=test,OU=SocieteX,DC=AD2016,DC=projet6,DC=oc'
# dict for all attributes of the user
ad_user = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'cn': 'test1',
    'givenName': 'First_name ',
    'displayName': 'test1',
    'sAMAccountName': 'test1',
    'sn': 'middle name i guest',
    'userAccountControl': '514',  # 514 will set user account to disabled, 512 is enable but can't create directly
    'userPrincipalName': 'test1@mon.domaine.fr',
    'mail': 'test1@mon.domaine.fr',
    'userPassword': 'passsword',
    'description': 'test'
}
 
# Open the LDAP connection
print("initializing ..")
try:
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    l = ldap.initialize(LDAP_ADDR)
except ldap.LDAPError as e:
    print(e)
    sys.exit(1)
 
# Set protocol version to LDAPv3
l.protocol_version = ldap.VERSION3
 
# Bind to AD with admin account
print("binding ..")
try:
    l.bind_s(LDAP_BIND_ADMIN, admin_pwd)
except ldap.LDAPError as e:
    print(e)
    sys.exit(1)
else:
    print('Sucessfully bound to AD')
 
# create ldif from attributes
ldif = modlist.addModlist(ad_user)
 
# insert user
try:
    l.add_s(user_dn, ldif)
    print("Insert new user")
except ldap.LDAPError as e:
    sys.stderr.write('Error while insert new user \n')
    sys.stderr.write('Message: ' + str(e) + '\n')
    sys.exit(1)
 
# close connexion
l.unbind()