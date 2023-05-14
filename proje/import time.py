import time

class DepremFormu:
    def init(self,ad,soyad,tc,tel_no,ihtiyac):
        self.ad=ad
        self.soyad=soyad 
        self.tc=tc 
        self.tel_no=tel_no 
        self.ihtiyac=ihtiyac
    def bilgileri_al(self): 
        self.ad = input("Adınızı girin: ")
        self.soyad = input("Soyadınızı girin: ")  
        while True:
            try:
                self.tc = input("TC Kimlik Numaranızı girin: ")
                if len(self.tc) != 11:
                    raise ValueError("TC Kimlik numarası 11 haneli olmalıdır.")
                break
            except ValueError as e:
                print(e)
        
        while True:
            try:
                self.tel_no = input("Telefon Numaranızı girin: ")
                if len(self.tel_no) != 10:
                    raise ValueError("Telefon numarası başında 0 olmadan 10 haneli olmalıdır.")
                break
            except ValueError as a:
                print(a)
        self.ihtiyac = ""

    def beslenme(self):
      print("Talebiniz alınmıştır, tek kişilik beslenme kolisi için yardımsever bilgileri telefonunuza SMS olarak gönderilmiştir.")
      print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
    def barinma_secimi(self):
        print("Lütfen aşağıdaki barınma seçeneklerinden birini seçin:")
        print("1- Çadır")
        print("2- Konteyner")
        print("3- Otel")
        print("4- Yurt")
        print("5- Öğretmen ve Polis Konuk Evleri")
        print("6- Aile Yanı")
        barinma_talep = input("Hangi barınma seçeneğini tercih edersiniz? (1-6): ")
        print("Barınma talebiniz alınmıştır.")
        print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
        return barinma_talep

    def giyecek(self):
        print("Lütfen yazlık-kışlık seçeneklerinden birisini seçiniz.")
        print("1-yazlık")
        print("2-kışlık")
        mevsim = input("Yazlık için: 1, kışlık için: 2 giriniz: ")
        print("Lütfen aşağıdaki seçeneklerden birini seçiniz.")
        if mevsim == "1":
            print("1-Kız Bebek")
            print("2-Erkek Bebek")
            print("3-Kız Çocuk")
            print("4-Erkek Çocuk")
            print("5-Yetişkin Erkek")
            print("6-Yetişkin Kadın")
            y_bölüm = input("Lütfen yukarıdaki seçeneklerden birini seçiniz: ")
            if y_bölüm == "1":
                print("Yazlık kız bebek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            elif y_bölüm == "2":
                print("Yazlık erkek bebek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            elif y_bölüm == "3":
                print("Yazlık kız çocuk kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            elif y_bölüm == "4":
                print("Yazlık erkek çocuk kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            elif y_bölüm == "5":
                print("Yazlık erkek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            elif y_bölüm == "6":
                print("Yazlık kadın kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
            else:
                print("Hatalı giriş yaptınız, program sonlandırılıyor.")

        elif mevsim == "2":
            print("1-Kız Bebek")
            print("2-Erkek Bebek")
            print("3-Kız Çocuk")
            print("4-Erkek Çocuk")
            print("5-Yetişkin Erkek")
            print("6-Yetişkin Kadın")
            k_bölüm = input("Lütfen yukarıdaki seçeneklerden birini seçiniz: ")
            if k_bölüm == "1":
                print("Kışlık kız bebek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            elif k_bölüm == "2":
                print("Kışlık erkek bebek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            elif k_bölüm == "3":
                print("Kışlık kız çocuk kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            elif k_bölüm == "4":
                print("Kışlık erkek çocuk kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            elif k_bölüm == "5":
                print("Kışlık erkek kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            elif k_bölüm == "6":
                print("Kışlık kadın kıyafeti için yardımsever bilgileri SMS olarak telefonunuza gönderilmiştir.")
            else:
                print("Hatalı giriş yaptınız, program sonlandırılıyor.")
        
    def hijyen_malzemeleri(self):
        print("Lütfen aşağıdaki hijyen seçeneklerinden birini seçin:")
        print("1- Kadın Hijyen Malzemeleri İhtiyaç Kolisi")
        print("2- Erkek Hijyen Malzemeleri İhtiyaç Kolisi")
        print("3- Temel Hijyen Malzemeleri İhtiyaç Kolisi")
        hijyen_talep = input("Hangi hijyen seçeneğini tercih edersiniz? (1-3): ")
        print("Hijyen Malzemeleri İhtiyaç Kolisi talebiniz alınmıştır.")
        print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
    def bebek_malzemeleri(self):
        secim = input("Lütfen aşağıdaki bebek malzemeleri seçeneklerinden birini seçin:\n1- Beslenme\n2- Barınma\n3- Hijyen\nSeçiminiz: ")
        if secim == "1":
            print("Bebek beslenme malzemelerini seçtiniz, yardımseverin bilgileri telefonunuza SMS olarak gönderilmiştir.")
            print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
        elif secim == "2":
            print("Bebek barınma malzemelerini seçtiniz, yardımseverin bilgileri telefonunuza SMS olarak gönderilmiştir.")
            print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
        elif secim == "3":
            print("Bebek hijyen ürünlerini seçtiniz, yardımsever bilgileri SMS olarak gönderilmiştir.")
            print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
        else:
            print("Hatalı giriş yaptınız, program sonlandırılıyor.")

    def psikolojik_yardim(self):
        print("Psikolojik yardım kategorisini seçtiniz. Lütfen bekleyiniz... ")
        time.sleep(1)
        psikolog_talep = input("Sizi bir psikologla eşleştiriyoruz. Onaylıyor musunuz? (evet/hayır): ")
        while True:
            if psikolog_talep == "evet":
                print("Psikoloğun bilgileri telefonunuza SMS olarak gönderilmiştir.")
                print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
                break
            elif psikolog_talep == "hayır":
                print("Uygulama sonlandırılıyor...")
                break
            else:
                print("Geçersiz işlem! Uygulama sonlandırılıyor...")
            break

    def iletisim(self):
        print("Lütfen aşağıdaki iletişim seçeneklerinden birini seçin:")
        print("1- AFAD")
        print("2- AHBAP")
        print("3- ACİL ÇAĞRI MERKEZİ")
        iletisim_talep = input("Hangi iletişim seçeneğine ulaşmak istiyorsunuz? (1-3): ")
        time.sleep(1)
        print("İletişim bilgileri sms olarak gönderilmiştir. Lütfen mesajlarınızı kontrol ediniz.")
        print("Çıkmak istiyorsanız n tuşuna basarak uygulamayı sonlandırabilirsiniz. ")
    def form_bilgilerini_goster(self):
        print("Ad Soyad:", self.ad, self.soyad)
        print("TC Kimlik Numarası:", self.tc)
        print("Telefon Numarası:", self.tel_no)
        

form = DepremFormu()
form.bilgileri_al()

print("""
"(İhtiyaç Başlıkları:")
    ("1- Beslenme")
    ("2- Barınma ")
    ("3- Giyecek")
    ("4- Hijyen Malzemeleri")
    ("5- Bebek Malzemeleri")
    ("6- Psikolojik Destek")
    ("7- İletişim (AFAD, AHBAP, vb.")
    ("n tuşuna basarak uygulamayı sonlandırabilirsin.")
""")

while True:

  islem = input("Hangi ihtiyacınız var? (1-7 arasında bir sayı girin): ")

  if (islem == "n"):
    print("Uygulama Sonlandırıldı..")
    break
  
  elif (islem == "1"):
    form.beslenme()
    print("*****************")
    print("İhtiyaç: beslenme")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "2"):
    form.barinma_secimi()
    print("*****************")
    print("İhtiyaç: barınma ")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "3"):
    form.giyecek()
    print("*****************")
    print("İhtiyaç: giyecek ")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "4"):
    form.hijyen_malzemeleri()
    print("*****************")
    print("İhtiyaç: hijyen malzemeleri ")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "5"):
    form.bebek_malzemeleri()
    print("*****************")
    print("İhtiyaç: bebek malzemeleri ")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "6"):
    form.psikolojik_yardim()
    print("*****************")
    print("İhtiyaç: psikolojik yardım ")
    print("*****************")
    form.form_bilgilerini_goster()
  elif (islem == "7"):
    form.iletisim()
    print("*****************")
    print("İhtiyaç: iletişim ")
    print("*****************")
    form.form_bilgilerini_goster()