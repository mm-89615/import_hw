import datetime
from application import salary
from application.db import people




if __name__ == "__main__":
    print(datetime.datetime.now())
    salary.calculate_salary()
    people.get_employees()