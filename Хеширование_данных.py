import hashlib

myhash = input ('Введите хешируемые данные: ')

hash_object = hashlib.sha256(myhash.encode())
print (hash_object.hexdigest())