# Fachliche Fehleranalyse: Monetarismus Interaktive Waage

## ❌ KRITISCHE FEHLER

### 1. **FALSCHE GELDPOLITIK-LOGIK** (Schwerwiegend!)

**Problem:** Alle Geldpolitik-Maßnahmen ERHÖHEN die Geldmenge - das ist das Gegenteil der realen Wirkung!

```javascript
// AKTUELL (FALSCH):
<button class="geld" onclick="adjustMoney(2)">Leitzins erhöhen (+2%)</button>
function adjustMoney(percent) {
  geldMenge *= (1 + percent / 100);  // ERHÖHT die Geldmenge!
}
```

**Realität:**
- **Leitzins erhöhen** → Geldmenge SINKT (kontraktive Geldpolitik)
- **Staatsanleihen verkaufen** → Geldmenge SINKT (Geld wird abgeschöpft)
- **Mindestreserven erhöhen** → Geldmenge SINKT (Banken können weniger Kredite vergeben)
- **Liquidität verringern** → Geldmenge SINKT (per Definition)

**Korrektur erforderlich:**
```javascript
function adjustMoney(percent) {
  geldMenge *= (1 - percent / 100);  // VERRINGERT die Geldmenge
}
```

---

### 2. **FALSCHE INFLATIONSBERECHNUNG**

**Problem:** Inflation wird als statisches Verhältnis von Geldmenge zu BIP berechnet.

```javascript
// AKTUELL (FALSCH):
const ratio = geldMenge / bip;  // 4.09 / 1.121 = 3.65
let percentage = Math.round(Math.abs((ratio - 1) * 100));  // = 265%
```

**Fachliche Probleme:**

a) **Inflation ist eine Änderungsrate, keine Bestandsgröße**
   - Inflation = prozentuale Änderung des Preisniveaus über Zeit
   - Nicht: absolutes Verhältnis M/Y

b) **Quantitätstheorie wird falsch angewandt**
   - Korrekte Formel: M·V = P·Y
   - Wobei: M = Geldmenge, V = Umlaufgeschwindigkeit, P = Preisniveau, Y = reales BIP
   - Bei konstantem V: ΔM - ΔY ≈ Inflation
   - Inflation = (Wachstumsrate Geldmenge) - (Wachstumsrate BIP)

c) **Dimensionsproblem**
   - Ein M/Y-Verhältnis von 3,65 bedeutet NICHT 265% Inflation
   - Es bedeutet nur, dass die Geldmenge 3,65x größer ist als das Jahres-BIP
   - Für Deutschland wäre M3/BIP ≈ 1,5-2,0 realistisch

---

### 3. **UNREALISTISCHE AUSGANGSWERTE**

**Problem:**
```javascript
let geldMenge = 4.09; // Billionen €
let bip = 1.121; // Billionen €
// Verhältnis: 3,65
```

**Realität Deutschland (2024):**
- BIP: ~4,0 Billionen €
- M3 (breiteste Geldmenge Eurozone): ~16 Billionen €
- M3/BIP Eurozone: ~1,5-2,0
- M3 Deutschland allein: ~6-8 Billionen €

**Das aktuelle Verhältnis 3,65 ist extrem unrealistisch!**

---

### 4. **BEGRIFFSVERWIRRUNG: Inflation vs. Inflationsdruck**

**Problem:** Die Anzeige suggeriert eine aktuelle Inflationsrate von 264%.

**Korrekt wäre:**
- "Potenzieller Inflationsdruck durch Geldmengenüberhang"
- Oder: Zeige die ÄNDERUNG der Geldmenge/BIP über Zeit als Proxy für Inflation

**Beispiel bessere Formulierung:**
```
Geldmengenüberhang: 265%
→ Starker inflationärer Druck
```

---

## ⚠️ KONZEPTIONELLE PROBLEME

### 5. **Fehlende zeitliche Dimension**

- Inflation ist eine Flussgroße (% pro Jahr)
- BIP ist eine Flussgröße (€ pro Jahr)
- Geldmenge ist eine Bestandsgröße (€ zu einem Zeitpunkt)

**Verbesserung:** Zeige Änderungsraten statt absoluter Werte

### 6. **Umlaufgeschwindigkeit wird ignoriert**

In der Quantitätstheorie (M·V = P·Y):
- V (Velocity) kann sich ändern
- Bei konstanter Geldmenge kann V steigen → Inflation
- Bei sinkender V kann Geldmengenwachstum neutral sein

---

## ✅ KORREKTURVORSCHLÄGE

### Variante A: Einfache Korrektur
1. Geldpolitik-Buttons: Verwende NEGATIVE Prozente
2. Umbenennung: "Inflation" → "Geldmengenüberhang"
3. Realistische Startwerte: geldMenge = 1.5, bip = 1.0

### Variante B: Fachlich korrekte Simulation
1. Tracking von Änderungsraten über Zeit
2. Inflation = ΔM% - ΔBIP%
3. Integration der Umlaufgeschwindigkeit V
4. Zeitachse mit Perioden

---

## ZUSAMMENFASSUNG

| Fehler | Schwere | Status |
|--------|---------|--------|
| Geldpolitik erhöht statt senkt Geldmenge | 🔴 KRITISCH | Muss behoben werden |
| Inflationsberechnung fachlich falsch | 🔴 KRITISCH | Muss überarbeitet werden |
| Unrealistische Ausgangswerte | 🟡 WICHTIG | Sollte angepasst werden |
| Fehlende Zeitdimension | 🟡 WICHTIG | Konzeptionelle Verbesserung |
| V (Velocity) wird ignoriert | 🟢 OPTIONAL | Für Fortgeschrittene |

---

## EMPFEHLUNG

**Minimale Korrektur für funktionale Korrektheit:**
```javascript
// 1. Geldpolitik korrigieren
function adjustMoney(percent) {
  geldMenge *= (1 - percent / 100);  // Minus statt Plus!
}

// 2. Label ändern
// "Inflation" → "Geldmengenüberhang relativ zu BIP"

// 3. Realistische Werte
let geldMenge = 1.5; // Billionen €
let bip = 1.0; // Billionen €
```
