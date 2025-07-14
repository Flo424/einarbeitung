#Code1 zu aufgabe 2. Implementierung der Klasse in Python
class members:

    def __init__(self, name, age, secret_identity, powers, ID):
        self.name = name
        self.age = age
        self.secret_identity = secret_identity
        self.powers = powers
        self.ID = ID
        
    def print_info(self):
        print(f"Member Name: {self.name}   Secret identity: {self.secret_identity}  Powers: {self.powers}  ID: {self.ID}")

        
    
class squads:
    def __init__(self, squadName, homeTown,formed,status,secretBase,active,members):
        self.squadName = squadName
        self.homeTown = homeTown
        self.formed = formed
        self.status = status
        self.secretBase = secretBase
        self.active = active
        self.members = members

    def add_member(self, name, age, secret_identity, powers,ID):
        new_member = members(name, age, secret_identity, powers,ID)
        self.members.append(new_member)
    
    def delete_member_by_id(self, member_id):
        for index, member in enumerate(self.members):
            if member.ID == member_id:
                self.members.pop(index)
    

    def print_info(self):
        print(f"\n\nsquadname: {self.squadName} \nhomeTown: {self.homeTown} \nformed: {self.formed} \nstatus: {self.status} \nsecretBase: {self.secretBase} \nactive: {self.active} ")
        for i in self.members:
            i.print_info()

 

#Code 2 zu Aufgabe 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n)
import json

with open('base.json', 'r') as file:
    json_data = json.load(file)

squads_list = []

current_id = 1

for squad in json_data:
    members_list = []
    for member in squad.get('members', []):
        id = current_id
        current_id += 1
    
        members_list.append(
            members(name = member.get("name"),
            age = member.get("age"),
            secret_identity= member.get("secretIdentity"),
            powers = member.get("powers"),
            ID = id
            )
        )
    squads_list.append(
        squads(squadName=squad.get("squadName"),
            homeTown = squad.get("homeTown"),
            formed=squad.get("formed"),
            status=squad.get("status"),
            secretBase=squad.get("secretBase"),
            active=squad.get("active"),
            members=members_list
            )
    )


    
#code 3 zu Aufgabe 4.Methode zum Hinzufügen eines Members:

for squad in squads_list:
    if squad.squadName == "Super hero squad":
        squad.add_member("timmy", 12, "Turner", ["Laser", "Super strength"],101)



# code 4 zu Aufgabe 5.Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern
# oben implementiert

#code 5 zu Aufgabe 6.Methode zum Löschen eines Members anhand der ID:
for squad in squads_list:
    if squad.squadName == "Super hero squad":
        squad.delete_member_by_id(15)

# Ausgabe nach Löschen
for i in squads_list:
    i.print_info()

