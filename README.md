# Beetmomente Ratgeber

Gartenbeiträge für den Ratgeber der App **Beetmomente** (Bereich
„Wissen → Ratgeber“). Die App lädt die Beiträge direkt aus diesem
Repository.

## Ohne Gewähr

Alle Angaben in diesem Repository sind sorgfältig zusammengestellt, aber
**ohne Gewähr**. Sie ersetzen keine fachliche Beratung. Garten, Boden,
Klima und Pflanzen sind verschieden; prüfe die Hinweise für deine
Bedingungen. Eine Haftung für Schäden aus der Nutzung der Inhalte ist
ausgeschlossen, soweit das gesetzlich zulässig ist.

## Lizenz und Namensnennung

Die Texte stehen unter der Lizenz
[Creative Commons Namensnennung 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.de),
vollständiger Text in [`LICENSE`](LICENSE).

Du darfst die Beiträge teilen und bearbeiten, auch kommerziell, wenn du
**die Quelle nennst und auf dieses Repository verweist**, zum Beispiel:

> Text: „Garten winterfest machen“ aus dem
> [Beetmomente Ratgeber](https://github.com/FlyingKaenguru/beetmomente-ratgeber),
> Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de),
> eigene Änderungen gekennzeichnet.

Gib dabei an, ob du den Text verändert hast.

© 2026 FlyingKaenguru (Beetmomente)

## Beiträge und Änderungen

Hinweise und Korrekturen gern als Issue oder Pull Request. Zusammengeführt
wird nur von der Inhaberin des Repositorys; der Branch `main` ist
geschützt.

## Aufbau

```
index.json                    Inhaltsverzeichnis
garten-winterfest-machen.md   ein Beitrag je Datei
LICENSE                       CC BY 4.0
scripts/check.py              Prüfung (Verzeichnis, Länge, Stil)
.github/workflows/check.yml   führt die Prüfung bei Pull Requests aus
```

### index.json

```json
{
  "schema_version": 1,
  "articles": [
    {
      "id": "garten-winterfest-machen",
      "title": "Garten winterfest machen",
      "summary": "Beete, Stauden, Kübel und Leitungen gut durch den Winter bringen.",
      "file": "garten-winterfest-machen.md",
      "updated": "2026-11-15",
      "reading_minutes": 3,
      "tags": ["Herbst", "Winter"],
      "months": [10, 11, 12],
      "plants": []
    }
  ]
}
```

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `schema_version` | ja | Formatversion, derzeit `1`. Höhere Versionen ignoriert die App. |
| `id` | ja | Eindeutig, ändert sich nie (Kleinbuchstaben, Bindestriche). |
| `title` | ja | Titel (zeigt die App oben an). |
| `summary` | ja | Ein, zwei Sätze für die Liste. |
| `file` | ja | Dateiname, nur `a-z`, `0-9`, `-`, endet auf `.md`. |
| `updated` | ja | Datum der letzten inhaltlichen Änderung (`JJJJ-MM-TT`). **Bei jeder Änderung erhöhen**, nur dann lädt die App den Text neu. |
| `reading_minutes` | nein | Lesezeit, rund 200 Wörter pro Minute. |
| `tags` | nein | Stichworte. |
| `months` | nein | Monate (1–12), in denen der Beitrag passt. |
| `plants` | nein | IDs der Pflanzenprofile der App (z. B. `tomate`). |

Fehlerhafte Einträge überspringt die App, der Rest bleibt sichtbar.

### Beiträge

- Markdown, **ohne** Überschrift erster Ebene (`# …`), den Titel zeigt die
  App. Abschnitte mit `##`.
- Stil: du-Form, kurze Sätze, keine Ausrufezeichen, keine Binde- oder
  Gedankenstriche.
- Länge: **höchstens etwa 3 Minuten Lesezeit**, also höchstens rund
  600 Wörter (200 Wörter pro Minute). Längere Themen auf mehrere Beiträge
  aufteilen.
- `scripts/check.py` prüft Verzeichnis, Länge, Lesezeit und Stil; die
  GitHub Action führt es bei jedem Pull Request aus.
- Am Ende jedes Beitrags der Hinweis „Alle Angaben ohne Gewähr“ mit
  Quelle und Lizenz.
- Keine Bilder von fremden Servern; die App zeigt sie nicht an.
- Höchstens 256 KB je Datei, höchstens 50 Beiträge.

## Wie die App lädt

- Beim Öffnen des Ratgebers höchstens einmal am Tag, über den Knopf
  „Aktualisieren“ oder durch Ziehen nach unten; nur wenn „Ratgeber online
  aktualisieren“ in den Einstellungen der App an ist.
- Quelle: `https://raw.githubusercontent.com/FlyingKaenguru/beetmomente-ratgeber/main/…`.
  GitHub hält Dateien dort einige Minuten im Zwischenspeicher.
- Geladen werden nur neue oder geänderte Beiträge (nach `updated`). Ohne
  Netz zeigt die App den zuletzt geladenen Stand.
