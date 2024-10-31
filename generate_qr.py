import qrcode

# URL for the QR code
url = "https://github.com/GxPatel"

# Generate QR code
qr = qrcode.make(url)

# Save QR code as a PNG file
qr.save("github_qr_code.png")
print("QR code generated and saved as 'github_qr_code.png'")
