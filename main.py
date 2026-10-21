kutubxona = {}
ishora = True

while ishora:
    kitob = input("Kitob nomini kiriting: ")
    muallif = input(f"'{kitob}' kitobining muallifini kiriting: ")
    kutubxona[kitob] = muallif

    javob = input("Yana kitob qo'shasizmi? (ha/yo'q): ")
    if javob.lower() == "yo'q" or javob.lower() == 'yoq':
        ishora = False

print("\nKutubxonadagi kitoblar ro'yxati:")
for kitob, muallif in kutubxona.items():
    print(f"'{kitob}' - Muallif: {muallif}")

mehmonlar = []
ishora = True

while ishora:
    ism = input("Mehmon ismini kiriting (to'xtatish uchun 'stop' deb yozing): ")
    if ism.lower() == 'stop':
        ishora = False
    else:
        mehmonlar.append(ism.title())

print("\nSizning mehmonlar ro'yxatingiz:")
for mehmon in mehmonlar:
    print(mehmon)

vazifalar = []
ishlamoqda = True

while ishlamoqda:
    vazifa = input("Bugungi vazifani kiriting (to'xtatish uchun 'tugatish' deb yozing): ")
    if vazifa.lower() == 'tugatish':
        ishlamoqda = False
    else:
        vazifalar.append(vazifa)

print("\nSizning bugungi vazifalaringiz ro'yxati:")
for tartib, ish in enumerate(vazifalar, 1):
    print(f"{tartib}. {ish}")

jurnal = {}
ishlamoqda = True

while ishlamoqda:
    talaba = input("Talabaning ismini kiriting: ")
    baho = input(f"{talaba}ning bahosini kiriting: ")

    jurnal[talaba] = baho

    javob = input("Yana talaba qo'shasizmi? (ha/yo'q): ")
    if javob.lower() == "yo'q" or javob.lower() == 'yoq':
        ishlamoqda = False

print("\nTalabalarning yakuniy baholari jurnali:")
for talaba, baho in jurnal.items():
    print(f"Talaba: {talaba} | Bahosi: {baho}")
