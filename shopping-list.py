import time

print("Initializing Personal Shopping List Maker")
print("...")
time.sleep(1)

shopping_list = []

while True:
    new_item = input("> ")
    if new_item == "done":
       break
    shopping_list.append(new_item)
    

print(shopping_list)
listitem = shopping_list.sort()

counter = 0
for listitem in shopping_list:
    counter += 1
    print("Item No." + str(counter) + " " + listitem)

        