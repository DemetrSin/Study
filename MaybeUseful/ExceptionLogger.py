import os.path
import sys


class Logger(Exception):
    file_name = 'logger.log'

    def __init__(self,  *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def write_logs(self):
        with open(self.file_name, 'w') as file:
            file.write(f"{os.path.basename(__file__)}\n")
            if self.args:
                for arg in self.args:
                    file.write(f"{self.__class__.__name__}:  {arg}\n")
            if self.kwargs:
                for k, v in self.kwargs.items():
                    file.write(f"{self.__class__.__name__}:  {k}: {v}\n")

    @classmethod
    def set_file_name(cls, file_name):
        cls.file_name = file_name

    def __str__(self):
        return f"{self.args}, {self.kwargs}"


try:
    raise Logger(file=Logger.file_name, exception='Custom made exception')
except Logger as e:
    e.write_logs()


try:
    # Logger.file_name = 'logger2.log'
    Logger.set_file_name('logger2.log')
    raise Logger('Any text here', 'And try this.', file=__name__, problem='Test case')
except Logger as e:
    e.write_logs()


try:
    1 / 0
except Exception as e:
    Logger.file_name = 'logger3.log'
    Logger(e, sys.exc_info(), filename='logs.log').write_logs()
