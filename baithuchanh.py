class Hocsinh :
    def __init__(self,name,diachi,chieucao,cannang,hocluc):
        self.name = name
        self.diachi = diachi
        self.chieucao = chieucao
        self.cannang = cannang
        self.hocluc = hocluc
    def speakinfo(self) :
        print(f"Tên học sinh là {self.name}, Địa chỉ là {self.diachi}, \nChiều cao của {self.name} là {self.chieucao}, Cân nặng của \n{self.name} là {self.cannang}, học lực của {self.name} là {self.hocluc}")
    def update_diachi(self) :
        self.diachi = input(f"Nhập địa chỉ mới cho {self.name}: ")
        print(f"Địa chỉ mới của {self.name} là {self.diachi}")
    def update_chieucao_cannang(self) :
        print("Đã đến kì kiểm tra sức khỏe rồi")
        self.chieucao = input(f"Hãy nhập chiều cao mới cho {self.name} nào: ")
        self.cannang = input(f"Hãy nhập cân nặng mới của {self.name}: ")
        print(f"Chiều cao mới của {self.name} là: {self.chieucao} , Cân nặng mới của {self.name} là: {self.cannang}")  
ten_hocsinh = input("Hãy nhập tên của học sinh: ")
diachi_hocsinh = input("Hãy nhập địa chỉ của học sinh: ")
chieu_cao = input("Hãy nhập chiều cao của học sinh: ")
can_nang = input("Hãy nhập cân nặng cho học sinh: ")
hoc_luc = input("Hãy nhập học lực của học sinh: ")
mystudent = Hocsinh(ten_hocsinh, diachi_hocsinh, chieu_cao, can_nang, hoc_luc)
mystudent.speakinfo()
mystudent.update_diachi()
mystudent.update_chieucao_cannang()
mystudent.speakinfo()