from bank import Account

account = Account(10024)
account.save()
print(account.get_account_number())
