from keyword import iskeyword

class User:
    def __init__(self, username, password):
        validate_name(self, username)
        self.username = username
        if not validate_password(self, password):
            raise Shortpassword(password=password)
        self.password = password

def validate_name(self, username):
    if len(username)<4:
        raise NametoShort(name=username)


def validate_password(self, password):
    return any(char.isdigit() for char in password) and any(char.isalpha for char in password)

class Shortpassword(Exception):
    def __init__(self, password, base_message="Le mot de passe ne match pas les specifications", *args, **kwargs):
        msg = f"{base_message}: {password}"
        super().__init__(msg, *args, **kwargs)


class NametoShort(Exception):
    def __init__(self, name, base_message = "Le nom d’utilisateur est trop court",*args, **kwargs):
        msg = f"{base_message}= {name}"
        super().__init__(msg, *args, **kwargs)

paul = User(username="polo", password="toto2")

pierre = User(username="pierre", password="hier")

lau = User(username="lau", password="ras2")