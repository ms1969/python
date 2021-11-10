class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) == False:
            print("Ошибочная почта")
            return None
        email1 = email[email.index('@')::]
        if email.count('@') == 1 and email1.count('.') > 0 and (
                email1.index('.') - email1.index('@')) > 1:
            self.__email = email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait