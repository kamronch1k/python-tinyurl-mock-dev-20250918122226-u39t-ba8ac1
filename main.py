import hashlib
s='devrunner'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
