## Tiny Testing Framework used in example.py

### Introduction:

tylerkcraine and ntgomes made this in response to the fact that we couldn’t use pytest for our unit testing, and that the tests (examples) must run during program execution. Keep in mind this testing framework is a bit more limited than pytest.

### General Setup:

You can import things from the src folder as you normally would. Ignore the auto completion complaining its taken care of in the example file. 

#### General Test Anatomy:
All of your tests must be contained in the example.py

Define a new method in the Example class within example.py. If the method starts with `eg_`, then it will be considered as a test for the class to run.

```python
class Example(object): # Inside here is where you will add your test method
	def eg_the(self):
		# An existing sample test method
		self.params = The()
        oo(self.params.the)
		assert true
	
	def eg_myNewPassingTest(self):
		#Passing test
		assert False
	def eg_myNewFailingTest(self):
		#Passing test
		assert False
```

## Note for Pycharm:
If you are using PyCharm with this framework, you will have to switch the unittest option for testing in your project settings.
To do this press (Ctrl + Alt + S). The setting will be under Tools > Python Integrated Tools. Change "default test runner" to unittest using the dropdown.