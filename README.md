#   Grundgesetz für die Bundesrepublik Deutschland (grundgesetz-dev)

Dieses [Repository](https://github.com/bheisig/grundgesetz-dev) ermöglicht das Nachvollziehen aller Veränderungen am Grundgesetz für die Bundesrepublik Deutschland seit seinem Inkrafttreten im Jahr 1949. Es enthält den vollständigen Gesetzestext zuzüglich vieler Informationen, die damit in Verbindung stehen. Somit steht ein umfassendes Werk zur Verfügung, die Entwicklung der deutschen Verfassung transparenter zu machen.


##  Hintergrund

Dieses Projekt ist Teil der Open-Data-Bewegung und unterliegt der [Open Definition](http://opendefinition.org/okd/). Unser **Ziel** ist, öffentliche Daten leicht zugänglich zu machen; unser **Weg** ist, freie Software und freie Formate für unsere Arbeit zu verwenden; unsere **Idee** ist, das Grundgesetz für die Bundesrepublik Deutschland als _das_ Beispiel für öffentliche Daten wie Verfassungen und Gesetzestexte von unfreien Formaten zu "befreien" und umfassend zu erschließen.

Gesetzestexte sind wie Software: der "Quelltext" ist gut strukturiert mit einfacher Syntax und Änderungen sind auch nichts anderes als Patches, um Fehler zu beseitigen oder neuen Anforderungen zu genügen. Das jedenfalls dachten wir uns vor einiger Zeit. Wie wäre es, ein Gesetz wie ein Stück Software zu behandeln, zu versionieren und zu patchen? Softwareentwickler benutzen dafür Versionskontrollsysteme wie [`git`](http://git-scm.com/). Damit kann man nachvollziehen, wer wann was und warum geändert hat. Als Syntax nahmen wir das leicht verständliche und weit verbreitete [`markdown`](http://daringfireball.net/projects/markdown/), das sich wie einfacher Text liest. Um die Gesetzestexte in schöne Formate konvertieren zu können, entschieden wir uns für das mächtige [`pandoc`](http://johnmacfarlane.net/pandoc/index.html), das unser verwendetes `markdown` mit sinnvoller Syntax anreichert. Die Patches haben wir mit dem kleinen, aber feinen Tool [`quilt`](http://savannah.nongnu.org/projects/quilt) erstellt. Den letzten Schliff gaben wir dem Projekt mit der selbst geschriebenen Software [`DocPatch`](https://github.com/bheisig/DocPatch).

Wir beschränken uns nicht auf den reinen Text und die Änderungen, sondern gehen einen Schritt weiter: Mit Hilfe von weiteren strukturierten Daten ("Metadaten") stellen wir den Text als solches und alle Änderungen in einen größeren Kontext: Wann wurde eine Änderung verabschiedet? Wer hat sie initiiert, wer unterschrieben? Das sind alles Fragen, die wir versuchen zu beantworten.


##  Handhabung

Beschäftigen Dich eine oder mehrere der folgenden Fragen, dann bist Du hier genau richtig: Wie gehst Du am Besten vor, wenn Du ...

*   aus den Quellen dieses Repositories ein versioniertes Grundgesetzes erstellen möchtest?
*   aus den Quellen eines versionierten Grundgesetzes verschiedene Ausgabeformate erstellen möchtest?
*   Dich an der Entwicklung beteiligen möchtest?


### Voraussetzungen

Bevor wir Dir die oben gestellten Fragen konkret beantworten können, solltest Du Dich vorher intensiv mit `DocPatch` und unseren Zielen auseinandergesetzt haben. Auch schadet es nicht, sich mit dem Gesetzestext und dem nötigen Vokabular zu beschäftigen.

Bitte installiere [`DocPatch`](https://github.com/bheisig/DocPatch) mit allen Abhängigkeiten und wechsle in das Hauptverzeichnis dieses geklonten Repositories.


### Dateistruktur

Dieses Repository enthält die folgende Dateistruktur:

*   `etc/`: Konfigurations- und weitere Dateien
    *   `docpatch.conf`: Konfigurationsdatei für _DocPatch_
    *   `meta-info.txt`: Beschreibung der Metadaten über eine Gesetzesänderung
    *   `meta.template`: Vorlage einer Metadaten-Datei für Gesetzesänderungen
    *   `meta.json`: Meta-Informationen im JSON-Format
*   `meta/`: Dateien mit Metadaten über Gesetzesänderungen nach dem Schema `[n].meta`, wobei `n` die fortlaufende Nummer der Änderung darstellt
*   `out/`: aus den Quellen des versionierten Gesetzestextes erstellte Ausgabeformate
*   `ref/`: Referenzen, Quellenangaben, mitgelieferte Quellen
*   `repo/`: aus den Quellen dieses Repositories versioniertes Grundgesetz
*   `src/`: Gesetzestexte; pro Datei ein Artikel nach dem Schema `[n].md`, wobei `n` die Artikelnummer mit füllenden Nullen und `md` die Dateiendung für in Markdown verfasste Texte ist
*   `tpl/`: Vorlagen für die Ausgabeformate


### Erstellen eines versionierten Grundgesetzes aus den Quellen dieses Repositories

Laut der Anleitung von `DocPatch` benötigst Du dafür nur folgenden Aufruf in der Kommandozeile:

    docpatch build

Das Repository wird unter `repo` erstellt. Mehr Optionen verrät Dir die Hilfe `docpatch build --help` bzw. die Man Page `man docpatch-build`.


### Erstellen verschiedener Ausgabeformate aus den Quellen eines versionierten Grundgesetzes

Der vorherige Schritt gilt als Voraussetzung für diesen. Mit dem Kommando

    docpatch create --format pdf --revision last

erstellst Du im Ordner `out/` den Gesetzestext im PDF-Format mit allen Änderungen. Alle unterstützten Formate und Optionen sind in der Hilfe `docpatch create --help` bzw. in der Man Page `docpatch-create` zu finden.


## Mitwirken und Entwicklung

Wir sind ständig auf der Suche nach Menschen und Maschinen, die uns tatkräftig unterstützen möchten -- sei es durch kreative Mithilfe, Spenden von Dienst- oder Sachleistungen. Melde Dich, wenn Du Dich für die "Befreiung Deiner Grundrechte" interessierst ;-)

Hast Du eine tolle Idee, was wir unbedingt umsetzen sollten? Hast Du einen Fehler gefunden? Hast Du Vorschläge, wie wir etwas besser machen können? Wir benutzen den [GitHub-eigenen Issue Tracker](https://github.com/bheisig/grundgesetz-dev/issues) für jegliche Anfragen solcher Art.


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

Hinter DocPatch stehen Freiwillige, die sich in ihrer Freizeit tatkräftig einsetzen:

*   Initiiert durch eine Diskussion zwischen Hauro und [Lars Sobiraj](http://lars-sobiraj.de/)
*   Erste wichtige Schritte durch [Benjamin Heisig](http://benjamin.heisig.name/), Björn und Hauro
*   Software von Benjamin Heisig
*   Patch-Marathon mit Benjamin Heisig, Gammlaa und Schnitzel
*   Webseite von Benjamin Heisig, Haggis McMutton und Schnitzel
*   Zahlreiche Vorschläge und Verbesserungen von Bernhard Físseni
*   Öffentlichkeitsarbeit durch Lars Sobiraj
*   Mit vielen Ideen aus dem Umfeld von [Chaospott Essen](http://chaospott.de/) und [foobar e. V.](http://wiki.die-foobar.de/)


##  Kontakt

Wer mit uns in Kontakt treten möchte, möge sich bitte direkt an [Benjamin Heisig](http://benjamin.heisig.name/) wenden oder indirekt die üblichen [Kommunikationskanäle des Chaospott Essen](http://wiki.die-foobar.de/wiki/Foobar) bemühen.


##  Sonstiges

*   Der aktuelle Gesetzestext trotzt der Rechtschreibreform von 1996 und verwendet sowohl die alte als auch die neue deutsche Rechtschreibung nebeneinander.
*   Das Entfernen von Artikeln durch das Ersetzen des Artikelinhalts durch "[aufgehoben]" weicht nur an einer Stelle ab: In der 12. Revision wird der Artikel 96 durch den Inhalt von 96a ersetzt und 96a vollständig entfernt.


##  Siehe auch

*   _DocPatch_:
    *   Website: <http://wiki.die-foobar.de/wiki/DocPatch>
    *   Tools auf GitHub: <https://github.com/bheisig/DocPatch>
*   Grundgesetz für die Bundesrepublik Deutschland:
    *   Artikel auf Wikipedia "Grundgesetz für die Bundesrepublik Deutschland": <https://de.wikipedia.org/wiki/Grundgesetz_f%C3%BCr_die_Bundesrepublik_Deutschland>
    *   Artikel auf Wikipedia "Liste der Artikel des Grundgesetzes": <https://de.wikipedia.org/wiki/Liste_der_Artikel_des_Grundgesetzes>
    *   Gesetzestext, bereitgestellt von der Juris GmbH: <http://www.gesetze-im-internet.de/gg/index.html>
    *   Historisch-synoptische Edition: <http://lexetius.com/GG>


##  Lizenzen und Urheberrecht

Laut [UrhG §5](http://www.gesetze-im-internet.de/urhg/__5.html) genießen amtliche Werke wie das Grundgesetz für die Bundesrepublik Deutschland kein Urheberrecht. Allerdings gilt dies nicht für die vom Bundesanzeiger Verlag herausgegebenen Bundesgesetzblätter, in denen die Gesetzesänderungen verkündet werden, die von der Juris GmbH aufbereiteten Inhalte sowie für die unter in den [Quellen](#quellen) genannten Schriftwerke.

Von uns verwendete Software und Formate sind konsequent offen gelegt.

Selbst erarbeitete Inhalte stehen unter einer [Creative-Commons-Lizenz CC BY-SA 3.0 DE](http://creativecommons.org/licenses/by-sa/3.0/de/).

