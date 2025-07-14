## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.

### 2. Implementierung der Klasse in Python:
- **Erstelle eine Python-Klasse oder Klassen**, die die Struktur des UML-Klassendiagramms widerspiegeln.
- **Definiere die Attribute und Methoden** entsprechend den Daten und Anforderungen aus dem JSON-Dokument.
```python
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

```

### 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n):
- **Schreibe ein Python-Skript**, das die JSON-Daten einliest.
- **Erstelle Instanzen der zuvor definierten Klasse(n)** und initialisiere sie mit den Daten aus dem JSON-Dokument.
```python
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

```

### 4. Methode zum Hinzufügen eines Members:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein neues Mitglied zum Team hinzufügt.
- Die Methode sollte die benötigten Informationen (z.B. Name, ID) als Parameter entgegennehmen und ein neues Mitgliedsobjekt erstellen und zur entsprechenden Liste hinzufügen.

```python
for squad in squads_list:
    if squad.squadName == "Super hero squad":
        squad.add_member("timmy", 12, "Turner", ["Laser", "Super strength"],101)

for i in squads_list:
    i.print_info()

```
### 5. Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern:
- **Implementiere eine Methode in der entsprechenden Klasse**, die das gesamte Team und deren Mitglieder auf eine lesbare Weise ausgibt.
- Die Methode sollte durch die Mitglieder des Teams iterieren und deren Details anzeigen.

-oben implementiert

### 6. Methode zum Löschen eines Members anhand der ID:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein Mitglied anhand seiner ID löscht.
- Die Methode sollte die Liste der Mitglieder durchsuchen, das Mitglied mit der passenden ID finden und es aus der Liste entfernen.
```Python
for squad in squads_list:
    if squad.squadName == "Super hero squad":
        squad.delete_member_by_id(4)

# Ausgabe nach Löschen
for i in squads_list:
    i.print_info()
```



## Fragen zur Objektorientierung

1. Warum verwendet man Objektorientierung?
-vereinfacht die Modellierung realer Konzepte in Ihren Programmen und ermöglicht Ihnen die Erstellung von Systemen, die wiederverwendbarer und skalierbarer sind
2. Welche weiteren Vorgehensweisen gibt es?
-Instanzmethoden, statische Methoden und Klassenmethoden, sowie die Verwendung von Attributen (Instanz- und Klassenattribute) und die Überladung von Operatoren
3. Was ist ein Objekt und was eine Klasse?
-eine Klasse ist eine Blaupause oder ein Bauplan für Objekte, während ein Objekt eine konkrete Instanz dieser Klasse ist
4. Was versteht man unter Kapselung?
-durch Kapselung kann man sicherstellen das daten nicht unabsichtlich geändert werden, da sie "verkapselt" in einer Klasse sind und nur in dieser klasse verändert werden darf
5. Was ist Vererbung?
-vererbung ermöglicht es in einer klasse, Eigenschatfen (Attribute und Methoden) einer anderen Klasse zu übernehmen.
6. Was versteht man unter Refactoring?
-den Prozess der Änderung eines bestehenden Code, um desen Struktur, Design oder Implementierung zu verbessern und gleichzeitig die Funktionalität nicht zu verändern
7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
Es macht Code sauberer, verständlicher und wartbarer, was wiederum die Wiederverwendung erleichtert
8. Für was gibt es die `__init__`-Funktion in einer Klasse?
-Sie dient dazu, die anfänglichen Werte der Objektattribute (Instanzvariablen) festzulegen
9. Für was braucht man den `self` Parameter?
-innerhalb einer Methoden-Definition auf das Objekt selbst zu verweisen, das die Methode aufruft.
10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
-einzeilige mit einem hashtag(#) und meerzeilige mit drei anführungszeichen am anfang des kommentares und am ende(""")
11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
-Java, C# und C++
12. Korrigiere die Fehlerhaften Skripte.

### Code 1
```python
class MyClass:
    def __init__(name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```


### Code 2
```python
def say_hello():
    print("Hello, World!")  

say_hello()
```


### Code 3 
```python
x = 10
if x == 5:   
    print("x is 5")
```


### Code 4
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```


### Code 5
```python
values = [1, 2, 3, 4, 5]
a, b, c, d, e = values
```