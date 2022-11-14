import time


class Application:

    def __init__(self, company_name: str, status: str, notes: str):
        self.company_name = company_name
        self.status = status
        self.notes = notes
        self.salary = ''
        self.get_salary()

    def __str__(self):
        return f'company: {self.company_name}\n' \
               f'status: {self.status}\n' \
               f'notes: {self.notes}\n' \
               f'expected salary: {self.salary}'

    def get_salary(self):
        print('New application created!\n')
        with open('salary.txt', 'w') as f:
            f.write(self.company_name)

        time.sleep(2.2)
        with open('salary.txt', 'r') as f:
            salary = f.readline()
            self.salary = salary

    def edit_app(self):
        print("Here are the current details of your application:\n")
        print(self.__str__())


if __name__ == "__main__":
    zillow = Application("Zillow", "accepted offer", "starting in June")
    zillow.edit_app()
