from seleniumbase import BaseCase

class HomePageTests(BaseCase):
  def test_bmi(self):
    # on load
    self.assert_element_not_visible('label#bmiResult')
    
    # valid input
    self.update_text('input#weight', 100)
    self.js_click('button#calculateBMI')
    self.assert_element_visible('label#bmiResult')

    # invalid input
    self.update_text('input#weight', 'a')
    self.click('button#calculateBMI')
    self.assert_element_not_visible('label#bmiResult')

  def test_retirement(self):
    # on load
    self.assert_element_not_visible('label#retirmentResult')
    
    # valid input
    self.update_text('input#salary', 30000)
    self.update_text('input#saveGoal', 100000)
    self.js_click('button#calculateRetirement')
    self.assert_element_visible('label#retirementResult')

    # invalid input
    self.update_text('input#salary', 'a')
    self.update_text('input#saveGoal', 'a')
    self.js_click('button#calculateRetirement')
    self.assert_element_not_visible('label#retirementResult')

  def test_inputs(self):
    # No errors on load
    self.assert_element_not_visible('label#weightWarning')
    
    self.assert_element_not_visible('label#salaryWarning')
    self.assert_element_not_visible('label#saveGoalWarning')

    # Invalid strings
    self.update_text('input#weight', 'a')
    self.assert_text('Invalid weight value', 'label#weightWarning')

    self.update_text('input#salary', 'a')
    self.assert_text('Invalid salary value', 'label#salaryWarning')

    self.update_text('input#saveGoal', 'a')
    self.assert_text('Invalid save goal value', 'label#saveGoalWarning')

    # Return to valid inputs
    self.update_text('input#weight', 1)
    self.assert_element_not_visible('label#weightWarning')

    self.update_text('input#salary', 1)
    self.assert_element_not_visible('label#salaryWarning')

    self.update_text('input#saveGoal', 1)
    self.assert_element_not_visible('label#saveGoalWarning')

    # Invalid numbers
    self.update_text('input#weight', 0)
    self.assert_text('Invalid weight value', 'label#weightWarning')

    self.update_text('input#salary', 0)
    self.assert_text('Invalid salary value', 'label#salaryWarning')

    self.update_text('input#saveGoal', 0)
    self.assert_text('Invalid save goal value', 'label#saveGoalWarning')

    
    self.update_text('input#weight', -0.1)
    self.assert_text('Invalid weight value', 'label#weightWarning')

    self.update_text('input#salary', -0.1)
    self.assert_text('Invalid salary value', 'label#salaryWarning')

    self.update_text('input#saveGoal', -0.1)
    self.assert_text('Invalid save goal value', 'label#saveGoalWarning')