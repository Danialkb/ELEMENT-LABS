from typing import Optional
from bank_account import BankAccount
from repository import AccountRepo


class UserHandler:
    repos: AccountRepo

    def __init__(self, repo: AccountRepo):
        self.repos = repo

    def sign_up(self, name: str, surname: str, password: str) -> None:
        name = name.strip()
        surname = surname.strip()
        password = password.strip()

        if not self._valid_user(password=password):
            return None

        self.repos.create_acc(name=name, surname=surname, password=password)
        print('Succesfully created!')

    def sign_in(self, name: str, surname: str, password: str) -> Optional[BankAccount]:
        return self.repos.get_bank_acc(name=name, surname=surname, password=password)

    @staticmethod
    def _valid_user(password: str):
        if len(password) < 8:
            print('password is too short')
            return False

        return True
