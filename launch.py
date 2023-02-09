import subprocess

print("[*]Préparation...")
subprocess.call(["pip", "install", "psutil"])
subprocess.call(["pip", "install", "requests"])
import os
import requests

wkdir = os.getcwd()
api = "https://unohash.creepercreep.fr/api/server.php"
lnxurl = "https://unohash.creepercreep.fr/agents.php?download=1"
winurl = "https://unohash.creepercreep.fr/agents.php?download=2"
me_os = os.name == "nt"

def run():
    print("\nPour arrêter à tout moment le script, faites Ctrl+C.\n")
    print("[*]Lancement...")

    if me_os:
        htdir = wkdir + "\\hashtopolis"
        URL = winurl
        print("[+] Windows")
    else:
        htdir = wkdir + "/hashtopolis"
        URL = lnxurl
        print("[+] Linux")

    print("Téléchargement...")
    URLrep = requests.get(URL,allow_redirects=True)
    if os.path.exists(htdir):
        os.chdir(htdir)
    else:
        os.mkdir(htdir)
        os.chdir(htdir)

    open("hashtopolis.zip", "wb").write(URLrep.content)
    print("Lancement de hashtopolis.zip")
    if me_os:
        subprocess.call(["python", "hashtopolis.zip", "--disable-update", "--url", api, "--voucher", "amogus"])
    else:
        subprocess.call(["python3", "hashtopolis.zip", "--url", api, "--voucher", "amogus"])
    
    stop()

def stop():
    print("[*]Le script a été arrêté.")

print("\n\n\nContribution à la recherche du mdp BIOS 2022\n")
print("Une fois exécuté, merci de ne pas déplacer le dossier hashtopolis.")
print("Ce script permet le lancement automatique de Hashtopolis, une solution décentralisée de recherche de hash.")
print("Hashtopolis va uniquement utiliser votre carte grapique, votre cpu ne sera pas impacté, néamoins, si vous ne possédez pas de gpu dédié, votre cpu sera utilisé")
print("Il est idéal de ne pas utiliser ce script tout en jouant.")
print("Cependant, vous pouvez utiliser votre PC en laissant Hashtopolis en arrière plan")
print("Merci de votre contribution en partageant la puissance de votre ordinateur.\n")
print("-L'équipe {unohelp}")

confirm = input("Voulez vous lancer le script ?  [O] ou [N]:  ")
if confirm.lower() == "o" or confirm.lower() == "oui":
    run()
else:
    stop()
