#practice
height = float(input('Please enter your height(m):'))
weight = float(input('Please enter your weight(kg):'))
bmi = weight/pow(height, 2)
if bmi >= 32:
    print('Your BMI is %.2f, severe obesity' %bmi)
elif bmi >= 28:
    print('Your BMI is %.2f, obesity' %bmi)
elif bmi>= 25:
    print('Your BMI is %.2f, overweight' %bmi)
elif bmi>= 18.5:
    print('Your BMI is %.2f, normal weight' %bmi)
elif bmi>0:
    print('Your BMI is %.2f, underweight' %bmi)
else:
    print('Error')

