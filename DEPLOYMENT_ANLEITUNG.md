# 🚀 Deployment-Anleitung: Monetarismus-Waage Online

## ✅ FÜR 30 GLEICHZEITIGE NUTZER: GitHub Pages (EMPFOHLEN)

### Warum GitHub Pages?
- ✅ **Kostenlos**
- ✅ **Schnell** (weltweites CDN)
- ✅ **Zuverlässig** (99,9% Uptime)
- ✅ **Skaliert** problemlos für 30+ Nutzer
- ✅ **Kein Server-Setup** nötig

---

## 📋 SCHRITT 1: GitHub Pages aktivieren (2 Minuten)

1. Gehen Sie zu: https://github.com/florianderwein-sketch/Geldmenge

2. Klicken Sie auf **"Settings"** (Zahnrad-Symbol)

3. Im linken Menü: **"Pages"**

4. Bei **"Source"**:
   - Branch: **`claude/fix-monetarism-scale-3i67p`** auswählen
   - Folder: **`/ (root)`**
   - Klicken Sie auf **"Save"**

5. ⏳ Warten Sie 1-2 Minuten

6. Aktualisieren Sie die Seite - Sie sehen dann:
   ```
   ✅ Your site is live at https://florianderwein-sketch.github.io/Geldmenge/
   ```

---

## 📱 SCHRITT 2: QR-Code verwenden

Der QR-Code wurde bereits erstellt: **`qr_code_geldmenge.png`**

### QR-Code anzeigen:
```bash
# Option 1: Als Bild öffnen
open qr_code_geldmenge.png

# Option 2: Für Präsentation
# Öffnen Sie die PNG-Datei und zeigen Sie sie auf einem Beamer/Monitor
```

### URL im QR-Code:
```
https://florianderwein-sketch.github.io/Geldmenge/
```

---

## 👥 SCHRITT 3: Testing mit 30 Personen

### Vorbereitung (5 Minuten vor dem Test):

1. **QR-Code auf Beamer/Monitor anzeigen**
   - Öffnen Sie `qr_code_geldmenge.png`
   - Vergrößern Sie den QR-Code für gute Scannbarkeit

2. **Testlink vorher selbst prüfen:**
   ```
   https://florianderwein-sketch.github.io/Geldmenge/
   ```

3. **WLAN-Verbindung prüfen**
   - Stellen Sie sicher, dass alle Teilnehmer WLAN haben

### Während des Tests:

**Ansage an Teilnehmer:**
```
1. Scannen Sie den QR-Code mit Ihrer Smartphone-Kamera
2. Öffnen Sie den Link
3. Testen Sie die Buttons:
   - Geldpolitik (grün): Geldmenge sinkt
   - BIP-Maßnahmen (braun): BIP steigt
4. Beobachten Sie die Waage und den Inflationsstatus
```

### Was die Teilnehmer sehen:

- **Startansicht:**
  - M3 Geldmenge: 4,10 Bio€
  - BIP: 4,500 Bio€
  - Status: "Geldmengendefizit: 9% → Deflationärer Druck"

- **Nach Geldpolitik-Button (z.B. "Leitzins erhöhen -2%"):**
  - Geldmenge sinkt auf 4,02 Bio€
  - Verhältnis ändert sich
  - Waage kippt nach rechts (mehr deflationär)

- **Nach BIP-Button (z.B. "Investitionen fördern +2%"):**
  - BIP steigt auf 4,59 Bio€
  - Waage kippt nach links
  - Status ändert sich zu stärkerem Defizit

---

## 🎯 TEST-SZENARIEN

### Szenario 1: Inflation bekämpfen (Geldmenge reduzieren)
1. Klick: "Staatsanleihen verkaufen (-3%)"
2. Ergebnis: Geldmenge sinkt, deflationärer Druck steigt

### Szenario 2: Wirtschaft ankurbeln (BIP erhöhen)
1. Klick: "Konsum stimulieren (+2.5%)"
2. Ergebnis: BIP steigt, Verhältnis verbessert sich

### Szenario 3: Ausbalancieren
Ziel: Verhältnis auf 1:1 bringen (Ausgewogen)

---

## 🔧 TECHNISCHE DETAILS

### Performance für 30 Nutzer:
- **GitHub Pages:** ✅ Kein Problem
  - Statisches HTML/CSS/JS
  - Keine Server-Last
  - Läuft komplett im Browser

### Was passiert bei 30 gleichzeitigen Zugriffen?
- ✅ Jeder lädt einmal die HTML-Datei (~5 KB)
- ✅ Alle Berechnungen laufen lokal im Browser
- ✅ Keine Server-Requests nach dem Laden
- ✅ **Total: ~150 KB Traffic = kein Problem**

---

## 📊 MONITORING

Nach dem Test können Sie die Zugriffe hier einsehen:
1. GitHub Repository → **Insights**
2. **Traffic** → Unique visitors

---

## 🚨 TROUBLESHOOTING

### Problem: "Seite nicht erreichbar"
**Lösung:**
- Prüfen Sie, ob GitHub Pages aktiv ist (Settings → Pages)
- Warten Sie 2-3 Minuten nach Aktivierung

### Problem: "QR-Code führt zu 404"
**Lösung:**
- Stellen Sie sicher, dass der Branch `claude/fix-monetarism-scale-3i67p` gewählt ist
- Überprüfen Sie, dass `index.html` im Root liegt

### Problem: "Änderungen nicht sichtbar"
**Lösung:**
- Hard Refresh im Browser: `Strg+Shift+R` (Windows) oder `Cmd+Shift+R` (Mac)
- GitHub Pages Cache braucht ~5 Minuten

---

## ✨ ALTERNATIVE: Lokaler Test (nur Sie)

Falls GitHub Pages nicht sofort verfügbar:

```bash
# Lokaler Webserver (bereits gestartet)
http://localhost:8000/index.html
```

**⚠️ ABER:** Nur für lokales Testing - NICHT für 30 externe Personen geeignet!

---

## 📝 FEEDBACK SAMMELN

Während des Tests:
- [ ] Funktioniert die Waage visuell?
- [ ] Sind die Button-Effekte klar?
- [ ] Ist die Interpretation verständlich?
- [ ] Gibt es Performance-Probleme?
- [ ] Ist das Design auf verschiedenen Handys gut lesbar?

---

## 🎉 NACH DEM TEST

Nach erfolgreichem Test können Sie:
1. Pull Request erstellen (Branch → Main mergen)
2. Domain einrichten (z.B. geldmenge.deinedomain.de)
3. Google Analytics einbauen (optional)

---

**Viel Erfolg beim Testing! 🚀**
