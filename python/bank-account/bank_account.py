from threading import Lock

class BankAccount:
    def __init__(self):
        self.close()
        self._lock = Lock()

    # @property
    # def balance(self):
    #     return self._balance
    #
    # @property
    # def closed(self):
    #     return self._closed

    def get_balance(self):
        if not self._closed:
            return self._balance
        else:
            raise ValueError("The account is not opened")

    def open(self):
        if self._closed:
            self._balance = 0
            self._closed = False
        else:
            raise ValueError("The account is not closed")

    def deposit(self, amount):
        self._lock.acquire()
        if not self._closed:
            if amount >= 0:
                self._balance += amount
            else:
                raise ValueError("Can't deposit a negative amount")
        else:
            raise ValueError("The account is not opened")
        self._lock.release()

    def withdraw(self, amount):
        self._lock.acquire()
        if not self._closed:
            if amount < 0:
                raise ValueError("Can't withdraw a negative amount")
            elif amount <= self._balance:
                self._balance -= amount
            else:
                raise ValueError("Bankruptcy!")
        else:
            raise ValueError("The account is not opened")
        self._lock.release()

    def close(self):
        if not hasattr(self, "_closed") or not self._closed:
            self._closed = True
        else:
            raise ValueError("The account is not opened")
