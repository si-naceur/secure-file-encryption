from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# فتح public key الموجود عندك
recipient_key = RSA.import_key(open("keys/public.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)

# إنشاء AES key عشوائي
session_key = get_random_bytes(16)

# فتح الملف المراد تشفيره
with open("sample.txt", "rb") as f:
    data = f.read()

# تشفير الملف بالAES
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# حفظ الملف المشفّر
with open("sample.txt.enc", "wb") as f:
    f.write(cipher_aes.nonce)
    f.write(tag)
    f.write(ciphertext)

# تشفير AES key بالRSA public key
enc_session_key = cipher_rsa.encrypt(session_key)
with open("keys/session_key.enc", "wb") as f:
    f.write(enc_session_key)

print("File encrypted successfully!")
