from modules.core.person import Person
import re
import mysql.connector as mysql
import json
import numpy as np
import base64


class Database():
    # ----> constructor
    def __init__(self):
        self.db = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="vipereo"
        )
        self.c = self.db.cursor()

    def close(self):
        if(self.con):
            self.db.close()

    # ----> create table if not exist
    def initiate(self) -> bool:
        try:
            # ----> create a table : Person
            self.c.execute("""CREATE TABLE IF NOT EXISTS Person(
            id int primary key auto_increment,
            firstname varchar(50),
            lastname varchar(50),
            email varchar(100),
            phone varchar(20),
            adress varchar(250)
            ) ENGINE=INNODB;
            """)
            # ----> create a table : Face
            self.c.execute("""CREATE TABLE IF NOT EXISTS Face(
            face_id int primary key auto_increment,
            person_id int,
            image BLOB,
            face_encode JSON DEFAULT NULL,
            FOREIGN KEY(person_id) REFERENCES Person(id) on delete cascade
            ) ENGINE=INNODB;
            """)

            self.c.execute("""CREATE TABLE IF NOT EXISTS LOL(
                image BLOB,
                face_encode JSON DEFAULT NULL
                ) ENGINE=INNODB;
                """)

            # ---> commit les modification
            self.db.commit()
            return True
        except:
            return False

    def convertImageToBinary(self, img) -> bytes:
        return base64.b64encode(img.read())

    def convertBinaryToImage(self, binary) -> bytes:
        return base64.b64decode(binary)

    def addPerson(self, person):
        self.c.execute(
            "insert into person(firstname,lastname,email,phone,adress) values(%s,%s,%s,%s,%s)", (person.Firstname(
            ), person.Lastname(), person.Email(), person.Phone(), person.Adress()))
        self.db.commit()

    def isUnique(self, person) -> bool:
        self.c.execute("select count(*) from person where firstname = %s and lastname = %s",
                       (person.Firstname(), person.Lastname()))
        i = self.c.fetchone()[0]
        if(i != 0):
            return False, "please choose a different firstname and lastname."
        self.c.execute(
            "select count(*) from person where email = %s ", (person.Email(),))
        j = self.c.fetchone()[0]
        if(j != 0):
            return False, "this email adress already exist, please try again."
        return True, "Cheking ..."

    def getPerson(self):
        self.c.execute("select * from person")
        result = self.c.fetchall()
        persons = []
        for person in result:
            id, firstname, lastname, email, phone, adress = person
            p = Person(firstname, lastname, email, phone, adress)
            p.setId(id)
            persons.append(p)
        return persons

    def getPersonByName(self, person):
        self.c.execute("select count(*) from person where firstname = %s and lastname = %s ",
                       (person.Firstname(), person.Lastname()))
        id, fistname, lastname, email, phone, adress = self.c.fetchone()[0]
        p = Person(fistname, lastname, email, phone, adress)
        p.setId(id)
        return
        # d = Database()
        # d.test()
