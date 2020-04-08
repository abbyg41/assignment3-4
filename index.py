from browser import document


def events():
  document['bmiCalculator'].bind('click', bmi)
  document['retirementCalculator'].bind('click', retirement )
  print('Set up all buttons')

  document['feet'].bind('input', feet)
  document['inches'].bind('input', inches)
  document['weight'].bind('input', weight)
  
  document['currentAge'].bind('input', currentAge)
  document['salary'].bind('input', salary_on_change)
  document['percentSaved'].bind('input', percentSaved)
  document['saveGoal'].bind('input', saveGoal)
  print('Set up all event listeners')

  feet_on_change('')
  inches_on_change('')
  current_age_on_change('')
  percent_saved_on_change('')
  print("Ran slider's first feedback")

# Helpers associated with getting user's BMI
def run_bmi(event):
  # Lead in with title
  print('\nCalculating BMI')
  # Expected input
  height = get_height()
  print(' Height: ' + str(height))

  # Expected input
  weight = get_weight()
  print(' Weight: ' + str(weight))

  if not(client.valid_bmi_values(height, weight)):
    document['bmiResult'].innerHTML = ''
    return

  print('\n Results:')
  calculate_bmi(height, weight)

def get_height():
  feet = int(document['feet'].value)
  inches = float(document['inches'].value)
  return client.get_height(feet, inches)

def get_weight():
  weight = document['weight'].value

  (valid, weight) = client.valid_weight(weight)
  if (valid):
    return weight
  return 'Invalid weight value'

def calculate_bmi(height, weight):
  (bmi, category) = client.get_bmi(height, weight)
  output = 'Calculated BMI: ' + str(bmi) + '<br> BMI Category: ' + str(category)

  print(output)
  document['bmiResult'].innerHTML = output

# Helper associated with getting user's estimated retirement age
def run_retirement_calculator(event):
  # Lead in with title
  print('\nCalculating age of retirement')
  
  age = get_current_age()
  print(' Age: ' + str(age))

  salary = get_salary()
  print(' Salary: ' + str(salary))

  percent_saved = get_percent_saved()
  print(' Percent Saved: ' + str(percent_saved))

  save_goal = get_save_goal()
  print(' Save goal: ' + str(save_goal))

  if not(client.valid_retirement_values(age, salary, percent_saved, save_goal)):
    document['retirementResult'].innerHTML = ''
    return

  print('\n Results')
  calculate_retirement_age(age, salary, percent_saved, save_goal)

def get_current_age():
  return int(document['currentAge'].value)

def get_salary():
  salary = document['salary'].value

  (valid, salary) = client.valid_salary(salary)
  if (valid):
    return salary
  return 'Invalid salary value'

def get_percent_saved():
  return float(document['percentSaved'].value)

def get_save_goal():
  save_goal = document['saveGoal'].value

  (valid, save_goal) = client.valid_save_goal(save_goal)

  if (valid):
    return save_goal
  return 'Invalid save goal value'

def calculate_retirement_age(age, salary, percent_saved, save_goal):
  (met, age_met) = client.get_retirement_age(age, salary, percent_saved, save_goal)

  output = 'Goal: '
  if (met):
    output = output + 'Met <br> Age: ' + str(age_met)
  else:
    output = output + 'Not met'

  document['retirementResult'].innerHTML = output


# User input BMI
def feet(event):
  value = document['feet'].value
  print('- onChange: Feet ' + str(value))
  document['feetLabel'].textContent = 'Feet: ' + str(value);

def inches(event):
  value = document['inches'].value
  print('- onChange: Inches ' + str(value))
  document['inchesLabel'].textContent = 'Inches: ' + str(value);

def weight(event):
  value = document['weight'].value
  (valid, value) = client.valid_weight(value)

  if (valid):
    document['weightWarning'].textContent = ''
  else:
    document['weightWarning'].textContent = 'Invalid weight value'

#calculate bmi
def get_height(feet, inches):
  return (int(feet)*12) + float(inches)

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



    #User input Retirement
def currentAge(event):
  value = document['currentAge'].value
  document['currentAgeLabel'].textContent = 'Current age: ' + str(value);

def salary(event):
  value = document['salary'].value
  (valid, value) = client.valid_salary(value)

  if (valid):
    document['salaryWarning'].textContent = ''
  else:
    document['salaryWarning'].textContent = 'Invalid salary value'

def percentSaved(event):
  value = document['percentSaved'].value
  document['percentSavedLabel'].textContent = 'Percent Saved (%): ' + str(value) + '%';

def saveGoal(event):
  value = document['saveGoal'].value
  (valid, value) = client.valid_save_goal(value)

  if (valid):
    document['saveGoalWarning'].textContent = ''
  else:
    document['saveGoalWarning'].textContent = 'Invalid save goal value
    
#calculate retirement
def get_retirement_age(age, salary, percent_saved, save_goal):
  percent_saved *= 1.35
  years = save_goal / (salary * (percent_saved/100))
  age_met = years + age
  age_met = round(age_met)

  met = age_met < 100
  return (met, age_met)