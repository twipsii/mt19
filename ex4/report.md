# Bericht MT19: Übung 4

*Lorenz Nagele*

## Datenset

Da die Intention dieser Übung hauptsächlich das Experimentieren mit einem RNN-Modell ist und wir als Output "nur" ein generiertes Sample zur Verfügung haben, wollte ich ein Datenset wählen, das domänenspezifisch ist und wo der Output damit möglichst nachvollziehbar sein soll. Songtexte (Lyrics) könnten sich gut dafür eignen und haben auch Potenzial einen amüsanten Text zu generieren.

Bei meiner Suche bin ich auf ein GitHub-Repo mit einer Sammlung von Metal-Lyrics gestossen: [JarbasAl/metal_dataset](https://github.com/JarbasAl/metal_dataset)

Ich habe mich für die Death Metal-Lyrics entschieden, die bereinigt über 2.8 Millionen Zeilen "tödliche" Gesangstexte enthalten.

## Pre-Processing

Das Datenset wurde automatisiert von einer Datenbank mit Songtexten gezogen und ist daher in einem unbereinigten Zustand. Die einzelnen Lyrics zu den Songs sind untereinander angehängt.

Im Skript *preprocessing_input.py* entferne ich zuerst alle leeren Zeilen. Desweiteren entferne ich Whitespaces am Anfang und Schluss jeder Zeile und wandle den Text in Kleinbuchstaben um, da bei Lyrics fast alle Zeilen mit einem Grossbuchstaben beginnen und auch viele Wörter grossgeschrieben werden, obwohl sie in Englisch verfasst sind. In der Metal-Musik wird oftmals auch "geschrien", was manchmal komplett in GROSSBUCHSTABEN versucht wird darzustellen.

Für das zweite Training verwende ich zusätzlich **SpaCy** um den Text zu tokenisieren, damit vor allem die Satzzeichen getrennt vom Text sind. Dazu füge ich die einzelnen Tokens wieder durch ein Leerzeichen getrennt zusammen.

## Anpassungen/Hyperparameter beim zweiten Training

**Trainingsset**

Für das erste Training habe ich von den ursprünglichen 2.8 Millionen Zeilen 100'000 verwendet, also 2000 fürs Dev-Set und 98'000 fürs Trainingsset.

Im zweiten Training habe ich dann die doppelte Menge genommen, also 200'000 Zeilen Text. Das Dev-Set bleibt mit 2000 Zeilen gleich gross und das Trainingsset enthielt neu 198'000 Zeilen.

**Hyperparameter**

Um das Resultat des ersten Trainings zu überprüfen, habe ich bereits ein paar Zeilen Text mit dem Sprachmodell generiert. Das Ergebnis war bereits erstaunlich gut! Deshalb habe ich für das zweite Training nicht viel verändert. Nur die Epochen habe ich von 10 auf 25 gesetzt. Dies birgt die Gefahr Overfiting zu betreiben, jedoch ist die Zahl nicht übertrieben hoch und ist zum Teil auch Standard bei anderen RNN-Trainings.

Diese Änderung konnte ich leicht im Kommandozeilenbefehl vornehmen, z.B.:

`romanesco train -e 25`

Ansonsten habe ich die Standard-Hyperparameter verwendet. Hier eine Auflistung aller Hyperparameter:

- VOCAB_SIZE = 10000
- BATCH_SIZE = 64
- NUM_EPOCHS = 25 (anstatt 10)
- NUM_STEPS = 100
- LEARNING_RATE = 0.001
- HIDDEN_SIZE = 1024
- EMBEDDING_SIZE = 256
- SAMPLE_LENGTH = 100

## Pärpläxitäten

- **1. Training**: 146.43
- **2. Training**: 163.73
