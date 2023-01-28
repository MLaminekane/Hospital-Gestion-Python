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
    print(f"{'CHOISIR VOTRE ROLE:':^60}\n")
    print(f"{text:^60}")
    print(f"{choix:^60}")
    f.ligne(TAILLE_ECRAN)
    f.ligne(TAILLE_ECRAN)
    return f.saisir_entier("Faites votre choix:\n", 1, 4)


def connexion():
    f.effacer_ecran()
    f.titre("CONNEXION", "-")


def menu_admin():
    print("1---------LISTER LES UTILISATEUR ")
    print("2---------AJOUTER SECRETAIRE ")
    print("3---------AJOUTER MEDECIN ")
    print("4---------MODIFIER MOT DE PASSE UTILISATEUR ")
    print("5---------MODIFIER ETAT UTILISATEUR ")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX \n", 1, 9)


def menu_secretaire():
    print("1---------LISTER LES RENDEZ-VOUS  ")
    print("2---------CREER RENDEZ-VOUS ")
    print("3---------MODIFIER RENDEZ-VOUS ")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX \n", 1, 9)


def menu_medecin():
    print("1---------LISTER LES RENDEZ-VOUS  ")
    print("2---------FAIRE CONSULTATION ")
    print("3---------MODIFIER DISPONIBILITE ")
    print("4---------CONSULTER PROFIL CLIENT ")
    print("5---------VOIR PROFIL")
    print("9---------SE DECONNECTER ")
    return f.saisir_entier("FAITES VOTRE CHOIX:\n", 1, 9)


def menu_client():
    print("1---------DEMANDE CONSULTATION")
    print("2---------VOIR SES CONSULTATIONS")
    print("3---------VOIR SES RENDEZ-VOUS")
    print("4---------VOIR RENDEZ-VOUS PROCHAIN")
    print("5---------TELECHARGER SON ORDONNANCE ")
    print("6---------MODIFIER SON RENDEZ VOUS PROCHAIN")
    print("7---------VOIR PROFIL")
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
                    sleep(10)
                case 2:
                    role = input("Secretaire--->1:\n")
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    login = f"{nom}{prenom}{(len(users)+1)*3}"
                    heure_pointe = input(
                        "entrer votre heure de pointe au format(hh/mm): ")
                    f.add_user_sec(users, nom, prenom, tel, heure_pointe,
                                   login, ROLES[int(role)])
                case 3:
                    role = input("Medecin--->2:\n")
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    specialite = input("votre specialité: ")
                    date_libre = input(
                        "entrer votre date libre au format(dd/mm/yyyy): ")
                    heure_libre = input(
                        "entre votre heure libre au format(hh/mm): ")
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
                    sleep(10)
                case 2:
                    role = input("Client--->0: ")
                    print("DEMANDE DE RENDEZ-VOUS")
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    date_rv = input(
                        "entrez date de rendez-vous au format(dd/mm/yyyy): ")
                    heure_rv = input(
                        "entrez heure rendez-vous au format(hh/mm): ")
                    service = input("entrer le service de consultation: ")
                    login = f"{nom}{prenom}{(len(users)+1)*2}"
                    f.create_user_rv_without_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service,
                                                       ROLES[int(role)])
                case 9:
                    retourMenu = 0
    if (role == ROLES[0]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_client()):
                case 1:
                    f.show_med_available(users)
                    f.show_med(users, input("entrer une date de rendez-vous: "),
                               input("entrer l'heure de rendez-vous: "), input(
                                   "entrer une date de medecin en fonction du service souhaiter: "),
                               input("entrer l'heure de medecin en fonction du service souhaiter: "))
                    sleep(3)
                case 3:
                    f.show_rv_clt(users, input("votre nom: "), input(
                        "votre prenom: "), int(input("numero phone: ")))
                    sleep(10)
                case 5:
                    f.write_ser(users, input("votre nom: "), input(
                        "votre prenom: "), int(input("numero phone: ")))
                    sleep(10)
                case 7:
                    f.profil_client(users, input("nom: "), input(
                        "prenom: "), int(input("numero: ")))
                    sleep(10)
                case 9:
                    retourMenu = 0
    if (role == ROLES[2]):
        retourMenu = 1
        while (retourMenu == 1):
            f.effacer_ecran()
            match (menu_medecin()):
                case 1:
                    f.show_user_rv(users)
                    sleep(10)
                case 2:
                    role = input("Client--->0: \n")
                    demande = int(
                        input("RV SANS ORDONNANCE--1 ou 2--RV AVEC ORDONNANCE"))
                    if (demande == 1):
                        print("DEBUT CONSULTATION...")
                        nom = input("Nom: \n")
                        prenom = input("Prenom: \n")
                        tel = int(input("Phone number: \n"))
                        date_rv = input(
                            "entrez date de rendez-vous au format(dd/mm/yyyy): ")
                        heure_rv = input(
                            "entrez heure rendez-vous au format(hh/mm): ")
                        service = input("entrer le service de consultation: ")
                        sleep(5)
                        print("FIN CONSULTATION ")
                        login = f"{nom}{prenom}{(len(users)+1)*2}"
                        f.create_user_rv_without_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service,
                                                           ROLES[int(role)])
                    elif (demande == 2):
                        print("DEBUT CONSULTATION")
                        sleep(5)
                        nom = input("Nom: \n")
                        prenom = input("Prenom: \n")
                        tel = int(input("Phone number: \n"))
                        date_rv = input(
                            "entrez date de rendez-vous au format(dd/mm/yyyy): ")
                        heure_rv = input(
                            "entrez heure rendez-vous au format(hh/mm): ")
                        service = input("entrer le service de consultation: ")
                        print("FIN CONSULTATION")
                        nom = input("Nom: \n")
                        prenom = input("Prenom: \n")
                        ordonnance = input("entrer l'ordonnace du client: ")
                        login = f"{nom}{prenom}{(len(users)+1)*2}"
                        f.create_user_rv_with_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service, ordonnance,
                                                        login, ROLES[int(role)])
                    else:
                        print("REVENEZ PLUS TARD")
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
                    sleep(10)
                case 5:
                    f.profil_client(users, input("nom: "), input(
                        "prenom: "), int(input("numero: ")))
                    sleep(10)
                case 9:
                    retourMenu = 0
