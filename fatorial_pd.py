import timeit
import time

def fat(n):
    if n <= 1:
        return 1
    if not hasattr(fat, 'cache'):
        fat.cache = {}
    if n in fat.cache:
        return fat.cache[n]
    result = n * fat(n-1)
    fat.cache[n] = result
    return result

def exec2n(n):
    print(f'Fatorial de {n}')
    t1 = timeit.default_timer()
    res = fat(n)
    t2 = timeit.default_timer()
    print(' - Resultado:', res)
    print(' - Tempo:', round((t2-t1), 5))
    return res


print('Rodando pela primeira vez:')
exec2n(100)
print()
exec2n(102)
print()
print()

print('Rodando pela segunda vez:')
exec2n(100)
print()
exec2n(102)
