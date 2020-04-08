from browser import document

def setup_events():
  

  document['feet'].bind('input', feetInput)
  document['inches'].bind('input', inchesInput)
  document['weight'].bind('input', weightInput)
  
  document['currentAge'].bind('input', currentAgeInput)
  document['salary'].bind('input', salaryInput)
  document['percentSaved'].bind('input', percentSavedInput)
  document['saveGoal'].bind('input', saveGoalInput)
  print('Set up all events')

  document['calculateBMI'].bind('click', run_bmi)
  document['calculateRetirement'].bind('click', run_retirement_calculator)
  print('Set up all buttons')
  

def run_bmi(event):
  print('\nCalculating BMI')
  height = get_height()
  print(' Height: ' + str(height))

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
  return ((int(feet)*12) + float(inches))

def get_weight():
  weight = document['weight'].value

  (valid, weight) = valid_weight(weight)
  if (valid):
    return weight
  return 'Invalid weight value'

def valid_weight(weight):
  valid = False;
  try:
    weight = float(weight)
    # x > 0
    if (weight > 0):
      valid = True;
  except Exception:
    valid = False;

  return (valid, weight)

def calculate_bmi(height, weight):
  (bmi, category) = get_bmi(height, weight)
  output = 'Calculated BMI: ' + str(bmi) + '<br> BMI Category: ' + str(category)
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
  print(output)
  document['bmiResult'].innerHTML = output

# Helper associated with getting user's estimated retirement age
def run_retirement_calculator(event):
  print('\nCalculating age of retirement')
  
  age = get_current_age()
  print(' Age: ' + str(age))

  salary = get_salary()
  print(' Salary: ' + str(salary))

  percent_saved = get_percent_saved()
  print(' Percent Saved: ' + str(percent_saved))

  save_goal = get_save_goal()
  print(' Save goal: ' + str(save_goal))

  if not(valid_retirement_values(age, salary, percent_saved, save_goal)):
    document['retirementResult'].innerHTML = ''
    return
  print('\n Results')
  get_retirement_age(age, salary, percent_saved, save_goal)

def get_retirement_age(age, salary, percent_saved, save_goal):
  percent_saved *= 1.35
  years = save_goal / (salary * (percent_saved/100))
  age_met = years + age
  age_met = round(age_met)

  met = age_met < 100
  return (met, age_met)

def get_current_age():
  return int(document['currentAge'].value)

def get_salary():
  salary = document['salary'].value

  (valid, salary) = valid_salary(salary)
  if (valid):
    return salary
  return 'Invalid salary value'
def valid_salary(salary):
  valid = False;
  try:
    salary = float(salary)
    # x > 0
    if (salary > 0):
      valid = True;
  except Exception: # Non float values
    valid = False;

  return (valid, salary)

def get_percent_saved():
  return float(document['percentSaved'].value)

def get_save_goal():
  save_goal = document['saveGoal'].value

  (valid, save_goal) = valid_save_goal(save_goal)

  if (valid):
    return save_goal
  return 'Invalid save goal value'
def valid_save_goal(save_goal):
  valid = False;
  try:
    save_goal = float(save_goal)
    if (save_goal > 0):
      valid = True;
  except Exception:
    valid = False;

  return (valid, save_goal)

def calculate_retirement_age(age, salary, percent_saved, save_goal):
  (met, age_met) = get_retirement_age(age, salary, percent_saved, save_goal)

  output = 'Goal: '
  if (met):
    output = output + 'Met <br> Age: ' + str(age_met)
  else:
    output = output + 'Not met'

  document['retirementResult'].innerHTML = output

def get_retirement_age(age, salary, percent_saved, save_goal):
  percent_saved *= 1.35
  years = save_goal / (salary * (percent_saved/100))
  age_met = years + age
  age_met = round(age_met)

  met = age_met < 100
  return (met, age_met)
# User input functions
def feetInput(event):
  value = document['feet'].value
  print('- onChange: Feet ' + str(value))
  document['feetLabel'].textContent = 'Feet: ' + str(value);

def inchesInput(event):
  value = document['inches'].value
  print('- onChange: Inches ' + str(value))
  document['inchesLabel'].textContent = 'Inches: ' + str(value);

def weightInput(event):
  value = document['weight'].value
  (valid, value) = valid_weight(value)

  if (valid):
    document['weightWarning'].textContent = ''
  else:
    document['weightWarning'].textContent = 'Invalid weight value'

def currentAgeInput(event):
  value = document['currentAge'].value
  document['currentAgeLabel'].textContent = 'Current age: ' + str(value);

def salaryInput(event):
  value = document['salary'].value
  (valid, value) = valid_salary(value)

  if (valid):
    document['salaryWarning'].textContent = ''
  else:
    document['salaryWarning'].textContent = 'Invalid salary value'

def percentSavedInput(event):
  value = document['percentSaved'].value
  document['percentSavedLabel'].textContent = 'Percent Saved (%): ' + str(value) + '%';

def saveGoalInput(event):
  value = document['saveGoal'].value
  (valid, value) = valid_save_goal(value)

  if (valid):
    document['saveGoalWarning'].textContent = ''
  else:
    document['saveGoalWarning'].textContent = 'Invalid save goal value'
