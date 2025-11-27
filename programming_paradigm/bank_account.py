# bank_account.py

class BankAccount:
    """
    A simple BankAccount class that demonstrates encapsulation
    by keeping the balance private and providing public methods
    to interact with it.
    """

    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize the bank account with an optional initial balance.
        Default is 0.0 if not provided.
        """
        # Private attribute (by convention with leading underscore)
        self._account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """
        Deposit a positive amount into the account.
        
        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        self._account_balance += amount
        # We don't print here to keep the class reusable and clean

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw an amount from the account if sufficient funds exist.
        
        Args:
            amount (float): The amount to withdraw.
        
        Returns:
            bool: True if withdrawal succeeded, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self._account_balance:
            return False  # Insufficient funds
        
        self._account_balance -= amount
        return True

    def display_balance(self) -> None:
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")
