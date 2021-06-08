class bankAccount:
	def __init__(self,int_rate,balance:0):
		self.int_rate = int_rate
		self.balance = balance

	def deposito(self,amount):
		self.balance += amount
		return self

	def retiro(self,amount):
		if amount > self.balance:
			print("Fondos insuficientes: cobrar una tarifa de 5$")
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
cuenta1 = bankAccount(0.08,200)
cuenta2 = bankAccount(0.04,500)
#DEPOSITIOS Y RETIROS
#En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta1.deposito(100).deposito(100).deposito(200).retiro(500).yield_interest().display_account_info()
#En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta2.deposito(200).deposito(150).retiro(900).retiro(100).retiro(50).retiro(50).yield_interest().display_account_info()