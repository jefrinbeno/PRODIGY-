import string

def check_password_strength(password):
    length=len(password)
    uppercase=any(char.isupper() for char in password)
    lowercase=any(char.islower() for char in password)
    digit=any(char.isdigit() for char in password)
    special_char=any(char in string.punctuation for char in password)

    score=0
    feedback=[]

    if length>=8:
        score+=1
    if uppercase:
        score+=1
    if lowercase:
        score+=1
    if digit:
        score+=1
    if special_char:
        score+=1

    if score==5:
        feedback.append("Excellent! Your password is very strong.")
    elif score>=3:
        feedback.append("Good! Your password is strong.")
    elif score>=2:
        feedback.append("Fair. Your password could be strong. ")
    else:
        feedback.append("Weak! Please consider a strong password.")
    return feedback

password=input("Enter the password: ")
strength_feedback=check_password_strength(password)

for feedback in strength_feedback:
    print(feedback)                        
