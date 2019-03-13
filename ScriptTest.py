import yaml

fichYAML = yaml.load(open('ParametreScript.yaml'))
print(fichYAML)

print(fichYAML['Connexion']['srvAD'])

testd = {}
