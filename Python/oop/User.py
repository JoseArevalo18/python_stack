class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
    
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("USUARIO:",self.name,"-","SALDO:",self.account_balance)

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
#USUARIO JOSE
jose.make_deposit(200)
jose.make_deposit(500)

jose.make_withdrawal(40)
jose.make_withdrawal(30)

jose.display_user_balance()
#USUARIO VICTOR
victor.make_deposit(2400)
victor.make_deposit(200)

victor.make_withdrawal(1200)
victor.make_withdrawal(20)

victor.display_user_balance()
#USUARIO MECIAS
mecias.make_deposit(4500)
mecias.make_deposit(300)

mecias.make_withdrawal(200)
mecias.make_withdrawal(50)
mecias.display_user_balance()
#TRANSFERENCIA ENTRE USUARIOS
mecias.transfer_money(250,jose)
mecias.transfer_money(300,victor)

victor.transfer_money(90,mecias)
victor.transfer_money(100,jose)

jose.transfer_money(80,mecias)
jose.transfer_money(200,victor)
