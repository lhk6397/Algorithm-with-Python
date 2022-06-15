string = input()
chars = []
num_sum = 0

for elem in string:
  if elem.isdigit():
    num_sum += int(elem)
  else: chars.append(elem)

chars.sort()
string = ''.join(chars)

print(string+str(num_sum))