import mysql.connector
import random
import string
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tp_db"
)
nbValeurs = 600

names = []
with open("noms.txt", "r") as f:
	names = f.readlines()

def insert_values(query, val, db):
	db.cursor().executemany(query, val)
	db.commit()
	print("Valeurs inserees dans la BDD.")

formation = "INSERT INTO formation (Diplome, Annee, Departement) VALUES (%s, %s, %s)"
formation_val = []
for i in range(nbValeurs):
	val = ('Diplome_'+str(i), random.randrange(2000, 2020), 'Departement_'+str(i))
	formation_val.append(val)
insert_values(formation, formation_val, mydb)

equipe = "INSERT INTO equipe (Nom, Slogan, NbPoints) VALUES (%s, %s, %s)"
equipe_val = []
for i in range(nbValeurs):
	val = ('Equipe_'+str(i), ''.join(random.choice(string.ascii_lowercase) for _ in range(15)), 0)
	equipe_val.append(val)
insert_values(equipe, equipe_val, mydb)

etudiant = "INSERT INTO etudiant (Nom, Prenom, Adresse, NbPoints, IdFormation, IdEquipe) VALUES (%s, %s, %s, %s, %s, %s)"
etudiant_val = []
for i in range(nbValeurs):
	val = ('Nom_Etudiant_'+str(i), random.choice(names).replace('\n', ''), ''.join(random.choice(string.ascii_lowercase) for _ in range(15)), 0, random.randrange(1,nbValeurs), random.randrange(1,nbValeurs))
	etudiant_val.append(val)
insert_values(etudiant, etudiant_val, mydb)

activite = "INSERT INTO activite (Nom, DateActivite, Lieu, Duree, Descriptif, NbPoints, NbMax) VALUES (%s, %s, %s, %s, %s, %s, %s)"
activite_val = []
for i in range(nbValeurs):
	val = ('Nom_Activite_'+str(i), datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ''.join(random.choice(string.ascii_lowercase) for _ in range(15)), datetime(1, 1, 1, 0, random.randrange(1,60), 0).strftime('%H:%M:%S'), ''.join(random.choice(string.ascii_lowercase) for _ in range(40)), random.randrange(10, 50), random.randrange(1, 40))
	activite_val.append(val)
insert_values(activite, activite_val, mydb)

challenge = "INSERT INTO challenge (Nom, DateChallenge, Lieu, Duree, Descriptif, NbPoints, NbEquipes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
challenge_val = []
for i in range(nbValeurs):
	val = ('Nom_Challenge_'+str(i), datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ''.join(random.choice(string.ascii_lowercase) for _ in range(15)), datetime(1, 1, 1, 0, random.randrange(1,60), 0).strftime('%H:%M:%S'), ''.join(random.choice(string.ascii_lowercase) for _ in range(40)), random.randrange(10, 50), random.randrange(2, 10))
	challenge_val.append(val)
insert_values(challenge, challenge_val, mydb)

inscription_activite = "INSERT INTO inscriptionactivite (IdActivite, IdEtudiant) VALUES (%s, %s)"
inscription_activite_val = []
temp = []
for i in range(nbValeurs):
	val = (random.randrange(1,nbValeurs), random.randrange(1,nbValeurs))
	while val in temp:
		val = (random.randrange(1,nbValeurs), random.randrange(1,nbValeurs))
	temp.append(val)
	inscription_activite_val.append(val)
insert_values(inscription_activite, inscription_activite_val, mydb)

inscription_challenge = "INSERT INTO inscriptionchallenge (IdChallenge, IdEquipe) VALUES (%s, %s)"
inscription_challenge_val = []
temp = []
for i in range(nbValeurs):
	val = (random.randrange(1,nbValeurs), random.randrange(1,nbValeurs))
	while val in temp:
		val = (random.randrange(1,nbValeurs), random.randrange(1,nbValeurs))
	temp.append(val)
	inscription_challenge_val.append(val)
insert_values(inscription_challenge, inscription_challenge_val, mydb)
