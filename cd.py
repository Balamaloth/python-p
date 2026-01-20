class Account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account_no = acc


    def debit(self , acc):
        self.balance -= acc
        print("debit amunt is :", acc)
        print("available balannce is :", self.balance)

    def credit(self , acc):
        self.balance += acc
        print("credit amount is :", acc)
        print("available banance is : " , self.balance)

    def get_balance(self): 
        return self.balance
    
acc1 = Account(50000 , 1223334444)
acc1.debit(4500)
acc1.credit(55000)