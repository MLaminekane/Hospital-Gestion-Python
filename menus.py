import fonctions as f
from fonctions import *
from constantes import TAILLE_ECRAN
from constantes import ROLES
from time import sleep
users = f.load_users_json("utilisateur.json")


def pre_connexion():
    f.effacer_ecran()
    f.ligne(TAILLE_ECRAN)
    f.ligne(TAILLE_ECRAN, "*")
    text = "CLIENT - SECREATIRE - MEDECIN - ADMIN"
    choix = "  1         2           3        4  "
    print(f"{'CHOISIR VOTRE ROLE:':^90}\n")
    print(f"{text:^90}")
    print(f"{choix:^90}")
    f.ligne(TAILLE_ECRAN)
    f.ligne(TAILLE_ECRAN)
    return f.saisir_entier("Faites votre choix:\n", 1, 4)


def connexion():
    f.effacer_ecran()
    f.titre("CONNEXION", "-")


def menu_admin():
    print("1---------LISTER LES UTILISATEURS ")
    print("2---------AJOUTER SECRETAIRE ")
    print("3---------AJOUTER MEDECIN ")
    print("4---------MODIFIER MOT DE PASSE UTILISATEUR ")
    print("5---------MODIFIER ETAT UTILISATEUR ")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX \n", 1, 9)


def menu_secretaire():
    print("1---------LISTER LES RENDEZ-VOUS  ")
    print("2---------CREER DEMANDE DE RENDEZ-VOUS  ")
    print("3---------GERER DEMANDE RV")
    print("4---------MODIFIER DISPONIBILITE MEDECIN ")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX \n", 1, 9)


def menu_medecin():
    print("1---------LISTER LES RENDEZ-VOUS  ")
    print("2---------LISTER DEMANDE RENDEZ-VOUS ET FAIRE CONSULTATION")
    print("3---------MODIFIER DISPONIBILITE ")
    print("4---------CONSULTER PROFIL CLIENT ")
    print("5---------VOIR SON PROFIL")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX:\n", 1, 9)


def menu_client():
    print("1---------VOIR SES CONSULTATIONS")
    print("2---------VOIR SES RENDEZ-VOUS")
    print("3---------TELECHARGER SA CONSULTATION ")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX \n", 1, 9)


def menu_users(role):
    if (role == ROLES[3]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_admin()):
                case 1:
                    print("1---------LISTE DES UTILISATEURS")
                    f.show_users(users)
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_admin()
                    else:
                        f.effacer_ecran()
                        menu_admin()
                case 2:
                    role = 1
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    login = f"{nom}{prenom}{(len(users)+1)*3}"
                    heure_pointe = input(
                        "entrer votre heure de pointe au format(hh:mm): ")
                    f.add_user_sec(users, nom, prenom, tel, heure_pointe,
                                   login, ROLES[int(role)])
                case 3:
                    role = 2
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    specialite = input("votre specialité: ")
                    date_libre = input(
                        "entrer votre date libre au format(YYYY/MM/DD): ")
                    heure_libre = input(
                        "entre votre heure libre au format(HH:MM): ")
                    login = f"{nom}{prenom}{(len(users)+1)*3}"
                    f.add_user_med(users, nom, prenom, tel, specialite, date_libre, heure_libre,
                                   login, ROLES[int(role)])
                case 4:
                    print("change user password")
                    f.change_password(users, int(input("entrer id: ")), input(
                        "entrer old pass: "), input("entrer new pass: "))
                case 5:
                    print("changer etat")
                    f.change_state(users, int(input("entrer id: ")),
                                   int(input("entrer new etat: ")))
                case 9:
                    retourMenu = 0
    if (role == ROLES[1]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_secretaire()):
                case 1:
                    f.show_user_rv(users)
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_secretaire()
                    else:
                        f.effacer_ecran()
                        menu_secretaire()
                case 2:
                    print("SERVICES DISPONIBLES: 'DENTISTE' / 'OPHTALMOLOGUE' / 'CARDIOLOGUE'")
                    f.demande_rv(users, input("nom: "), input("prenom: "), int(
                        input("tel: ")), print("motif"), input("service: "), input("ordonnance (oui ou non): "), print(role))
                case 3:
                    f.show_dm_clt(users, input("service de demande: "))
                    f.change_state_dm(users,int(input("entrer nouvelle etat de demande: ")))        
                case 4:
                    f.show_med_available(users)
                    print(
                        "QUE VOULEZ VOUS CHANGER L'HEURE OU LA DATE ? \nSi heure appuyez sur 1\nSi date appuyez sur 2")
                    choix = int(input("entrer votre choix: "))
                    if choix == 1:
                        f.change_heure(users, int(input("entrer id: ")), input(
                            "old heure: "), input("new heure: "))
                    elif choix == 2:
                        f.change_date(users, int(input("entrer id: ")), input(
                            "old date: "), input("new date: "))
                case 9:
                    retourMenu = 0
    if (role == ROLES[0]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_client()):
                case 1:
                    f.show_cons(users, input("nom medecin: "))
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_client()
                    else:
                        f.effacer_ecran()
                        menu_client()
                case 2:
                    f.show_rv_clt(users, input("votre nom: "), input(
                        "votre prenom: "), int(input("numero phone: ")), input("mot de passe: "))
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_client()
                    else:
                        f.effacer_ecran()
                        menu_client()
                case 3:
                    f.write_ord(users, input("votre nom: "), input(
                        "votre prenom: "), int(input("numero phone: ")))

                case 9:
                    retourMenu = 0
    if (role == ROLES[2]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_medecin()):
                case 1:
                    f.show_user_rv(users)
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_medecin()
                    else:
                        f.effacer_ecran()
                        menu_medecin()
                case 2:
                    f.show_dm_clt(users, input("votre specialite: "))
                    sleep(5)
                    x = input("voulez vous faire la consultation oui ou non : ")
                    if x == "oui":
                        role = 0
                        demande = int(
                            input("RV SANS ORDONNANCE--1 ou 2--RV AVEC ORDONNANCE"))
                        if (demande == 1):
                            print("DEBUT CONSULTATION...")
                            nom = input("Nom: \n")
                            prenom = input("Prenom: \n")
                            tel = int(input("Phone number: \n"))
                            date_rv = input(
                                "entrez date de rendez-vous au format(YYYY-MM-DD): ")
                            heure_rv = input(
                                "entrez heure rendez-vous au format(HH:MM): ")
                            service = input(
                                "entrer le service de consultation: ")
                            nomMed = input(
                                "nom du medecin pour la comsultation du patient: ")
                            sleep(5)
                            print("FIN CONSULTATION ")
                            f.create_user_rv_without_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service, nomMed,
                                                               ROLES[int(role)])
                        elif (demande == 2):
                            print("DEBUT CONSULTATION")
                            sleep(5)
                            nom = input("Nom: \n")
                            prenom = input("Prenom: \n")
                            tel = int(input("Phone number: \n"))
                            date_rv = input(
                                "entrez date de rendez-vous au format(YYYY-MM-DD): ")
                            heure_rv = input(
                                "entrez heure rendez-vous au format(HH:MM): ")
                            service = input(
                                "entrer le service de consultation: ")
                            nomMed = input(
                                "nom du medecin pour la comsultation du patient: ")
                            print("FIN CONSULTATION")
                            nom = input("Nom: \n")
                            prenom = input("Prenom: \n")
                            ordonnance = input(
                                "entrer l'ordonnace du client: ")
                            login = f"{nom}{prenom}{(len(users)+1)*2}"

                            f.create_user_rv_with_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service, nomMed, ordonnance,
                                                            login, ROLES[int(role)])
                case 3:
                    f.show_med_available(users)
                    print(
                        "QUE VOULEZ VOUS CHANGER L'HEURE OU LA DATE ? \nSi heure appuyez sur 1\nSi date appuyez sur 2")
                    choix = int(input("entrer votre choix: "))
                    if choix == 1:
                        f.change_heure(users, int(input("entrer id: ")), input(
                            "old heure: "), input("new heure: "))
                    elif choix == 2:
                        f.change_date(users, int(input("entrer id: ")), input(
                            "old date: "), input("new date: "))
                case 4:
                    f.details_client(users, int(input("entrer id: ")))
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_medecin()
                    else:
                        f.effacer_ecran()
                        menu_medecin()
                case 5:
                    f.profil_client(users, input("nom: "), input(
                        "prenom: "), int(input("numero: ")))
                    retour = input("Appuyez sur une touche pour retourner au menu: ")
                    if retour == "R":
                        f.effacer_ecran()
                        menu_medecin()
                    else:
                        f.effacer_ecran()
                        menu_medecin()
                case 9:
                    retourMenu = 0
