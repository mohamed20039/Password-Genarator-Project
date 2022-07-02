import string
import secrets

length=input('Choose the length your password: ')
alphabet=string.ascii_letters + string.digits

password="".join(secrets.choice(alphabet) for i in range(int(length)))
print (password)