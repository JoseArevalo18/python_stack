class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
    
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("USUARIO:",self.name,"-","SALDO ACTUAL:",self.account_balance)
        return self

    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        print("SALDO DE:",self.name,"==",self.account_balance)
        print("SALDO DE:",user.name,"==",user.account_balance)

                    #USUARIOS
jose   = User("Jose Arevalo", "josealfredoee@hotmail.es")
victor = User("Victor Arevalo", "vity_arevalo@hotmail.com")
mecias = User("Mecias Arevalo", "meciasarevalo@hotmail.com")

                #OPERACIONES DE TRANSFERENCIA
#USUARIO1 JOSE
jose.make_deposit(200).make_deposit(500).make_deposit(500).make_withdrawal(300).display_user_balance()
#USUARIO2 VICTOR
victor.make_deposit(2400).make_deposit(200).make_withdrawal(1200).make_withdrawal(20).display_user_balance()
#USUARIO3 MECIAS
mecias.make_deposit(4800).make_withdrawal(300).make_withdrawal(200).make_withdrawal(50).display_user_balance()
#TRANSFERENCIA ENTRE USUARIOS
jose.transfer_money(200,mecias)

jose.display_user_balance()
mecias.display_user_balance()