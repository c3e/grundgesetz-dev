#   Grundgesetz-dev (gg-dev)

Dieses Repository dient als Grundlage zum Aufbau eines versionierten Grundgesetzes der Bundesrepublik Deutschland. Dieses Projekt sprich dieses Repository gilt als erster Meilenstein in der Entwicklung von versionierten Dokumenten mit dem Tool mit _[DocPatch](https://wiki.die-foobar.org/wiki/DocPatch)_.

#   Handhabung

Beschäftigen Dich eine oder mehrere der folgenden Fragen, dann bist Du hier genau richtig: Wie gehst Du am Besten vor, wenn Du ...

*   aus den Quellen dieses Repositories ein versioniertes Grundgesetzes erstellen möchtest?
*   aus den Quellen eines versionierten Grundgesetzes verschiedene Ausgabeformate erstellen möchtest?
*   Dich an der Entwicklung beteiligen möchtest?

##  Voraussetzungen

Bevor wir Dir die oben gestellten Fragen konkret beantworten können, solltest Du Dich vorher intensiv mit _DocPatch_ und unseren Zielen auseinandergesetzt haben. Auch schadet es nicht, sich mit dem Gesetzestext und dem nötigen Vokabular zu beschäftigen.

Bitte installiere _DocPatch_ mit allen Abhängigkeiten und wechsel in das Hauptverzeichnis dieses Repositories.

##   Dateistruktur

Dieses Repository enthält die folgende Dateistruktur:

*   `etc/`: Konfigurations- und weitere Dateien
    *   `docpatch.conf`: Konfigurationsdatei für _DocPatch_
    *   `meta-info.txt`: Beschreibung der Metadaten über eine Gesetztesänderung
    *   `meta.template`: Vorlage einer Metadaten-Datei für Gesetzesänderungen
*   `meta/`: Dateien mit Metadaten über Gesetzesänderungen nach dem Schema `[n].meta`, wobei `n` die fortlaufende Nummer der Änderung darstellt
*   `out/`: aus den Quellen des versionierten Gesetzestextes erstellte Ausgabeformate
*   `ref/`: Referenzen, Quellenangaben, mitgelieferte Quellen
*   `repo/`: aus den Quellen dieses Repositories versioniertes Grundgesetz
*   `src/`: Gesetzestexte; pro Datei ein Artikel nach dem Schema `[n].md`, wobei `n` die Artikelnummer und `md` die Dateiendung für in Markdown verfasste Texte ist
*   `tpl/`: Vorlagen für die Ausgabeformate

##  Erstellen eines versionierten Grundgesetzes aus den Quellen dieses Repositories

FIXME

##  Erstellen verschiedener Ausgabeformate aus den Quellen eines versionierten Grundgesetzes

FIXME

##  Mitwirken und Entwicklung

#   Roadmap/ToDo

*   Inkrafttreten von Änderung 53?
*   Unterschriften von Änderung 17?
*   Änderung 58: FIXME
*   "Überschriften" der Artikel berücksichtigen 
*   Professionelle Vorlagen erstellen/verwenden
    *   Vorschlag: [Dokumentenvorlage für juristische Texte in LaTeX](http://www.jurawiki.de/LaTeX)
*   Referenzen im bibtex-Format statt in der Datei `reference.md`

#   Siehe auch

*   _DocPatch_:
    *   Website: <https://wiki.die-foobar.org/wiki/DocPatch>
    *   Tools auf GitHub: <https://github.com/bheisig/DocPatch>
*   Grundgesetz der Bundesrepublik Deutschland:
    *   Artikel auf Wikipedia: <>
    *   Gesetzestext, bereitgestellt von der Juris GmbH: <>
