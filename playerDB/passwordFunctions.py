import os
import hashlib

def passwordHashing(password):
    # Generate a random 16-byte salt
    salt = os.urandom(16)
    
    # Create the hash using SHA-256
    hashObj = hashlib.sha256(salt + password.encode())
    passwordHash = hashObj.digest()

    # Combine the salt and the password hash
    saltHash = salt + passwordHash
    
    # Encode the result in hexadecimal
    return saltHash.hex()



def verifyPassword(storedHash, password):
    # decodes from hex
    saltAndHash = bytes.fromhex(storedHash)

    # separates salt from hash
    salt = saltAndHash[:16]
    originalHashedPassword = saltAndHash[16:]

    # hashes the new password and incorporates the salt
    newHash = hashlib.sha256(salt + password.encode())
    newHashedPassword = newHash.digest()

    # returns comparison
    return originalHashedPassword == newHashedPassword