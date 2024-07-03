from datetime import *
from application.salary import *
from application.db.people import *

if __name__ == "__main__":
    print(datetime.now())
    calculate_salary()
    get_employees()