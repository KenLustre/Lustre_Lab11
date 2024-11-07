list = []
i = 1
passed = 0
x = 0
user_input = input(f"Enter Grade of Student {i} (Type 'done' to finish): ")
while user_input.lower() != "done":
    if int(user_input) >= 40 and  int(user_input) <= 100:
        list.append(int(user_input))
        if int(user_input) >= 75:
            passed += 1
    else:
        x += 1
        break
    i += 1
    user_input = input(f"Enter Grade of Student {i} (Type 'done' to finish): ")
if x == 0:
    ave = sum(list) / len(list)
    passing_percentage = (passed / len(list)) * 100
    print(f"Average Grade: {ave: .2f}")
    print(f"No. of Students Passed: {passed}")  
    print(f"Passing Score: {int(passing_percentage)}%")
else:
    print("Invalid Grade. Please enter a valid grade between 40 and 1")




