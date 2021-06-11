class MathDojo: 
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        #tu codigo aqui
        for i in range(len(nums)):
            self.result += nums[i]
        self.result += num
        return self
    def subtract(self,num,*nums): 
        #tu codigo aqui
        for i in range(len(nums)):
            self.result -= nums[i]
        self.result -= num
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) #debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!