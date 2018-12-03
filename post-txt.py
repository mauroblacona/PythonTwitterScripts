from data import api

import random

with open("nombre.txt", "r") as f:
     lineas = f.readlines()
     api.PostUpdate(lineas[0])
with open("nombre.txt", "w") as f:
     f.writelines(lineas[1:])

