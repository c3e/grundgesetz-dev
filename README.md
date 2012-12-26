#   Grundgesetz für die Bundesrepublik Deutschland (grundgesetz-dev)

Dieses Projekt dient als Grundlage zum Aufbau eines versionierten Grundgesetzes für die Bundesrepublik Deutschland. Dieses Projekt sprich dieses Repository gilt als erster Meilenstein in der Entwicklung von versionierten Dokumenten`.


##  Hintergrund

Dieses Projekt ist Teil der Open-Data-Bewegung und unterliegt der [Open Definition](http://opendefinition.org/okd/). Unser **Ziel** ist, öffentliche Daten leicht zugänglich zu machen; unser **Weg** ist, freie Software und freie Formate für unsere Arbeit zu verwenden; unsere **Idee** ist, das Grundgesetz für die Bundesrepublik Deutschland als _das_ Beispiel für öffentliche Daten wie Verfassungen und Gesetzestexte zu von unfreien Formaten zu "befreien" und in einer umfassenden Gänze zu erschließen.

Gesetzestexte sind wie Software: der "Quelltext" ist gut strukturiert mit einfacher Syntax und Änderungen sind auch nichts anderes als Patches, um Fehler zu beseitigen oder neuen Anforderungen zu genügen. Das jedenfalls dachten wir uns vor einigen Jahren. Wie wäre es, ein Gesetz wie ein Stück Software zu behandeln, zu versionieren und zu patchen? Software-Entwickler nehmen für diese Tätigkeiten Versionskontrollsysteme wie `[git](http://git-scm.com/)`. Damit kann man nachvollziehen, wer wann was und warum geändert hat. Als Syntax nahmen wir das leicht verständliche und weit verbreitete `[markdown](http://daringfireball.net/projects/markdown/)`, das sich wie einfacher Text liest. Um die Gesetzestexte in schöne Formate konvertieren zu können, entschieden wir uns für das mächtige `[pandoc](http://johnmacfarlane.net/pandoc/index.html)`, das unser verwendetes `markdown` mit sinnvoller anreichert. Die Patches haben wir dem kleinen, aber feinen Tool `quilt` erstellt. Den letzten Schliff gaben wir dem Projekt mit der selbstgeschriebenen Software `[DocPatch](https://github.com/bheisig/DocPatch)`.

Wir beschränken uns nicht auf den reinen Text und die Änderungen, sondern gehen einen Schritt weiter: Mit Hilfe von weiteren strukturierten Daten ("Metadaten") stellen wir den Text als solches und alle Änderungen in einen größeren Kontext: Wann wurde eine Änderung verabschiedet? Wer hat sie initiiert, wer unterschrieben? Das sind alles Fragen, die wir versuchen zu beantworten.


##  Handhabung

Beschäftigen Dich eine oder mehrere der folgenden Fragen, dann bist Du hier genau richtig: Wie gehst Du am Besten vor, wenn Du ...

*   aus den Quellen dieses Repositories ein versioniertes Grundgesetzes erstellen möchtest?
*   aus den Quellen eines versionierten Grundgesetzes verschiedene Ausgabeformate erstellen möchtest?
*   Dich an der Entwicklung beteiligen möchtest?


### Voraussetzungen

Bevor wir Dir die oben gestellten Fragen konkret beantworten können, solltest Du Dich vorher intensiv mit `DocPatch` und unseren Zielen auseinandergesetzt haben. Auch schadet es nicht, sich mit dem Gesetzestext und dem nötigen Vokabular zu beschäftigen.

Bitte installiere `DocPatch` mit allen Abhängigkeiten und wechsle in das Hauptverzeichnis dieses geklonten Repositories.


### Dateistruktur

Dieses Repository enthält die folgende Dateistruktur:

*   `etc/`: Konfigurations- und weitere Dateien
    *   `docpatch.conf`: Konfigurationsdatei für _DocPatch_
    *   `meta-info.txt`: Beschreibung der Metadaten über eine Gesetztesänderung
    *   `meta.template`: Vorlage einer Metadaten-Datei für Gesetzesänderungen
    *   `meta.json`: Meta-Informationen im JSON-Format
*   `meta/`: Dateien mit Metadaten über Gesetzesänderungen nach dem Schema `[n].meta`, wobei `n` die fortlaufende Nummer der Änderung darstellt
*   `out/`: aus den Quellen des versionierten Gesetzestextes erstellte Ausgabeformate
*   `ref/`: Referenzen, Quellenangaben, mitgelieferte Quellen
*   `repo/`: aus den Quellen dieses Repositories versioniertes Grundgesetz
*   `src/`: Gesetzestexte; pro Datei ein Artikel nach dem Schema `[n].md`, wobei `n` die Artikelnummer mit füllenden Nullen und `md` die Dateiendung für in Markdown verfasste Texte ist
*   `tpl/`: Vorlagen für die Ausgabeformate


### Erstellen eines versionierten Grundgesetzes aus den Quellen dieses Repositories

Laut der Anleitung von `DocPatch` benötigt Du dafür nur folgenden Aufruf in der Kommandozeile:

    docpatch build

Das Repository wird unter `repo` erstellt. Mehr Optionen verrät Dir die Hilfe `docpatch build --help` bzw. die Man Page `man docpatch-build`.


### Erstellen verschiedener Ausgabeformate aus den Quellen eines versionierten Grundgesetzes

Der vorherige Schritt gilt als Voraussetzung für diesen. Mit dem Kommando

    docpatch create --format pdf --revision 0

erstellst Du im Ordner `out/` den Gesetzestext im PDF-Format in der allerersten Version (`0`). Alle unterstützten Formate und Optionen sind in der Hilfe `docpatch create --help` bzw. in der Man Page `docpatch-create` zu finden.


### Mitwirken und Entwicklung

Wir sind immer auf der Suche nach Menschen und Maschinen, die uns tatkräftig unterstützen wollen -- sei es durch kreative Mithilfe, Spenden von Dienst- oder Sachleistungen. Melde Dich, wenn Du Dich für die "Befreiung Deiner Grundrechte" interessierst ;-)

Hast Du eine tolle Idee, was wir unbedingt umsetzen sollten? Hast Du einen Fehler gefunden? Hast Du Vorschläge, wie wir etwas besser machen können? Wir benutzen den GitHub-eigenen Issue Tracker für jegliche Anfragen solcher Art: <https://github.com/bheisig/grundgesetz-dev/issues>.


##  Quellen

*   "[Bundesgesetzblatt Online-Abonnement](http://www1.bgbl.de/informationen/bgbl-online.html)"; detailierte Angaben befinden sich in den jeweiligen Meta-Informationen der versionierten Gesetzesänderungen.
*   Steffi Menzenbach, Anja Netterscheidt, Maren Beckebanze, Lena Kuhn: "[Änderungen des Grundgesetzes seit 1949 -- Inhalt, Datum, Abstimmungsergebnis und Textvergleich](http://www.bundestag.de/dokumente/analysen/2009/aenderungen_des_grundgesetzes_seit_1949.pdf)" (PDF), 2009, Wissenschaftliche Dienste, Deutscher Bundestag
*   Steffi Menzenbach, Patrizia Robbe, Lena Kuhn, Karolin Wilcke: "[60 Jahre Grundgesetz -- Zahlen und Fakten](http://www.bundestag.de/dokumente/analysen/2009/60_Jahre_Grundgesetz.pdf)" (PDF), 2009, Wissenschaftliche Dienste, Deutscher Bundestag


##  Roadmap/ToDo

*   Logo
*   Historie rund um den Vertrag von Lissabon
    *   Inkrafttreten von Änderung 53
    *   Nummerierung ab Änderung 58
*   Unterschriften von Änderung 17
*   "Überschriften" der Artikel berücksichtigen 
*   Professionelle Vorlagen erstellen/verwenden
    *   Vorschlag: [Dokumentenvorlage für juristische Texte in LaTeX](http://www.jurawiki.de/LaTeX)
*   Referenzen im bibtex-Format
*   Git Commit Messages durch `meta.json` erstellen
*   Website mit Community-Funktionen
    *   Kommentierung
    *   Änderungsvorschläge
*   Automatische Übersetzungen
*   Artikel des Tages (fortune)
*   Zeitleiste
    *   Historische Einordnung
    *   Bilder, Videos usw.
    *   Wikipedia: passender Jahres-/Monats-/Tages-Artikel
*   Meta-Informationen
    *   Personenverzeichnis
    *   Wikipedia-Artikel
    *   Hintergründe/Kontext recherchieren (Warum gab es eine Änderung?)


##  Mitwirkende

*   Initiert durch eine Diskussion zwischen Hauro und Lars
*   Erste wichtige Schritte durch [Ben](https://benjamin.heisig.name/), Björn und Hauro
*   Software von Ben
*   Patch-Marathon mit Ben, Gammlaa und Schnitzel
*   Mit vielen Ideen aus dem Umfeld von [Chaospott](http://chaospott.de/) und [foobar e. V.](https://wiki.die-foobar.de/)


##  Siehe auch

*   _DocPatch_:
    *   Website: <https://wiki.die-foobar.de/wiki/DocPatch>
    *   Tools auf GitHub: <https://github.com/bheisig/DocPatch>
*   Grundgesetz für die Bundesrepublik Deutschland:
    *   Artikel auf Wikipedia "Grundgesetz für die Bundesrepublik Deutschland": <https://de.wikipedia.org/wiki/Grundgesetz_f%C3%BCr_die_Bundesrepublik_Deutschland>
    *   Artikel auf Wikipedia "Liste der Artikel des Grundgesetzes": <https://de.wikipedia.org/wiki/Liste_der_Artikel_des_Grundgesetzes>
    *   Gesetzestext, bereitgestellt von der Juris GmbH: <http://www.gesetze-im-internet.de/gg/index.html>
    *   Historisch-synoptische Edition: <http://lexetius.com/GG>


##  Lizenzen und Urheberrecht

Laut [UrhG §5](http://www.gesetze-im-internet.de/urhg/__5.html) genießen amtliche Werke das Grundgesetz für die Bundesrepublik Deutschland kein Urheberrecht. Allerdings gilt dies nicht für die Bundesgesetzblätter, in denen die Gesetzesänderungen verkündet werden, die von der Juris GmbH aufbereiteten Inhalte sowie für die unter in den [Quellen](#quellen) genannten Schriftwerke.

Von uns verwendetete Software und Formate sind konsequent offengelegt.

