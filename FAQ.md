# FAQ – Monetarismus-Simulation: Interaktive Waage

## 📚 Allgemeine Fragen

### **Was ist dieses Tool?**
Ein interaktives Bildungstool zur Veranschaulichung monetaristischer Grundkonzepte. Es simuliert die Beziehung zwischen Geldmenge (M3), Wirtschaftsleistung (BIP) und Inflation anhand einer visuellen Waage.

### **Für wen ist dieses Tool gedacht?**
- **Studierende** der Wirtschaftswissenschaften (Grundstudium)
- **Schüler** in der Oberstufe (Wirtschaftskurse)
- **Interessierte Laien**, die monetaristische Konzepte verstehen möchten
- **Lehrkräfte** zur Veranschaulichung im Unterricht

### **Ist dieses Tool kostenlos?**
Ja, vollständig kostenlos und Open Source (siehe GitHub-Repository).

---

## 🎓 Pädagogische Fragen

### **Warum zeigt das Tool nicht die reale Inflationsrate?**
Das Tool verwendet ein **didaktisch vereinfachtes Modell** basierend auf der Quantitätsgleichung:
```
M × V = P × Y
```

**Vereinfachungen:**
- Umlaufgeschwindigkeit (V) = 1 (konstant)
- Keine Erwartungsbildung modelliert
- Keine Zeitverzögerungen
- Keine Angebotsschocks

**Reale Inflation** hängt von vielen weiteren Faktoren ab:
- Angebots- und Nachfrageschocks
- Erwartungen der Marktteilnehmer
- Globale Lieferketten
- Rohstoffpreise
- Wechselkurse

**Zweck:** Das Tool zeigt die **grundlegende Logik** monetaristischer Theorie, nicht die komplexe Realität.

### **Ist die Formel (M/Y - 1) × 100 = Inflation korrekt?**
**Akademisch korrekt:** Nein, zu vereinfacht.
**Didaktisch sinnvoll:** Ja, für Lernzwecke.

**Korrektere Darstellung:**
```
Inflation ≈ ΔM + ΔV - ΔY
(Wachstumsraten)
```

**Unser Modell:** Zeigt das M/Y-Verhältnis als Proxy für inflationären Druck, nicht als exakte Inflationsrate.

### **Warum werden historische Szenarien mit modellierten Daten dargestellt?**
**Exakte historische Daten** wären extrem komplex:
- Weimar 1923: Tagesschwankungen, multiple Währungen
- Venezuela 2023: Offiziell vs. Schwarzmarkt-Inflation
- Japan 1990er: Strukturelle vs. zyklische Deflation

**Modellierte Werte** ermöglichen:
- Vergleichbarkeit zwischen Szenarien
- Klare Ursache-Wirkungs-Beziehungen
- Fokus auf monetaristische Mechanismen

---

## 🔬 Wissenschaftliche Fragen

### **Warum wird V (Umlaufgeschwindigkeit) als konstant angenommen?**
**Historischer Kontext:** Monetaristische Theorie (Friedman) ging von relativ stabiler Umlaufgeschwindigkeit aus.

**Realität:** V schwankt erheblich:
- Eurozone: V ≈ 1,0-1,5
- USA: V ≈ 1,2-2,0
- Stark abhängig von Konjunktur und Geldpolitik

**Warum trotzdem V=1?**
1. Fokus auf M und Y (steuerbare Variablen)
2. Vereinfachung für Lernzwecke
3. Disclaimer macht diese Vereinfachung transparent

### **Ignoriert das Tool keynesianische Ansätze?**
**Ja, bewusst.** Das Tool heißt "**Monetarismus**-Simulation" und fokussiert auf:
- Geldmengen-Steuerung
- Quantitätsgleichung
- Friedman'sche Perspektive

**Nicht modelliert:**
- Fiskalpolitik
- IS-LM-Modell
- Nachfragesteuerung
- Liquiditätsfalle

**Zweck:** Klare Abgrenzung eines spezifischen theoretischen Ansatzes.

### **Warum fehlt die Unterscheidung zwischen nominaler und realer Geldmenge?**
**Vereinfachung:** Das Modell arbeitet mit nominalen Größen.

**In der Realität wichtig:**
- M/P (reale Geldmenge)
- Inflation = Wachstum (nominales M) - Wachstum (reales Y)

**Für Anfänger:** Zu komplex, wird in Fachliteratur vertieft.

---

## ⚖️ Rechtliche & Ethische Fragen

### **Kann ich rechtlich belangt werden, wenn jemand auf Basis dieses Tools Entscheidungen trifft?**
**Nein, durch mehrfache Absicherung:**

1. **Modal-Disclaimer** (beim Start, muss bestätigt werden)
2. **Footer-Hinweis** (permanent sichtbar)
3. **Titel** ("Simulation", "Bildungsprojekt")
4. **Meta-Tags** (SEO kennzeichnet als Bildungstool)

**Haftungsausschluss:**
> "Dieses Tool stellt keine wirtschafts- oder finanzwissenschaftliche Beratung dar..."

**Vergleich:** Wie Physik-Simulationen in der Schule (ignorieren Luftwiderstand) oder Chemie-Modelle (vereinfachte Atomdarstellung).

### **Darf ich dieses Tool in der Lehre verwenden?**
**Ja, ausdrücklich erwünscht!**

**Empfehlung für Lehrkräfte:**
1. Disclaimer vorlesen/besprechen
2. Grenzen des Modells diskutieren
3. Mit Fachliteratur ergänzen (z.B. Mankiw, Blanchard)
4. Reale Daten zum Vergleich zeigen

### **Können Ökonomen das Tool als "falsch" kritisieren?**
**Berechtigte Kritik:** "Zu vereinfacht für reale Analyse"
**Antwort:** "Ja, bewusst! Es ist ein **didaktisches** Tool für **Einsteiger**, kein Forschungsmodell."

**Analogie:**
- Newtonsches Modell vs. Relativitätstheorie (beide haben ihren Platz)
- Unser Tool = Newtonsches Modell der Geldtheorie

---

## 💻 Technische Fragen

### **Wie funktioniert die Simulation technisch?**
**Rein client-seitig:**
- Pure JavaScript (keine Server-Kommunikation)
- Berechnung: `ratio = geldMenge / bip`
- Inflation: `(ratio - 1) × 100`
- Waage rotiert proportional zu ratio

**Vorteile:**
- ✅ Sofortige Reaktion
- ✅ Offline nutzbar
- ✅ Keine Daten werden übertragen
- ✅ Datenschutzkonform

### **Woher stammen die EZB-Live-Daten?**
**Quelle:** [ECB Data Portal](https://data.ecb.europa.eu/)

**Daten (November 2025):**
- M3 Geldmenge: €17,2 Billionen
- BIP Eurozone: ~€14,5 Billionen (geschätzt)

**Warum hart-codiert?**
- API-Zugriff würde CORS-Probleme verursachen
- Daten ändern sich nur monatlich
- Für Lernzwecke ausreichend statisch

### **Kann das Tool 1000 gleichzeitige Nutzer handhaben?**
**Ja, problemlos!**

**Architektur:**
- Statisches HTML auf GitHub Pages CDN
- Kein Backend/keine Datenbank
- Jeder User rechnet lokal im Browser

**Skalierbarkeit:** >100.000 gleichzeitige User möglich

### **Funktioniert das Tool auf Smartphones?**
**Ja, vollständig optimiert:**
- ✅ Touch-Gesten (48px Buttons)
- ✅ Responsive Design (Mobile-First)
- ✅ Safe-Area für Notch/Dynamic Island
- ✅ Keine Scrolling-Probleme

**Getestet auf:**
- iOS (iPhone 12+, Safari)
- Android (Chrome)
- Tablets (iPad)

---

## 🎮 Nutzungs-Fragen

### **Wie löse ich die Challenges?**
**Tipps pro Challenge:**

**🇩🇪 Weimarer Republik (62.400% → <5%):**
- Extrem schwer! Benötigt 6-8 Runden
- Strategie: Alle Maßnahmen kombinieren
- Tipp: Staatsanleihen verkaufen (-3%) mehrfach nutzen

**🇻🇪 Venezuela (2.900% → <10%):**
- Schwer, 4-5 Runden nötig
- Strategie: Schrittweise Reduktion
- Tipp: Start mit Leitzins + Anleihen = -5%

**🇯🇵 Japan (-16,7% → 0-3%):**
- Mittel, 2-3 Runden
- Strategie: Geldmenge ERHÖHEN (expansiv)
- Tipp: Leitzins senken + Anleihen kaufen = +5%

**🇪🇺 EZB (18,6% → 1-3%):**
- Mittel, 2 Runden mit Präzision
- Strategie: Zwei Reduktionsrunden
- Tipp: 1. Runde -8,5%, 2. Runde Feinabstimmung

### **Warum ändert sich die Inflation nur schrittweise?**
**Design-Entscheidung:** Jeder Klick = eine geldpolitische Maßnahme

**In Realität:**
- Maßnahmen wirken mit Zeitverzögerung (6-18 Monate)
- Schrittweise Anpassung üblich

**Im Tool:** Sofortige Wirkung für didaktische Klarheit

### **Kann ich eigene Szenarien erstellen?**
**Aktuell nicht in der UI, aber:**

**Für Entwickler (JavaScript):**
```javascript
scenarios.custom = {
  name: 'Eigenes Szenario',
  icon: '🎨',
  geldmenge: 10,  // Ihre Werte
  bip: 8,
  description: 'Ihre Beschreibung'
};
```

**Feature-Request:** Könnte in zukünftiger Version hinzugefügt werden

---

## 🐛 Problem-Lösungen

### **Die Waage zeigt "22,2%" aber ich sehe nur "Inflation: 22,2%"**
**Erwartetes Verhalten!**
- Startwert: M=5,5, Y=4,5 → (5,5/4,5 - 1) × 100 = 22,2%
- Dies ist der Ausgangszustand "Deutschland Ende 2025" (modelliert)

### **Challenge bleibt bei 1,9% stecken, zählt aber nicht als erfüllt**
**Präzisionsproblem behoben!**
- Früher: Rundung versteckte echten Wert
- Jetzt: 1 Dezimalstelle wird angezeigt
- EZB-Challenge akzeptiert 1,0-3,0% (erweitert von 1,5-2,5%)

### **Japan-Challenge akzeptiert Deflation als Erfolg?**
**Bug wurde gefixt!** (Commit 3947d81)
- Problem war: `Math.abs()` entfernte Vorzeichen
- Jetzt: Deflation (-) ≠ Inflation (+)
- Japan-Challenge benötigt echte positive Inflation

---

## 📖 Quellenangaben & Weiterführendes

### **Wissenschaftliche Grundlagen:**
- Friedman, M. (1968): "The Role of Monetary Policy"
- Fisher, I. (1911): "The Purchasing Power of Money"
- Quantitätsgleichung: MV = PY

### **Lehrbücher zur Vertiefung:**
- Mankiw, N.G.: "Makroökonomie"
- Blanchard, O.: "Macroeconomics"
- Mishkin, F.S.: "The Economics of Money, Banking, and Financial Markets"

### **Aktuelle Daten:**
- [ECB Data Portal](https://data.ecb.europa.eu/)
- [Eurostat](https://ec.europa.eu/eurostat)
- [Deutsche Bundesbank](https://www.bundesbank.de/de/statistiken)

### **Historische Kontexte:**
- Weimar Republik: Bresciani-Turroni (1937)
- Japan's Lost Decade: Krugman (1998)
- Venezuela Crisis: IMF Country Reports

---

## 🆘 Support & Feedback

### **Ich habe einen Bug gefunden!**
**Melden Sie auf:** [GitHub Issues](https://github.com/florianderwein-sketch/Geldmenge/issues)

**Bitte angeben:**
- Browser & Version
- Gerät (Desktop/Mobile)
- Schritte zur Reproduktion
- Screenshot falls möglich

### **Ich habe eine Feature-Idee!**
**Willkommen!** Öffnen Sie ein Issue auf GitHub mit Tag `enhancement`

**Beliebte Wünsche:**
- [ ] Eigene Szenarien erstellen
- [ ] Zeitverzögerungen simulieren
- [ ] Vergleich Monetarismus vs. Keynesianismus
- [ ] Highscore/Leaderboard
- [ ] Mehr historische Szenarien

### **Kann ich zum Projekt beitragen?**
**Ja, gerne!** Das Projekt ist Open Source.

**Möglichkeiten:**
- Code-Verbesserungen (Pull Requests)
- Übersetzungen (Englisch, Französisch, etc.)
- Didaktische Verbesserungen
- Dokumentation erweitern

---

## 📝 Lizenz & Verwendung

### **Unter welcher Lizenz steht das Tool?**
**MIT License** (siehe LICENSE-Datei im Repository)

**Bedeutet:**
- ✅ Kommerzielle Nutzung erlaubt
- ✅ Modifikation erlaubt
- ✅ Verteilung erlaubt
- ✅ Private Nutzung erlaubt
- ⚠️ Keine Gewährleistung/Haftung

### **Muss ich den Autor nennen?**
**Ja, bitte:**
```
"Monetarismus-Simulation" by [Your Name]
https://github.com/florianderwein-sketch/Geldmenge
```

### **Kann ich das Tool für kommerzielle Schulungen verwenden?**
**Ja**, unter Beachtung:
1. MIT-Lizenz einhalten (Urhebernennung)
2. Disclaimer beibehalten
3. Keine Haftung des Original-Autors

---

## 🎯 Abschließende Klarstellung

### **Was dieses Tool KANN:**
✅ Grundkonzepte des Monetarismus vermitteln
✅ Zusammenhang M3/BIP/Inflation visualisieren
✅ Geldpolitische Instrumente demonstrieren
✅ Historische Krisen in Kontext setzen
✅ Interaktives Lernen ermöglichen

### **Was dieses Tool NICHT KANN:**
❌ Reale Inflationsraten exakt vorhersagen
❌ Als Grundlage für Finanzentscheidungen dienen
❌ Alle makroökonomischen Zusammenhänge abbilden
❌ Wirtschaftspolitische Beratung ersetzen
❌ Komplexität der Realität vollständig erfassen

---

**Version:** 1.0
**Letzte Aktualisierung:** Januar 2026
**Kontakt:** [GitHub Repository](https://github.com/florianderwein-sketch/Geldmenge)

---

*"Das beste Modell ist eine Lüge, die nützlich ist."*
— Georg Box (modifiziert)
