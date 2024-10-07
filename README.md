# SPIKE Prime Emulator mit Pybricks

## Einleitung

Willkommen zum **SPIKE Prime Emulator mit Pybricks**! Dieses Projekt ermöglicht es dir, Programme für den LEGO SPIKE Prime Hub zu entwickeln und zu testen, ohne die physische Hardware zu benötigen. Der Emulator simuliert das 5x5-Matrixdisplay und die Tasten des Hubs unter Verwendung von Pybricks und Tkinter.

Dieses Projekt ist ideal für Entwickler, Pädagogen und Enthusiasten wie dich, die Programme schreiben und testen möchten, ohne direkten Zugriff auf einen SPIKE Prime Hub zu haben.

## Inhaltsverzeichnis

1. [Einleitung](#einleitung)
2. [Features](#features)
3. [Voraussetzungen](#voraussetzungen)
4. [Installation](#installation)
5. [Verwendung](#verwendung)
   - [Starten des Emulators](#starten-des-emulators)
   - [Bedienung](#bedienung)
6. [Beispielprogramm](#beispielprogramm)
   - [Programmstruktur](#programmstruktur)
   - [Anpassen des Programms](#anpassen-des-programms)
7. [Projektstruktur](#projektstruktur)
8. [Erweiterung des Projekts](#erweiterung-des-projekts)
9. [Fehlerbehebung](#fehlerbehebung)

## Features

- **Emulation des 5x5-Matrixdisplays**: Visualisiert das Display mit einstellbarer Helligkeit der einzelnen Pixel.
- **Emulation der Tasten**: Simuliert die linken, mittleren und rechten Tasten des Hubs, inklusive Tastendruck- und -freigabeereignissen.
- **Beispielprogramm**: Enthält ein interaktives Menüsystem zur Demonstration der Emulatorfunktionen.
- **Motor- und Sensor-Simulation**: Grundlegende Simulation von Motoren und eines Kraftsensors zur Demonstration von Hardware-Interaktionen.

## Voraussetzungen

- **Python 3.x**: Stelle sicher, dass Python 3 installiert ist. Überprüfe deine Version mit:

  ```bash
  python --version
  ```

- **Tkinter**: Wird für die GUI benötigt. Tkinter ist normalerweise standardmäßig installiert. Um zu überprüfen, ob Tkinter installiert ist, führe folgendes Skript aus:

  ```python
  import tkinter
  print("Tkinter ist installiert!")
  ```

  Falls Tkinter nicht installiert ist:

  - **Windows**: Tkinter ist in der Regel enthalten.
  - **macOS**: Installiere es über Homebrew:

    ```bash
    brew install python-tk
    ```

  - **Linux (Ubuntu/Debian)**:

    ```bash
    sudo apt-get install python3-tk
    ```

## Installation

1. **Repository klonen oder herunterladen**

   Klone das Repository oder lade das ZIP herunter und entpacke es:

   ```bash
   git clone https://github.com/blockplacer4/pybricks-emulator.git
   cd pybricks-emulator
   ```

2. **Abhängigkeiten installieren**

   Es sind keine zusätzlichen Python-Pakete erforderlich, da das Projekt auf Standardbibliotheken basiert.

## Verwendung

### Starten des Emulators

Führe das Beispielprogramm `main.py` aus, um den Emulator zu starten:

```bash
python main.py
```

### Bedienung

- **Emulatorfenster**: Es öffnet sich ein Fenster mit dem 5x5-Matrixdisplay des SPIKE Prime Hubs.
- **Tastensteuerung**:

  - **Schaltflächen**: Unter dem Display befinden sich drei Schaltflächen für die linken, mittleren und rechten Tasten.
  - **Tastatursteuerung**:

    - **Linke Taste**: Linke Pfeiltaste
    - **Mittlere Taste**: Eingabetaste
    - **Rechte Taste**: Rechte Pfeiltaste

- **Menünavigation**:

  - Verwende die **linke** und **rechte** Taste, um durch die Menüoptionen zu navigieren.
  - Drücke die **mittlere** Taste, um eine Option auszuwählen.

## Beispielprogramm

Das `main.py`-Skript enthält ein interaktives Menüsystem, das die Funktionen des Emulators demonstriert.

### Programmstruktur

- **Funktionen**:

  - `einsammelone()`: Beispiel-Funktion, die ausgeführt wird, wenn sie im Menü ausgewählt wird.

- **Debug-Programme**:

  - Enthalten in der Liste `debugs`, ermöglichen sie das Testen von Motoren in verschiedenen Richtungen.

- **Motoren**:

  - Simuliert durch die Klasse `Motor`, mit Methoden:

    - `run(speed)`: Startet den Motor mit der angegebenen Geschwindigkeit.
    - `stop()`: Stoppt den Motor.

- **Kraftsensor**:

  - Simuliert durch die Klasse `ForceSensor`, mit der Methode:

    - `pressed()`: Gibt an, ob der Sensor gedrückt ist (in der Simulation immer `False`).

### Anpassen des Programms

- **Neue Funktionen hinzufügen**:

  Füge eigene Funktionen zur Liste `funktionen` hinzu:

  ```python
  def meine_funktion():
      print("Meine Funktion wird ausgeführt!")

  funktionen = [einsammelone, meine_funktion]
  ```

- **Debug-Programme erweitern**:

  Du kannst weitere Debug-Elemente zur Liste `debugs` hinzufügen, um zusätzliche Motoren oder Aktionen zu testen.

## Projektstruktur

- **`main.py`**: Hauptprogramm, das den Emulator verwendet und ein Beispielmenü bereitstellt.
- **`emulator.py`**: Enthält die Klasse `MatrixDisplayEmulator`, die das Display und die Tasten emuliert.
- **`pybricks_sim.py`**: Simuliert die Pybricks-Bibliothek mit Klassen wie `PrimeHub`, `Button` und `Display`.

## Erweiterung des Projekts

- **Erweiterte Sensor-Simulation**:

  - Implementiere zusätzliche Sensoren wie Farbsensoren oder Gyroskope.

- **Erweiterte Motorsteuerung**:

  - Füge Funktionen für präzisere Motorsteuerung hinzu, z. B. Gradgenauigkeit oder Geschwindigkeitsprofile.

- **GUI-Verbesserungen**:

  - Füge dem Emulator weitere GUI-Elemente hinzu, um z. B. Sensorwerte anzuzeigen oder Einstellungen zu ändern.

- **Kompatibilität mit echten Pybricks-Programmen**:

  - Passe die Simulation so an, dass sie bestehende Pybricks-Programme ohne Modifikationen ausführen kann.

## Fehlerbehebung

- **Tkinter nicht gefunden**:

  - Stelle sicher, dass Tkinter installiert ist (siehe [Voraussetzungen](#voraussetzungen)).

- **Emulatorfenster öffnet sich nicht**:

  - Überprüfe, ob das Skript Fehler ausgibt, und stelle sicher, dass alle Dateien korrekt vorhanden sind.

- **Tasten reagieren nicht**:

  - Stelle sicher, dass das Emulatorfenster den Fokus hat, wenn du die Tastatur verwendest.

---

Viel Spaß beim Programmieren und Testen mit dem SPIKE Prime Emulator!
