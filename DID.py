import rsa
def createDID():
    Credential = input("What Credential is this for?:")
    Credentialname = input("Name on Credential:")
    Credentialdegree = input("What degree is this:")
    publicKey, privateKey = rsa.newkeys(1024)
    message1 = f"{Credential}, {Credentialname}, {Credentialdegree}"
    encmsg = rsa.encrypt(message1.encode(), privateKey)
    print((encmsg))
    print(publicKey)
    DID = "did:university:universitydid"
    print(DID)

createDID()