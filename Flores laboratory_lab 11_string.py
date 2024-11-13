foods = []

print ("enter different kinds of food")
count = 0 
while count < 10:
    food = input(f"Food {count + 1}  ")
    foods.append(food)
    count +=1
    
num_letters = int(input("enter the number of letter to filter meals by: "))

result = []
for food in foods:
    if len(food) == num_letters:
        result.append(food)
        
if result:
    print("foods with", num_letters, "letters" (result))
else:
    print("no meals can be found with", num_letters, "letters.")