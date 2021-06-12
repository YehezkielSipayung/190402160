print("INFORMASI WIRAUSAHA DI PROVINSI SUMATERA UTARA")
class usaha:
	def __init__(self, namausaha, usia, alamat, bidang):
		self.namausaha = namausaha
		self.usia = usia
		self.alamat = alamat
		self.bidang = bidang
		self.status="unknown"    
		if(usia<10):
			self.status="usaha baru"
		else:
			self.status="usaha tua"

	def Nama(self):
		print("Namausaha " + self.namausaha)       
	def Usia(self):
		print("Usia " + str(self.usia))
	def Alamat(self):
		print("Alamat " + self.alamat)
	def Bidang(self):
		print("Bidang " + self.bidang)
        
	def print(self):
		print(self.namausaha+", "+str(self.usia)+", "+self.alamat+","+self.bidang+", "+str(self.status))        

p1 = usaha("JATI AGUNG", 12, "JL. SUDIRMAN", "FURNITURE")
p2 = usaha("BURNIG HALL", 11, "JL. MERDEKA", "KULINER")
p3 = usaha("MEDAN JAYA", 14, "JL. PENJAJAHAN", "COFFESHOP")
p4 = usaha("SBC", 9, "JL. KASTI", "GYM")
p5 = usaha("KANTOR LOOP", 6, "JL. RAJA", "ELEKTRONIK")
p6 = usaha("MAKMUR", 5, "JL. TENIS", "KULINER")
p7 = usaha("SEJAHTERA", 6, "JL. PENJAJAHAN", "KONSULTAN PAJAK")
p8 = usaha("KERJA TULIS", 9, "JL. PEMBANGUNAN", "ATK")
p9 = usaha("AMPCOMP", 12, "JL. SUDIRMAN", "ELEKTRONIK")
p10 = usaha("AYAM LONCAT", 6, "JL. SUTOMO", "KULINER")
p1.print()
p2.print()
p3.print()
p4.print()
p5.print()
p6.print()
p7.print()
p8.print()
p9.print()
p10.print()