#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Formation
#------------------------------------------------------------

CREATE TABLE Formation(
        idFormation Int  Auto_increment  NOT NULL ,
        Diplome     Varchar (50) NOT NULL ,
        Annee       Int NOT NULL ,
        Departement Varchar (50) NOT NULL
	,CONSTRAINT Formation_PK PRIMARY KEY (idFormation)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Equipe
#------------------------------------------------------------

CREATE TABLE Equipe(
        IdEquipe Int  Auto_increment  NOT NULL ,
        Nom      Varchar (50) NOT NULL ,
        Slogan   Varchar (50) NOT NULL ,
        NbPoints Int NOT NULL
	,CONSTRAINT Equipe_PK PRIMARY KEY (IdEquipe)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Etudiant
#------------------------------------------------------------

CREATE TABLE Etudiant(
        IdEtudiant  Int  Auto_increment  NOT NULL ,
        Nom         Varchar (50) NOT NULL ,
        Prenom      Varchar (50) NOT NULL ,
        Adresse     Varchar (50) NOT NULL ,
        NbPoints    Int NOT NULL ,
        idFormation Int NOT NULL ,
        IdEquipe    Int
	,CONSTRAINT Etudiant_PK PRIMARY KEY (IdEtudiant)

	,CONSTRAINT Etudiant_Formation_FK FOREIGN KEY (idFormation) REFERENCES Formation(idFormation)
	,CONSTRAINT Etudiant_Equipe0_FK FOREIGN KEY (IdEquipe) REFERENCES Equipe(IdEquipe)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Activite
#------------------------------------------------------------

CREATE TABLE Activite(
        IdActivite   Int  Auto_increment  NOT NULL ,
        Nom          Varchar (50) NOT NULL ,
        DateActivite Date NOT NULL ,
        Lieu         Varchar (50) NOT NULL ,
        Duree        Time NOT NULL ,
        Descriptif   Varchar (50) NOT NULL ,
        NbPoints     Int NOT NULL ,
        NbMax        Int NOT NULL
	,CONSTRAINT Activite_PK PRIMARY KEY (IdActivite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Challenge
#------------------------------------------------------------

CREATE TABLE Challenge(
        IdChallenge   Int  Auto_increment  NOT NULL ,
        Nom           Varchar (50) NOT NULL ,
        DateChallenge Date NOT NULL ,
        Lieu          Varchar (50) NOT NULL ,
        Duree         Time NOT NULL ,
        Descriptif    Varchar (50) NOT NULL ,
        NbPoints      Int NOT NULL ,
        NbEquipes     Int NOT NULL
	,CONSTRAINT Challenge_PK PRIMARY KEY (IdChallenge)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: InscriptionActivite
#------------------------------------------------------------

CREATE TABLE InscriptionActivite(
        IdActivite Int NOT NULL ,
        IdEtudiant Int NOT NULL
	,CONSTRAINT InscriptionActivite_PK PRIMARY KEY (IdActivite,IdEtudiant)

	,CONSTRAINT InscriptionActivite_Activite_FK FOREIGN KEY (IdActivite) REFERENCES Activite(IdActivite)
	,CONSTRAINT InscriptionActivite_Etudiant0_FK FOREIGN KEY (IdEtudiant) REFERENCES Etudiant(IdEtudiant)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: InscriptionChallenge
#------------------------------------------------------------

CREATE TABLE InscriptionChallenge(
        IdChallenge Int NOT NULL ,
        IdEquipe    Int NOT NULL
	,CONSTRAINT InscriptionChallenge_PK PRIMARY KEY (IdChallenge,IdEquipe)

	,CONSTRAINT InscriptionChallenge_Challenge_FK FOREIGN KEY (IdChallenge) REFERENCES Challenge(IdChallenge)
	,CONSTRAINT InscriptionChallenge_Equipe0_FK FOREIGN KEY (IdEquipe) REFERENCES Equipe(IdEquipe)
)ENGINE=InnoDB;

