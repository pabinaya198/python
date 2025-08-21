like2='bananas'
print(name + 'likes' + like1 + 'and' + like2)

text='{} likes {} and {}'
print(text-format(name,like1,like2))

print('{} likes {} and {}.format(name,like1,like2)')

text='{0} likes {2} and {1}'
print(text-format(name,like1,like2))

text='{name} likes {fruit} and {fruit2}'
print(text.format(name='hari',fruit1='apples',fruit2='bananas'))
print(text.format(name='ravi',fruit1='grapes',fruit2='oranges'))

