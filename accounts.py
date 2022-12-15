# importing random and daytime module to use them in our class
import random
import datetime


class BasicAccount():
    """
    basicAccount is one of the accounts that we offer in banks.It has the Account holder name,
    Account number, balance, card number and expiration time.
    """
    acNumber = 0

    # The account number is s increasing For each instance that we wish to create.

    def __init__(self, theAcName: str, theOpeningBalance: float):
        self.name = theAcName
        BasicAccount.acNumber += 1
        self.acNum = str(BasicAccount.acNumber)
        self.balance = theOpeningBalance
        self.cardNumber = str(random.randint(1111111111111111, 9999999999999999))
        self.cardExp = (datetime.datetime.now().month, int(str(datetime.datetime.now().year + 3)[2:4]))
        print(f"Dear {self.name} Thanks for joining our bank")

    def __str__(self):
        return f"Dear{self.name} you have £ {self.balance}"

    def deposit(self, theAmount):
        """
        Deposit money to the account.
        Parameters:
            theAmount: float - The amount of money that customer wanted to deposit it Hss to be positive
        Returns:
            Nothing
        """
        if theAmount > 0:
            self.balance += theAmount

    def withdraw(self, theAmount):
        """
        Withdraw money to from account.
        Parameters:
            theAmount: float - The amount of money that customer wanted to withdraw it Has to be between zero and the balance
        Returns:
            Nothing
        """
        if 0 < theAmount <= self.balance:
            self.balance -= theAmount
            print(f"{self.name} has withdrawn £{theAmount}. New balance is £{self.balance}")
        else:
            print(f"Ypu Can not withdraw £{theAmount}")

    def getAvailableBalance(self):
        """
        Get available balance.
        Parameters:
            Nothing
        Returns:
            Remaining balance
        """
        return self.balance

    def getBalance(self):
        """
        Get available balance.
        Parameters:
            Nothing
        Returns:
            Remaining balance
        """
        return self.balance

    def printBalance(self):
        """
        Print the balance and make it visible
        Parameters:
            Nothing
        Returns:
            Nothing
        """
        print(f"Hi Dear {self.name} your current balance is £{self.balance}")

    def getName(self):
        """
        Return the account holder name
        Parameters:
            Nothing
        Returns:
            Name of the account holder
        """
        return str(self.name)

    def getAcNum(self):
        """
        Return The account holder unique account number
        Parameters:
            Nothing
        Returns:
            Unique account number of Account holder
        """
        return str(self.acNum)

    def issueNewCard(self):
        """
        Generate a new Card number digit and expiration date for
        a new card when the card is lost or expired.
        Parameters:
            Nothing
        Returns:
            Nothing
        """
        self.cardNumber = str(random.randint(1111111111111111, 9999999999999999))
        self.cardExp = (datetime.datetime.now().month, int(str(datetime.datetime.now().year + 3)[2:4]))

    def closeAccount(self):
        """
       Close the account when a Account holder wants and the Account holder provides the remaining balance.
        Parameters:
            Nothing
        Returns:
            True
        """
        BasicAccount.withdraw(self, self.balance)
        return True


class PremiumAccount(BasicAccount):
    """
    Account-holders could be eligible for an overdraft; They take the initial limit
     when they open an account and in the future, they may be able to change the limit.
    """

    def __init__(self, theAcName, theOpeningBalance, theInitialOverdraftLimit):
        super().__init__(theAcName, theOpeningBalance)
        self.overdraftLimit = theInitialOverdraftLimit
        self.overdraft = False

    def __str__(self):
        return f"Dear{self.name} you have £ {self.balance} You are illegible for £ {self.overdraftLimit} overdraft"

    def setOverdraftLimit(self, newLimit: float):
        """
        Set New overdraft limit to the account
        Parameters:
            New overdraft limit : float
        Returns:
            Nothing
        """
        self.overdraftLimit = newLimit

    def getAvailableBalance(self):
        """
        Calculate available balance(Balance + overdraft limit) .
        Parameters:
            Nothing
        Returns:
            available balance
        """
        return float(self.balance + self.overdraftLimit)

    def printBalance(self):
        """
        Print the balance and make it visible
        Parameters:
            Nothing
        Returns:
            Nothing
        """
        if self.overdraft:
            print(f"Your balance is £{self.balance}, Your overdraft limit {self.overdraftLimit} "
                  f"and your remaining overdraft limit is {self.overdraftLimit + self.balance} ")
        else:
            print(f"Your balance is £{self.balance}, Your overdraft limit {self.overdraftLimit}")

    def deposit(self, theAmount):
        """
        Deposit money to the account(With depositing money overdraft situation may change).
        Parameters:
            theAmount: float - The amount of money that customer wanted to deposit it Hss to be positive
        Returns:
            Nothing
        """
        if theAmount > 0:
            self.balance += theAmount
            if self.balance > 0:
                self.overdraft = False

    def withdraw(self, theAmount):
        """
        Withdraw money from the account. This amount must be between zero and aggregation of balance
        and overdraft limit,If this condition shall not satisfy the withdrawal couldn't be done.
        Parameters:
            theAmount: float - The amount of money that customer wanted to withdraw
        Returns:
            Nothing
        """
        if 0 < theAmount <= self.balance + self.overdraftLimit:
            self.balance -= theAmount
            if self.balance < 0:
                self.overdraft = True
            print(f"{self.name} has withdrawn £{theAmount}. New balance is £{self.balance}")
        else:
            print(f"Can not withdraw £{theAmount}")

    def closeAccount(self):
        """
       Close the account when a Account holder wants and the Account holder provides the remaining balance.
       However if account holder is overdrawn it couldn't close the account.
        Parameters:
            Nothing
        Returns:
            True or False
        """
        if self.balance >= 0:
            PremiumAccount.withdraw(self, self.balance)
            print(f"Dear {self.name} we are looking forward to see you again")
            return True
        else:
            print("yo cant close account ")
            return False
