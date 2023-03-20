def calculate(number):   
    def binary_hesaplama(sıfırbirler):
        sonuc = []
        üs = -1
        for sıfırbir in sıfırbirler:
            üs += 1
            if sıfırbir == 1:
                deger = 2**üs
                sonuc.append(deger)
        return sonuc

    binary_rakam_listesi = []

    binary = number

    for rakam in binary:
        binary_rakam_listesi.append(int(rakam))

    binary_rakam_listesi.reverse()

    return sum(binary_hesaplama(binary_rakam_listesi))