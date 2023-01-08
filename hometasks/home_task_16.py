"""

ДЗ 16. Классы Employee и Company

"""

source = "{:,d} USD"


class Company:
    country = 'Ukraine'

    def __init__(self, company_name, company_type, total_employees, enps, monthly_income, monthly_outcome):
        self.company_name = company_name
        self.company_type = company_type
        self.total_employees = total_employees
        self.enps = enps
        self.monthly_income = monthly_income
        self.monthly_outcome = monthly_outcome

    def how_satisfy_for_employees(self):
        """Выводит сообщенеие, насколько сотрудники удовлетворены тем что работают в конкретной в компании"""
        if 0 <= self.enps <= 30:
            not_bad = 'Good range, however, the company still has room to move and what to improve'
            print('\n'.join(['*' * (len(not_bad)+4), '* {} *'.format(not_bad), '*' * (len(not_bad)+4)]))
        elif 30 < self.enps <= 70:
            good = 'The company is a good employer and has more happy employees than unhappy employees'
            print('\n'.join(['*' * (len(good)+4), '* {} *'.format(good), '*' * (len(good)+4)]))
        elif 70 < self.enps <= 100:
            excellent = 'Employees like to work in the company and they actively recommend it to their friends, ' \
                        'increasing the recognition and brand of the employer'
            print('\n'.join(['*' * (len(excellent)+4), '* {} *'.format(excellent), '*' * (len(excellent)+4)]))

    def increase_monthly_income(self, value_for_increase):
        """
        Увеличивает ежемесячный доход на переданное аргументом значение
        """
        self.monthly_income += value_for_increase
        increased_income = source.format(self.monthly_income)
        print((f'For {self.company_name} monthly income was increased at {value_for_increase}.'
               f'Current value is {increased_income}'))

    def decrease_monthly_income(self, value_for_decrease):
        """
         Уменьшает ежемесячный доход на переданное аргументом значение
        """
        self.monthly_income -= value_for_decrease
        decreased_income = source.format(self.monthly_income)
        print((f'For {self.company_name} monthly income was decreased at {value_for_decrease}.'
               f'Current value is {decreased_income}'))

    def net_income(self, months=None):
        """Возвращает значение чистой прибыли за 1 месяц по дефолту, иначе чистая прибыль возвращается
        за переданное число месяцев"""
        net_difference = self.monthly_income - self.monthly_outcome
        if months:
            plural = net_difference * months
            beautify_plural = source.format(plural)
            return beautify_plural
        else:
            single = source.format(net_difference)
            return single

    def greater_than(self, number):
        """Метод сравнения фактического количества сотрудников компании
        с переданным в качестве аругмента"""
        if self.total_employees < number:
            difference_negative = number - self.total_employees
            print(f'In {self.company_name} {difference_negative} employees less! '
                  f'Total number is {self.total_employees}')
        elif self.total_employees == number:
            print(f'In {self.company_name} exactly {number} employees!')
        else:
            difference_positive = self.total_employees - number
            print(f'In {self.company_name} {difference_positive} employees more. '
                  f'Total number is {self.total_employees}')

    @staticmethod
    def is_available_to_come(year, month, day):
        """
        Определяет переданную дату
        Печатает текст сообщения и календарик на месяц года который передан, в случае если переданная дата =
        не рабочий день
        """
        import calendar
        date_res = calendar.weekday(year, month, day)
        if date_res == 5 or date_res == 6:
            doors_closed = 'Unfortunately, at the date you choose the doors in office closed. \n' \
                           'We will glad to see you at any weekday! \n' \
                           'Please, choose another day! \n'
            print(doors_closed)
            calendar.prmonth(theyear=year, themonth=month, w=3, l=1)
        else:
            doors_opened = 'We will glad to see you at the office!'
            print(doors_opened)

    @classmethod
    def create_company_with_globallity(cls, company_name, company_type, total_employees, enps, monthly_income,
                                       monthly_outcome, globallity):
        """
        Создает компанию с полем globallity
        """
        instance = cls(company_name, company_type, total_employees, enps, monthly_income, monthly_outcome)
        instance.globallity = globallity
        return instance


epam = Company('Epam Ukraine', 'IT', 12600, 88, 189254169, 124589635)
soft_serve = Company('Soft Serve', 'IT', 10918, 91, 98541962, 76458142)
global_logic = Company('Global Logic', 'IT', 7379, 79, 74695365, 48365125)
luxoft = Company('Luxoft_Ukraine', 'IT', 4000, 95, 28987456, 16123654)
evoplay = Company('Evoplay', 'IT', 3958, 54, 18789456, 9145789)

epam.how_satisfy_for_employees()
print()
evoplay.how_satisfy_for_employees()
print()
print(luxoft.net_income())
print()
soft_serve.greater_than(10918)
print()
sigma_software = Company.create_company_with_globallity('Sigma Software', 'IT', 2000, 12, 1254878, 987546, 'International')
print(sigma_software.globallity)
print()
Company.is_available_to_come(2023, 10, 14)
print()
print(source.format(epam.monthly_income))
epam.increase_monthly_income(17545)
print()
print(source.format(evoplay.monthly_income))
evoplay.decrease_monthly_income(100000)


class Employee:
    schedule = 'Monday-Friday'

    def __init__(self, name, age, gender, experience_years, position, level, salary, start_working_date):
        self.name = name
        self.age = age
        self.gender = gender
        self.experience_years = experience_years
        self.position = position
        self.level = level
        self.salary = salary
        self.start_working_date = start_working_date

    def raise_salary(self, amount):
        """Увеличивает значение salary для объекта на значение переданное аргументом amount"""""
        self.salary += amount
        print(f'Salary of {self.name} was raised at {amount}!')
        print(f'Now {self.name} earning {self.salary} per month.')

    def work_duration_from_start(self):
        """Отображает количество дней от начала работы сотрудника"""
        import datetime
        current_date = datetime.datetime.today()
        self_date_obj = datetime.datetime.strptime(self.start_working_date, '%m-%d-%y')
        delta = current_date - self_date_obj
        print(f'{self.name} start work {delta} ago')

    def get_experience(self):
        """Возвращает количество лет опыта"""
        print(f'{self.name} has {self.experience_years} years of experience')

    @staticmethod
    def get_working_hours(day):
        print('From 9am till 6pm')

    @classmethod
    def change_schedule(cls, new_schedule: str):
        """Меняет график для сотрудников в переменой класса"""
        cls.schedule = new_schedule
        print(f'Schedule of employees was changed. Starting from tomorrow new schedule: {cls.schedule}')


oskar = Employee('Oskar', 54, 'Male', 3, 'Python Developer', 'Middle', 2300, '11-17-20')
david = Employee('David', 31, 'Male', 1, 'C++ Developer', 'Trainee', 350, '02-14-22')
emily = Employee('Emily', 24, 'Female', 7, 'Front end Developer', 'Senior', 4245, '08-23-17')
rafael = Employee('Rafael', 40, 'Male', 4, 'QA Engineer', 'Middle', 1730, '03-10-18')
yerlina = Employee('Yerlina', 26, 'Female', 2, 'UI/UX Designer', 'Junior', 1140, '04-21-21')
genesis = Employee('Genesis', 19, 'Female', 8, 'Product manger', 'Senior', 3685, '05-19-22')
franchesca = Employee('Franchesca', 22, 'Female', 0, 'Support', 'Junior', 800, '07-14-20')

# oskar.raise_salary(150)
# print()
# genesis.get_working_hours(day=1)
# print()
# print(genesis.schedule)
# print()
# david.work_duration_from_start()
# print()
# yerlina.get_experience()
# print()
# Employee.change_schedule('Monday-Saturday')
