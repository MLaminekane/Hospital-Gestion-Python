import menus
from time import sleep as PAUSE
import fonctions as f
from constantes import ROLES
users = f.load_users_json("utilisateur.json")
retour = 1
while (retour == 1):
    choix = menus.pre_connexion()
    role = ROLES[choix-1]
    log = input("LOGIN: \n")
    passwd = input("PASSWORD: \n")
    connectedUser = f.connexion_json(log, passwd, role)
    if (connectedUser == None):
        f.titre("LOGIN OU MOT DE PASSE INVALIDE", '*')
        PAUSE(3)
    else:
        menus.menu_users(role)
