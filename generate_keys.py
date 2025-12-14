from Crypto.PublicKey import RSA

# إنشاء مفتاح جديد 2048 bit
key = RSA.generate(2048)

# حفظ المفتاح العمومي
with open("keys/public.pem", "wb") as f:
    f.write(key.publickey().export_key())

# حفظ المفتاح السري
with open("keys/private.pem", "wb") as f:
    f.write(key.export_key())

print("RSA keys generated successfully!")
