class BankAccount:
    history = []

    def __init__(self, name, balance,):
        self.name = name
        self.__balance = balance

    def get_name(self):
        print(f'ФИО - {self.name}')

    def get_balance(self):
        print(f'На балансе {self.__balance}')

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Внесение наличных на счет {amount}')
        self.history.append('Внесение наличных')

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print(f'Снятие наличных {amount}')
        self.history.append('Снятие наличных')

    def history_list(self):
        print('\nИстория платежей:')
        for i in self.history:
            print(f'- {i}')


account = BankAccount('Иванов Артем Рустамович', 56000)

account.get_name()
account.get_balance()
account.deposit(43823)
account.withdraw(9000)

account.history_list()