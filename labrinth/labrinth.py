import random

field_size = int(input()) * 2 + 1 # field is always square; even numbers for walls, odd available to move
player_start_point = [random.random(1, field_size, 2), random.random(1, field_size, 2)]  # player can move to odd numbers only; [0] -- x, [1] -- y

# create field
field_init = list()
for i in range(field_size - 1):
  if i == 0 or i == field_size - 1:
    field_init.append(["- " for t in range(field_size - 1)])
    field_init[i].append("-")
  elif i % 2 == 1:
    field_init.append(["|"])
    for j in range(field_size - 1):
            if j % 2 == 0:
              field_init[i].append(" .")
            else:
              field_init[i].append(" |")
  elif i % 2 == 0:
    field_init.append(["|"])
    for k in range(field_size - 1):
      if k % 2 == 0:
        field_init[i].append(" -")
      else:
        field_init[i].append(" |")
  else:
    print("error while initialize")

# initialize
for field_string in field_init:
  print(field_string, "\n")
