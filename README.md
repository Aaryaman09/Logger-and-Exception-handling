# Logger and Exception handling

In your module or class, import the CustomLogger and CustomExceptionHandler classes.
```python
from my_logger import CustomLogger, CustomExceptionHandler

class MyClass:

    def __init__(self):
        self.logger = CustomLogger('myclass.log')
        self.exception_handler = CustomExceptionHandler(self.logger)
        sys.excepthook = self.exception_handler.handle_exception

    def my_method(self):
        self.logger.log('This is a log message from MyClass.my_method()')

        try:
            # do something that might raise an exception
        except Exception as e:
            raise Exception('An error occurred') from e
```

In this example, we import the CustomLogger and CustomExceptionHandler classes from the my_logger module and create instances of them in the __init__ method of our class. We set the sys.excepthook to the exception handler's handle_exception method. In the my_method method, we log a message with the logger and wrap some code in a try-except block to handle any exceptions that might occur.
