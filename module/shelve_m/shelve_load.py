import shelve

f = shelve.open('shelve_test')

print(f['test'], f['t1'], f['t2'])