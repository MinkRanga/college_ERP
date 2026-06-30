from app.auth.hashing import hash_password

password = "admin123"

hashed = hash_password(password)

print(hashed)