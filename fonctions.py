import os
import json
from constantes import ROLES
import menus as f
import string
import random
from time import sleep
from constantes import (TAILLE_ECRAN, F_USERS, ETAT)


def saisir_entier(msg: str, min: int, max: int) -> int:
    entier = input(msg)
    while (not entier.isdigit() or (int(entier) < min or int(entier) > max)):
        entier = input(msg)
    return int(entier)


def effacer_ecran():
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")


def ligne(taille: int, motif="-"):
    print(motif*taille)


def titre(titre: str, motif="-"):
    ligne(TAILLE_ECRAN, motif)
    ligne(TAILLE_ECRAN, motif)
    print(f"{titre:90}")
    ligne(TAILLE_ECRAN, motif)
    ligne(TAILLE_ECRAN, motif)


def load_users():
    with open(F_USERS) as f:
        return f.read().splitlines()[1:]


def load_users_json(nom):
    with open(nom) as mon_ficher:
        return json.load(mon_ficher)


def connexion(log, password):
    effacer_ecran()
    users = load_users()
    for line in users:
        us = line.split(";")
        login = us[3]
        passwd = us[4]
        etat = int(us[6])
        if (log == login and password == passwd):
            if (etat == 1):
                return us
            else:
                print("VOUS AVEZ ETE BLOQUER")
    return []


def connexion_json(log, password, role):
    effacer_ecran()
    users = load_users_json("utilisateur.json")
    for line in users:
        login = line.get("login")
        passwd = line.get("pass")
        rol = line.get("role")
        etat = int(line.get("etat"))
        if (log == login and password == passwd and rol == role):
            if (etat == 1):
                return line
            else:
                print("VOUS AVEZ ETE BLOQUER")
    return None


def change_state(users: list, idUser: int, state: int):
    for line in users:
        id = line.get("id")
        etat = int(line.get("etat"))
        if (id == idUser):
            line["etat"] = state
            update_json(F_USERS, users)
    return users


def details_client(users: list, idUser: int):
    for line in users:
        id = line.get("id")
        if (id == idUser):
            print(json.dumps(line, indent=2))
    return users


def profil_client(users: list, nomUser: str, prenomUser: str, telUser: int):
    for line in users:
        nom = line.get("nom")
        prenom = line.get("prenom")
        tel = line.get("tel")
        if tel == telUser and nom == nomUser and prenom == prenomUser:
            print(json.dumps(line, indent=2))
    return users


def show_user_rv(users: list):
    for line in users:
        role = line.get("role")
        if role == "client":
            print(json.dumps(line, indent=2))
    return line


def update_json(nom_ficher_json: str, data: list) -> None:
    with open(nom_ficher_json, "w") as mon_ficher:
        json.dump(data, mon_ficher)


def change_password(users: list, idUser: int, old_pass: str, new_pass: str):
    for line in users:
        id = line.get("id")
        passw = line.get("pass")
        if (id == idUser and old_pass == passw and old_pass != new_pass):
            line["pass"] = new_pass
            update_json(F_USERS, users)
    return users


def add_user_sec(users: list, nom: str, prenom: str, tel: int, heure_pointe: str, login: str, role: str):
    users.append({"id": len(users)+1, "nom": nom, "prenom": prenom, "tel": tel, "heure_pointe": heure_pointe,
                 "login": login, "pass": "passer", "role": role, "etat": 1})
    update_json(F_USERS, users)


def add_user_med(users: list, nom: str, prenom: str, tel: int, sprecialite: str, date_libre: str, heure_libre: str, login: str, role: str):
    users.append({"id": len(users)+1, "nom": nom, "prenom": prenom, "tel": tel, "sprecialite": sprecialite, "date_libre": date_libre, "heure_libre": heure_libre,
                 "login": login, "pass": "passer", "role": role, "etat": 1})
    update_json(F_USERS, users)


def create_user_rv_with_ordonnace(users: list, nom: str, prenom: str, tel: int, date_rv: str, heure_rv: str, service: str, nomMed: str, ordonnance: str, login: str, role: str):
    users.append({"id": len(users)+1, "nom": nom, "prenom": prenom, "tel": tel, "date_rv": date_rv,
                  "heure_rv": heure_rv, "service": service, "nomMed": nomMed, "ordonnance": ordonnance, "login": login, "pass": "passer", "role": role, "etat": 1})
    update_json(F_USERS, users)


def create_user_rv_without_ordonnace(users: list, nom: str, prenom: str, tel: int, date_rv: str, heure_rv: str, service: str, nomMed: str, role: str):
    users.append({"id": len(users)+1, "nom": nom, "prenom": prenom, "tel": tel, "date_rv": date_rv,
                  "heure_rv": heure_rv, "service": service, "nomMed": nomMed, "role": role, "etat": 1})
    update_json(F_USERS, users)


def show_users(users: list):
    titre("LISTER UTILISATEUR", "-")
    print(f"{'ID':<4}{'NOM':<17}{'PRENOM':<17}{'LOGIN':<22}{'ROLE':<17}{'ETAT':<10}")
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        role = line.get("role")
        etat = int(line.get('etat'))
        if role == "admin" or role == "medecin" or role == "secretaire":
            print(
                f"{line.get('id'):<4}{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('login'):<22}{line.get('role'):<17}{ETAT[etat]:<10}")
    return users


def show_med_available(users: list):
    titre("LISTER MEDECIN DISPONIBLE", "-")
    print(f"{'NOM':<17}{'PRENOM':<17}{'SERVICE':<17}{'JOUR DISPONIBLE':<13}{'HEURE DISPONIBLE':<13}")
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        role = line.get("role")
        if role == "medecin":
            print(f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('sprecialite'):<17}{line.get('date_libre'):<13}{line.get('heure_libre'):<13}")
    return users


def show_med(users: list, date: str, heure: str, date_available: str, time_available: str):
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        role = line.get("role")
        if role == "medecin":
            for line in role:
                if date == date_available and heure == time_available:
                    print("DEMANDE RENDEZ-VOUS...")
                    print("SAISIR VOS DONNEES:\n")
                    nom = input("Nom: \n")
                    prenom = input("Prenom: \n")
                    tel = int(input("Phone number: \n"))
                    date_rv = input(
                        "entrez date de rendez-vous au format(dd/mm/yyyy): ")
                    heure_rv = input(
                        "entrez heure rendez-vous au format(hh:mm): ")
                    service = input("entrer le service de consultation: ")
                    sleep(5)
                    print("FIN CONSULTATION ")
                    f.create_user_rv_without_ordonnace(users, nom, prenom, tel, date_rv, heure_rv, service,
                                                       ROLES[int(role)])
                elif date != date_available and heure != time_available:
                    print("AUCUN MEDECIN N'EST DISPONIBLE A CES HORAIRES")
    return role


def change_date(users: list, idUser: int, old_date: str, new_date: str):
    for line in users:
        id = line.get("id")
        date = line.get("date_libre")
        if id == idUser and old_date == date and new_date != old_date:
            line["date_libre"] = new_date
            update_json(F_USERS, users)
        else:
            print("modification de compte qui n'est pas le votre impossible")
    return users


def change_heure(users: list, idUser: int, old_heure: str, new_heure: str):
    for line in users:
        id = line.get("id")
        heure = line.get("heure_libre")
        if id == idUser and old_heure == heure and new_heure != old_heure:
            line["heure_libre"] = new_heure
            update_json(F_USERS, users)
        else:
            print("modification de compte qui n'est pas le votre impossible")
    return users


def show_rv_clt(users: list, nomUser: str, prenomUser: str, telUser: int):
    titre("LISTE DES RENDEZ-VOUS", "-")
    print(f"{'NOM':<17}{'PRENOM':<17}{'DATE':<13}{'HEURE':<13}{'SERVICE':<15}")
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        nom = line.get("nom")
        prenom = line.get("prenom")
        tel = line.get("tel")
        if nomUser == nom and prenomUser == prenom and telUser == tel:
            print(f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('date_rv'):<13}{line.get('heure_rv'):<13}{line.get('service'):<15}")
    return users


def write_ser(users: list, nomUser: str, prenomUser: str, telUser: int):
    for line in users:
        nom = line.get("nom")
        prenom = line.get("prenom")
        tel = line.get("tel")
        if (nomUser == nom and prenomUser == prenom and telUser == tel):
            file_name = nomUser + "_" + \
                str(telUser) + ''.join(random.choices(string.ascii_letters +
                                                      string.digits, k=5)) + ".txt"
            with open(file_name, "w") as file:
                file.write("Consultation de : \n\n")
                file.write("Nom : " + nom + "\n")
                file.write("Prénom : " + prenom + "\n")
                file.write("Tel : " + str(tel) + "\n\n")
                file.write("Information sur la consultation : \n\n")
                file.write("Service : " + line.get("service") + "\n")
                file.write("Date : " + line.get("date_rv") + "\n")
                file.write("Heure : " + line.get("heure_rv") + "\n\n")
                file.write("MEDECIN: " + line.get("nomMed") + "\n\n")
                file.write("Prescription : \n\n")
                file.write(line.get("ordonnance") + "\n")
                return
    return users



def demande_rv(users: list, nom: str, prenom: str, tel: int, motif: str, service: str, ordonnance: str, role: str,):
    users.append({"id": len(users)+1, "nom": nom, "prenom": prenom, "tel": tel,
                 "motif": "demande rv", "service": service, "ordonnance": ordonnance, "role": "client", "etat": 1})
    update_json(F_USERS, users)


def show_dm_clt(users: list, sprecialiteUser: str):
    titre("LISTER DES DEMANDE RV", "-")
    print(f"{'NOM':<17}{'PRENOM':<17}{'NUMERO':<10}{'MOTIF':<11}{'SERVICE':<13}{'ORDONNANCE':<9}{'ETAT':<15}")
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        sprecialite = line.get("sprecialite")
        if sprecialiteUser == sprecialite:
            for line in users:
                service = line.get("service")
                motif = line.get("motif")
                etat = line.get("etat")
                if sprecialiteUser == "dentiste":
                    if motif == "demande rv" and service == "dentiste":
                        print(
                            f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('tel'):<10}{line.get('motif'):<11}{line.get('service'):<13}{line.get('ordonnance'):<10}{ETAT[etat]:<30}")
                if sprecialiteUser == "ophtalmologue":
                    if motif == "demande rv" and service == "ophtalmologue":
                        print(
                            f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('tel'):<10}{line.get('motif'):<11}{line.get('service'):<13}{line.get('ordonnance'):<10}{ETAT[etat]:<30}")
                if sprecialiteUser == "cardiologue":
                    if motif == "demande rv" and service == "cardiologue":
                        print(
                            f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('tel'):<10}{line.get('motif'):<11}{line.get('service'):<13}{line.get('ordonnance'):<10}{ETAT[etat]:<30}")
            return users

def change_state_dm(users: list, telUser: int, state: int):
    for line in users:
        tel = line.get("tel")
        etat = int(line.get("etat"))
        if (tel == telUser):
            line["etat"] = state
            update_json(F_USERS, users)
    return users    


def show_cons(users: list, telUser: int, nomMed: str):
    titre("LISTE DES CONSULTATIONS", "-")
    print(f"{'NOM':<17}{'PRENOM':<17}{'DATE':<13}{'HEURE':<15}{'SERVICE':<17}{'MEDECIN':<25}")
    ligne(TAILLE_ECRAN, "=")
    for line in users:
        tel = line.get("tel")
        med = line.get("nomMed")
        if (tel == telUser and med == nomMed):
            print(f"{line.get('nom'):<17}{line.get('prenom'):<17}{line.get('date_rv'):<13}{line.get('heure_rv'):<15}{line.get('service'):<17}{line.get('nomMed'):<25}")
    return users