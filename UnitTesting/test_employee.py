import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

	@classmethod	
	def setUpClass(self):		# este método de classe corre primeiro que todos
		pass

	@classmethod
	def tearDownClass(self):	# este método de classe corre no fim que todos
		pass

	def setUp(self):			# este método corre antes de cada teste
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)


	def tearDown(self):			# este método corre no fim de cada teste
		pass	


	def test_email(self):

		self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
		
		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Sue Smith')
		
		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Jane Smith')

	def test_apply_raise(self):
		
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)


	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True		# caso em que a conexão é bem feita
			mocked_get.return_value.text = 'Success'
			
			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Schafer/May')
			self.assertEqual(schedule, 'Success')



			mocked_get.return_value.ok = False		# caso em que a conexão é mal feita
			
			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Smith/May')
			self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
	unittest.main()	