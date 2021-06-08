class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accountC = bankAccount(int_rate=0.02,balance=0)
        self.accountA = bankAccount(int_rate=0.09,balance=0)
    
    def deposito(self,amount,accountType):
        if accountType == "Corriente":
            self.accountC.deposit(amount)
        elif accountType == "Ahorros":
            self.accountA.deposit(amount)
        else:
            print("!!!Tipo de cuenta invalido!!!")
        return self
    
    def retiro(self,amount,accountType):
        if accountType == "Corriente":
            self.accountC.withdraw(amount)
        elif accountType == "Ahorros":
            self.accountA.withdraw(amount)
        else:
            print("--!!!Tipo de cuenta invalido!!!--")
        return self
    
    def display_user_balance(self):
        print("Usuario: ",self.name,",","Saldo cuenta Corriente:",self.accountC.balance)
        print("Usuario: ",self.name,",","Saldo cuenta Ahorros:",self.accountA.balance)
        return self

    def tranferencia(self,amount,user):
        self.accountC.balance -= amount
        user.accountC.balance += amount
        print("**************")
        print("Saldo de:",self.name,":",self.accountC.balance)
        print("Saldo de:",user.name,":",user.accountC.balance)
        print("**************")

class bankAccount:
    def __init__(self,int_rate,balance:0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("------------")
            print("Fondos insuficientes: cobrar una tarifa de 5$")
            print("------------")
            self.balance -= 5       
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Saldo: ", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
#USUARIOS
jose = Usuario("Jose Arevalo", "josealfredoee@hotmail.es")
victor = Usuario("Victor Arevalo", "vity_arevalo@hotmail.com")
#RETIROS Y 
jose.deposito(200,"Corriente").deposito(100,"Ahorros").deposito(50,"Ahorros").retiro(200,"Ahorros").display_user_balance()

victor.deposito(100,"Corriente").deposito(300,"Ahorros").retiro(90,"Corriente").retiro(10,"Ahorros").retiro(20,"Corriente").display_user_balance()

victor.deposito(100,"perro").retiro(100,"perro")

jose.tranferencia(250,victor)