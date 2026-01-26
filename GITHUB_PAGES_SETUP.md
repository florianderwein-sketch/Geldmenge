# 🚀 GitHub Pages Aktivierung - Schritt-für-Schritt Anleitung

## ⏱️ Zeitaufwand: 2-3 Minuten

---

## SCHRITT 1: Repository öffnen

1. Öffnen Sie Ihren Browser
2. Gehen Sie zu:
   ```
   https://github.com/florianderwein-sketch/Geldmenge
   ```
3. **Loggen Sie sich ein**, falls noch nicht geschehen

---

## SCHRITT 2: Settings öffnen

1. Oben auf der Repository-Seite sehen Sie Tabs:
   ```
   < > Code    Issues    Pull requests    Actions    Projects    Settings
   ```

2. Klicken Sie ganz rechts auf **⚙️ Settings**

   ⚠️ **WICHTIG:** Falls Sie "Settings" nicht sehen:
   - Sie haben keine Admin-Rechte für das Repository
   - Nur der Repository-Owner kann GitHub Pages aktivieren
   - Fragen Sie den Owner, es für Sie zu aktivieren

---

## SCHRITT 3: Pages-Menü finden

1. Im **linken Seitenmenü** scrollen Sie nach unten
2. Unter der Kategorie **"Code and automation"** finden Sie:
   ```
   □ Environments
   ▶ Pages          ← HIER KLICKEN!
   □ Webhooks
   ```

3. Klicken Sie auf **Pages**

---

## SCHRITT 4: GitHub Pages konfigurieren

Sie sehen jetzt die GitHub Pages Konfiguration:

### A) Source-Bereich finden

Suchen Sie den Bereich **"Build and deployment"** → **"Source"**

### B) Branch auswählen

1. Klicken Sie auf das **Branch-Dropdown**
   - Steht aktuell auf "None" oder "main"

2. Wählen Sie aus der Liste:
   ```
   claude/fix-monetarism-scale-3i67p
   ```

3. Das **Folder-Dropdown** bleibt auf:
   ```
   / (root)
   ```

### C) Speichern

4. Klicken Sie auf den blauen **"Save"** Button

---

## SCHRITT 5: Warten & Verifizieren

### Nach dem Speichern:

1. **Blauer Banner erscheint:**
   ```
   ✓ GitHub Pages source saved
   ```

2. **Seite lädt neu** - warten Sie 30 Sekunden

3. **Reload** die Seite (F5 oder ⌘+R)

4. Nach 1-2 Minuten erscheint ein **grüner Banner:**
   ```
   ✅ Your site is live at https://florianderwein-sketch.github.io/Geldmenge/
   ```

---

## SCHRITT 6: Testen

1. Klicken Sie auf den Link:
   ```
   https://florianderwein-sketch.github.io/Geldmenge/
   ```

2. Die Monetarismus-Waage sollte erscheinen!

3. **Testen Sie:**
   - ✅ Waage ist sichtbar
   - ✅ Status am unteren Rand sichtbar
   - ✅ Buttons funktionieren
   - ✅ Auf Smartphone: Touch funktioniert

---

## SCHRITT 7: QR-Code nutzen

### Option A: Vorhandenen QR-Code verwenden

Der QR-Code ist bereits erstellt für genau diese URL!

**Datei-Pfad:**
```
/home/user/Geldmenge/qr_code_geldmenge.png
```

**So nutzen Sie ihn:**

1. **Auf Beamer/Monitor:**
   - Öffnen Sie `qr_code_geldmenge.png`
   - Vollbild anzeigen
   - 30 Leute scannen lassen mit Smartphone-Kamera

2. **Ausdrucken:**
   - QR-Code ausdrucken (A4)
   - An Wand hängen oder auf Tisch legen
   - Scannen lassen

3. **Per E-Mail/Chat:**
   - QR-Code als Attachment verschicken
   - Leute können vom Bildschirm scannen

---

## 🆘 TROUBLESHOOTING

### Problem 1: "Settings" nicht sichtbar

**Lösung:**
- Sie sind nicht Admin/Owner des Repos
- Kontaktieren Sie den Repository-Owner
- Owner muss GitHub Pages aktivieren

---

### Problem 2: Branch nicht in der Liste

**Prüfen Sie:**
```bash
# Im Terminal:
git branch -r | grep claude/fix-monetarism-scale-3i67p
```

Wenn leer → Branch wurde nicht gepusht.

**Lösung:**
```bash
git push -u origin claude/fix-monetarism-scale-3i67p
```

---

### Problem 3: 404 nach Aktivierung

**Das ist normal!** GitHub Pages braucht 1-3 Minuten zum Bauen.

**Lösung:**
1. Warten Sie 2-3 Minuten
2. Laden Sie die Seite neu (Strg+Shift+R)
3. Leeren Sie Browser-Cache

---

### Problem 4: "Some of your repository's code may not be ready to host"

**Ignorieren Sie diese Warnung!**

Das ist eine generische Warnung. Ihre Single-File-App funktioniert perfekt.

---

### Problem 5: QR-Code führt zu 404

**Mögliche Ursachen:**

A) **GitHub Pages noch nicht fertig**
   - Warten Sie 2-3 Minuten
   - Testen Sie die URL manuell im Browser

B) **Falscher Branch ausgewählt**
   - Prüfen Sie: Ist `claude/fix-monetarism-scale-3i67p` gewählt?
   - Nicht "main" oder "master"

C) **Repository ist privat**
   - GitHub Pages funktioniert nur bei öffentlichen Repos (Free Account)
   - Oder: GitHub Pro/Team Account nötig für private Repos

---

## ✅ ERFOLGSKRITERIEN

Ihre GitHub Pages ist korrekt aktiviert, wenn:

- ✅ Grüner Banner: "Your site is live at..."
- ✅ URL funktioniert im Browser
- ✅ URL funktioniert auf Smartphone
- ✅ QR-Code öffnet die richtige Seite

---

## 🎯 CHECKLISTE FÜR 30-PERSONEN-TEST

### Vor dem Test (5 Min):

- [ ] GitHub Pages aktiviert & getestet
- [ ] URL funktioniert: https://florianderwein-sketch.github.io/Geldmenge/
- [ ] QR-Code bereit (qr_code_geldmenge.png)
- [ ] QR-Code auf Beamer/Bildschirm angezeigt
- [ ] Eigenes Smartphone getestet (Touch-Targets funktionieren?)
- [ ] WLAN für Teilnehmer verfügbar

### Während dem Test:

- [ ] QR-Code gut sichtbar für alle
- [ ] Teilnehmer scannen und öffnen Link
- [ ] Alle können Waage sehen
- [ ] Buttons funktionieren (Touch-Feedback sichtbar)
- [ ] Status am unteren Rand immer sichtbar

### Nach dem Test:

- [ ] Feedback sammeln
- [ ] Performance-Probleme notiert?
- [ ] UX-Verbesserungen identifiziert?

---

## 📱 ANSAGE AN TEILNEHMER

**Sagen Sie den Teilnehmern:**

```
1. Scannen Sie den QR-Code mit Ihrer Smartphone-Kamera
2. Tippen Sie auf den Link, der erscheint
3. Die Waage zeigt aktuell "Inflation: 22%"
4. Testen Sie die ROTEN Buttons (Geldpolitik gegen Inflation)
   → Beobachten Sie: Inflation sinkt!
5. Testen Sie die GRÜNEN Buttons (Geldpolitik gegen Deflation)
   → Beobachten Sie: Kann zu Inflation führen!
6. Testen Sie die BRAUNEN Buttons (Fiskalpolitik)
   → BIP steigt → Verhältnis ändert sich
7. Tippen Sie "Zurücksetzen" für Neustart
```

---

## 🔗 WICHTIGE LINKS

**Ihre GitHub Pages URL:**
```
https://florianderwein-sketch.github.io/Geldmenge/
```

**Repository:**
```
https://github.com/florianderwein-sketch/Geldmenge
```

**GitHub Pages Einstellungen:**
```
https://github.com/florianderwein-sketch/Geldmenge/settings/pages
```

---

## 💡 TIPP: Custom Domain (Optional)

Falls Sie eine eigene Domain haben (z.B. geldmenge.ihredomain.de):

1. GitHub Pages Settings → Custom domain
2. Domain eintragen
3. DNS-Einträge bei Domain-Provider anpassen
4. Neuen QR-Code für Custom Domain erstellen

---

**Viel Erfolg beim Test! 🚀**
