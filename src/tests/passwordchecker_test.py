import unittest 
from pwd_checker import PasswordStrength

class TestChecker(unittest.TestCase):
  
  def test_password_strength(self):
    # Test password that is less than 8 characters long
    self.assertFalse(PasswordStrength.password_strength("p@ssW1"))
  
    # Test password that does not contain an uppercase letter
    self.assertFalse(PasswordStrength.password_strength("p@ssword1"))
  
    # Test password that does not contain a lowercase letter
    self.assertFalse(PasswordStrength.password_strength("P@SSWORD1"))
  
    # Test password that does not contain a digit
    self.assertFalse(PasswordStrength.password_strength("P@ssword"))
  
    # Test strong password
    self.assertTrue(PasswordStrength.password_strength("P@ssw0rd"))
 