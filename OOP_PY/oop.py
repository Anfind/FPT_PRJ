class SieuNhan:
    dataPower = 50
    def __init__(self, para_ten, para_color, para_vukhi):
        self.ten = para_ten
        self.color = para_color
        self.ten = para_vukhi
        SieuNhan.dataPower += 1
        self.dP = SieuNhan.dataPower 
    def power(self):
        if self.color == "red":
            return "fire"
        elif( self.color == "blue"):
            return "water"
        elif( self.color == "green"):
            return "plant"
        else:
            return 0

Sieu_nhan_a = SieuNhan("ThaiAn", "green", "Kiem")
Sieu_nhan_b = SieuNhan("ThaiAn", "green", "Kiem")

# print(Sieu_nhan_a.power())
print(Sieu_nhan_a.dP)
print(Sieu_nhan_b.dP)
