from config import app as application
from views import *

if __name__ == '__main__':
    application.run(debug=True, port=5000, host='0.0.0.0')