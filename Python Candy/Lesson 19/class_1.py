class Customer:
    def __init__(self, name, surname,age="Qeyd olunmayıb",email="Qeyd olunmayıb",id="Qeyd olunmayıb") -> None: #None bir növ boş qayıtmağa icazə vermir və errorun qarşısını alır
        #self dəyişməsi mümkün olan bir yazıdır
        # self.a = name #a-nı selfdə tanıdıb, içinə name atributunu value olaraq əlavə edirsən
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.id = id

    def show_info(self):
        print(f"Müştərinin məlumatları: \nAd: {self.name},\nSoyad: {self.surname}")
        print(f"Yaş: {self.age},\nGmail: {self.email},\nİdentifikasiya Nömrəsi: {self.id} ")

info = Customer("Aydan","Muxtarzade") #1 ci def
info.show_info()
