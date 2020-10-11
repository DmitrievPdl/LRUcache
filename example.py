from LRUСache import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse')) # вернёт 'James'
cache.delete('Walter')
print(cache.get('Walter')) # вернёт ''
print(cache)

cache2 = LRUCache(3)
cache2.set('a', '1')
cache2.set('b', '2')
cache2.set('c', '3')
cache2.set('d', '4')
cache2.set('e', '5')
cache2.set('f', '6')
cache2.set('g', '7')

print(cache2) # { g : 7, f : 6, e : 5 }

print(cache2.get('e')) # 5

print(cache2) # { e : 5, g : 7, f : 6 }

cache2.delete('g')
print(cache2) # { e : 5, f : 6 }

cache2.delete('e')
cache2.delete('f')
print(cache2) # {  }