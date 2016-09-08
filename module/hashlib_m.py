import hashlib, hmac

print(hashlib.md5(b'123').hexdigest())

print('\n', 'md5'.center(40, '*'))
a = hashlib.md5()
a.update(b'shiina_ao')

print(a.digest(), '\n', a.hexdigest())

print('\n', 'sha256'.center(40, '*'))
b = hashlib.sha256()
b.update(b'shiina_ao')

print(b.digest(), '\n', b.hexdigest())

print('\n', 'hmac'.center(40, '*'))
h = hmac.new(b'shiina')
h.update(b'_ao')
print(h.digest(), '\n', h.hexdigest())