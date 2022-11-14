import app_tracker


class App:

    def __init__(self):
        self.applications = []

    def main(self):

        print("Welcome to your application tracker! What would you like to do? \n")

        while True:
            print("Commands:\n"
                  "'view' (view all apps)\n"
                  "'new' (create a new application)\n"
                  "'edit' (edit an existing application)\n"
                  "'delete' (delete an existing application)\n")
            command = input("Enter command here: \n")

            match command:
                case 'view':
                    self.view()
                case 'new':
                    self.new()
                case _:
                    print("\nWe don't recognize that command! Please try again.\n")

    def new(self):
        company = input("What's the company's name? ")
        status = input("What's your application status? ")
        details = input("Any details you want to include? ")
        new_app = app_tracker.Application(company, status, details)
        self.applications.append(new_app)

    def view(self):
        for i, val in enumerate(self.applications):
            print(f'\n'
                  f'App number: {i + 1}\n'
                  f'Company: {val}\n')

        print("What's next? \n"
              "'edit' (edit one of these apps)\n"
              "'delete' (delete one of these apps)\n"
              "'home' go back home\n")
        choice = input()

        match choice:
            case 'edit':
                pass
            case _:
                pass


app = App()
app.main()
