#bmi functions
'''
float get_height(feet, inches)
(bool, float) valid_weight(weight)
bool valid_bmi_values(height, weight)
(float, string) get_bmi(height, weight)
'''

def get_height(feet, inches):
  return (int(feet)*12) + float(inches)

def valid_weight(weight):
  valid = False;
  try:
    weight = float(weight)
    if (weight > 0):
      valid = True;
  except Exception: 
    valid = False;

  return (valid, weight)

def valid_bmi_values(height, weight):
  return type(height) == float and type(weight) == float

def get_bmi(height, weight):
  bmi = (weight * 0.45) / ((height * 0.025)**2)
  bmi = round(bmi,1)

  category = ''
  if (bmi < 18.5):
    category = 'Underweight'
  elif (bmi >= 18.5 and bmi <= 24.9):
    category = 'Normal weight'
  elif (bmi >= 25 and bmi <= 29.9):
    category = 'Overweight'
  else:
    category = 'Obese'

  return (bmi, category)

#retirement functions
'''
(bool, float) valid_salary(salary)
(bool, float) valid_save_goal(save_goal)
bool valid_retirement_values(age, salary, percent_saved, save_goal)
(bool, int) get_retirement_age(age, salary, percent_saved, save_goal)
'''


def valid_salary(salary):
  valid = False;
  try:
    salary = float(salary)
    # x > 0
    if (salary > 0):
      valid = True;
  except Exception:
    valid = False;

  return (valid, salary)

def valid_save_goal(save_goal):
  valid = False;
  try:
    save_goal = float(save_goal)
    if (save_goal > 0):
      valid = True;
  except Exception:
    valid = False;

  return (valid, save_goal)

def valid_retirement_values(age, salary, percent_saved, save_goal):
  return type(age) == int and type(salary) == float and type(percent_saved) == float and type(save_goal) == float

def get_retirement_age(age, salary, percent_saved, save_goal):
  percent_saved *= 1.35
  years = save_goal / (salary * (percent_saved/100))
  age_met = years + age
  age_met = round(age_met)

  met = age_met < 100
  return (met, age_met)
