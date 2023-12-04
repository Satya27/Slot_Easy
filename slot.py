import os
import random
os.system('cls')

saldo = 100000
print(10*'---')
print("-----GAME SLOT 777-----")
print("""
Angka yang keluar akan dikalikan
dengan jumlah deposit anda, semakin besar
DPnya semakin besar dapatnya.
jika angka 'ganjil' maka hangus !!.
SELAMAT BERJUDI..!
""")

jebakan = 3

while True:
    print(10*'---')
    print('[{0}] Saldo Anda : {1}'.format(jebakan, saldo))
    print(10*'---')
    dp = int(input("Masukan DP : "))
    print(10*'---')
    print('Total Saldo Akhir : ', saldo-dp)
    print(10*'---')
    input("Enter untuk mulai judi angka..!!")
    print(10*'---')

    if jebakan <= 0:
        lsx = [1, 3, 5, 7, 9]
        x = random.choice(lsx)
        jebakan = 3
    else:
        lsx = [2, 4, 6, 8]
        x = random.choice(lsx)

    if x % 2 == 0:
        rp_bonus = dp*x
        saldo = saldo-dp+rp_bonus
        print("WIN !!! Angka yang keluar [", x, "] x DP [", dp, "] : ", dp*x)
        print(10*'---')
    else:
        rp_bonus = 0
        saldo = saldo-dp+rp_bonus
        print("ZOONG !!! Angka yang keluar Ganjil [", x, "]")
        print(10*'---')

    print('Saldo Akhir : ', saldo)
    print(10*'---')

    jebakan -= 1

    if saldo >= 1000:
        n = input("Apakah anda ingin lanjut [y/n]:")
        os.system('cls')
        if n == "n":
            break
    else:
        n = input("Saldo anda tidak cukup, silahkan isi DP anda")
        break
