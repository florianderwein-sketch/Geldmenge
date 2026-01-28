#!/usr/bin/env python3
import qrcode

# GitHub Pages URL
url = "https://florianderwein-sketch.github.io/Geldmenge/"

# QR-Code erstellen
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Als Bild speichern
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code_geldmenge.png")

# Als ASCII in Terminal ausgeben
print("\n" + "="*60)
print("QR-CODE FÜR MONETARISMUS-WAAGE")
print("="*60)
print(f"\nURL: {url}\n")
qr.print_ascii(invert=True)
print("\n" + "="*60)
print("QR-Code gespeichert als: qr_code_geldmenge.png")
print("="*60 + "\n")
