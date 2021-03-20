n = [10,1]

max = 0
min = 0

l = len(n)

for c in range(0, l):
  if c == 0:
    max = min = n[c]
  else:
    if n[c] > max:
      max = n[c]
    if n[c] < min:
      min = n[c]

print(f'Menor numero do Arrey é {min}')
print(f'Maior numero do Arrey é {max}')
