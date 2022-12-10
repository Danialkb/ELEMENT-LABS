from typing import List, Optional
from bank_account import BankAccount


class AccountRepo:
    accs: List[BankAccount] = []

    def create_acc(self, name: str, surname: str, password: str) -> None:
        acc = BankAccount(name, surname, password)
        self.accs.append(acc)

    def get_bank_acc(self, name: str, surname: str, password: str) -> Optional[BankAccount]:
        user = next(
            (u for u in self.accs if name == u.name and surname == u.surname and u.check_password(password)),
            None
        )

        if not user:
            print('No such user')
            return
        return user
