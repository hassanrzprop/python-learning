import random
import time
randomNumbers=random.randint(1,10)
print(randomNumbers)

afterDecimal=random.random()
print(afterDecimal)



# creating unique id
sand="@$%&()_-!^~`"
unique_id=sand[random.randint(0,len(sand))] + str(int(random.random())) +sand[random.randint(0,len(sand))] + str(round(time.time())) + sand[random.randint(0,len(sand))]
print(unique_id)