

class Person:

    def __init__(self, firstname: str, lastname: str, email: str, phone: str, adress: str):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.adress = adress

    def Id(self) -> int:
        return self.id

    def Firstname(self) -> str:
        return self.firstname

    def Lastname(self) -> str:
        return self.lastname

    def Phone(self) -> str:
        return self.phone

    def Email(self) -> str:
        return self.email

    def Adress(self) -> str:
        return self.adress

    def setId(self, id):
        self.id = id

    def setFirstname(self, firstname):
        self.firstname = firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, email):
        self.email = email

    def setAdress(self, adress):
        self.adress = adress

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return str(self.firstname).lower() == str(other.firstname).lower() and str(self.lastname).lower() == str(other.lastname).lower() or str(self.firstname).lower() == str(other.lastname).lower() and str(self.firstname).lower() == str(other.lastname).lower()
        else:
            return False


# s = Person("Ahmed", "Elbouchouki", "admin@elbouchouki.com",
#            "0680808080", "adress blablabla blabla lnla nla")
