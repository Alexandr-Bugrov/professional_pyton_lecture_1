from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def get_data_now():
    print(datetime.now())

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    get_data_now()

