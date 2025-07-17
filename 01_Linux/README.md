# Einrichten einer Virtual Machine (VM) unter Rocky Linux
## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.

### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer für das tägliche arbeiten. Du kannst ihn benennen wie du möchtest 

### Installierte Programme
a) nvim  
b) Git  
c) check-mk 
b) Erstelle ein Basis Monitoring für ein Server, Switches, Firewall 
## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
Linux ist ein Betriebssystem, das wie Windows oder macOS funktioniert, aber offener und anpassbarer ist und dir mehr Kontrolle über deinen Computer gibt
- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
hohe Sicherheit, Anpassbarkeit, Stabilität, Kostenfreiheit und eine große Community
- Warum sollt man nicht dauerhaft mit dem root User arbeiten?
da ein unbeabsichtigter Fehler oder eine Sicherheitslücke zu schwerwiegenden Schäden am System führen kann
- Was ist Virtualisierung und welche Vorteile bieten VMs?
Virtualisierung erlaubt es, auf einem Computer mehrere virtuelle Rechner gleichzeitig zu nutzen, um Platz zu sparen und verschiedene Systeme parallel laufen zu lassen, VMs haben verbesserte Ressourcenauslastung, Kostensenkung, verbesserte Sicherheit und größere Flexibilität
- Was sind yum und dnf?
Paketmanager für RPM-basierte Linux-Distributionen ( RPM steht für "Red Hat Package Manager" und ist ein Werkzeug, mit dem Softwarepakete erstellt, installiert, aktualisiert und verwaltet werden können)
- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
Eine IDE ist eine Entwicklungsumgebung, mit der man leichter programmieren kann, weil sie im Vergleich zu einem einfachen Texteditor viele automatische Hilfen und Funktionen bietet
- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
Ein LSP hilft dem Texteditor, Programmieren besser zu verstehen und macht das Schreiben leichter als ein einfacher Editor durch z.b code vorschläge wärend man schreibt.
- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
Man startet Programme mit & im Hintergrund und nutzt Befehle wie ps, jobs und kill, um sie zu sehen und zu stoppen.
- Wie kann man Skripte unter Linux erstellen und ausführen?
Um ein Skript unter Linux zu erstellen und auszuführen, benötigt man einen Texteditor und die Kommandozeile
- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
Der Linux-Kernel ist der Kern des Betriebssystems Linux und verwaltet die Hardware-Ressourcen und die Kommunikation zwischen Software und Hardware
- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
Ein Hardlink zeigt direkt auf den Inhalt (die Daten selbst), während ein symbolischer Link nur auf die Datei verweist (also auf den Dateipfad, der zum Inhalt führt).
- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
LTS-Versionen sind besonders lange sicher und stabil, weil sie viele Jahre Updates bekommen, ohne große Änderungen, sodass dein System zuverlässig läuft.
- Wie schreibt man Kommentare in Bash?
In Bash schreibt man Kommentare, indem man eine Zeile mit # beginnt
- Was ist vim?
Vim ist ein schneller und einfacher Texteditor den man mit der Tastatur steuert
### Linux-Befehle
Was bewirken folgende Befehle:
- `history`
man sieht die zuletzt eingegebene befehle auf der VM
- `chmod`
chmod wird verwendet, um die Berechtigungen für Dateien und Verzeichnisse auf Linux zu ändern
- `chown`
Ändert, wem eine Datei gehört
- `mv test.txt abc`
Datei umbenenen oder verschieben
- `ll | grep test`
Der Befehl grep test sucht auf Linux in der Eingabe oder einer Datei nach Zeilen, die das Wort „test“ enthalten, und gibt diese aus
- `find . -name cisco`
Sucht im aktuellen Ordner nach Dateien mit Namen „cisco“
- `find / -name cisco`
Sucht überall auf dem Computer nach Dateien mit Namen „cisco“
- `tar -xvf archive.tar.gz`
Entpackt eine gepackte Datei
- `df -h`
Zeigt, wie viel Speicher auf deinen Festplatten frei oder voll ist
- `du -sh directory`
Zeigt, wie groß ein Ordner ist
- `ps aux`
Zeigt, welche Programme gerade laufen
- `grep pattern file`
Sucht in einer Datei nach einem bestimmten Wort
- `top`
Zeigt laufende Programme und wie viel Leistung sie brauchen.
- `netstat -tuln`
Zeigt, welche Verbindungen dein Computer gerade hat
- `ifconfig`
Zeigt Informationen über deine Netzwerkverbindung
- `ping host`
Prüft, ob ein anderer Computer angepingt werden kann
