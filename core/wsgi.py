
import sys
import os
from api.main import app

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)


application = app

if __name__ == '__main__':
    application.run()
