import time

with open('salary.txt', 'w') as f:
    f.write("Zillow")

time.sleep(2)

with open('salary.txt') as f:
    response = f.readlines()

print(response)