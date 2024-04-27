print(2 > 3)#Conditions
#When you check two values are equal, make sure you use the == sign var_one==1 
#"if" statements
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(38))

#"if ... else" statements
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(38))

#"if ... elif ... else" statements

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
    
print(evaluate_temp_with_elif(36))


