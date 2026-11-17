from funksiyalar import qidirish,qoshish,korish,ochirish

while True:


    print("------- MENYU --------")
    print("1. qidirish")    
    print("2. qo'shish")
    print("3. korish")
    print("4. o'chirish")
    print("0. chiqish")
    print("----------------------")

    tanla = int(input("menyudan kerakli sonini yozing: "))

    if tanla == 0:
        print("dastur tugadi!")
        break
    elif tanla == 1:
        qidirish()
    elif tanla == 2:
        qoshish()
        print("qoshish")
    elif tanla == 3:
        korish()
    elif tanla == 4:
        ochirish()
    else:
        print("bunday buyruq mavjud emas!")