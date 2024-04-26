import random

field_size = int(input()) * 2 + 1 # field is always square; even numbers for walls, odd available to move
player_start_point = [random.randrange(1, field_size, 2), random.randrange(1, field_size, 2)]  # player can move to odd numbers only; [0] -- x, [1] -- y
print(player_start_point)
# create field
field_init = list()
for i in range(field_size):
  if i == 0 or i == field_size - 1:  # first and end string (walls)
    field_init.append(["- " for t in range(field_size - 1)])  
    field_init[i].append("-")
  elif i % 2 == 1:                   # odd strings -- available to move
    field_init.append(["|"])
    for j in range(field_size - 1):
            if j % 2 == 0:
              if i == player_start_point[1] and j + 1 == player_start_point[0]:
                field_init[i].append(" P")  # init player  
              else:
                field_init[i].append(" .")  # odd x
            else:
              field_init[i].append(" |")    # walls, even x
  elif i % 2 == 0:                          # walls, even y
    field_init.append(["|"])
    for k in range(field_size - 1):
      if k % 2 == 0:
        field_init[i].append(" -")          # walls
      else:
        field_init[i].append(" |")          # walls
  else:
    print("error while initialize")

# initialize
for field_string in field_init:             # print
  print("".join(field_string), "\n")
