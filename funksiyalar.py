
from database import cursor, db


def korish():
    kor = cursor.execute("SELECT * FROM sevimli_kinolar")

    for i in kor:
        print(i)


def qoshish():
    nomi = input("Kino nomi: ")
    top_kinolar = input("Top kinolarmi: ")
    janrlar = input("Janri: ")
    vaqt = input("Davomiyligi: ")
    tavsiya_etilgan = input("Tavsiya etilganmi: ")

    cursor.execute("""
    INSERT INTO sevimli_kinolar
    (nomi, top_kinolar, janrlar, vaqt, tavsiya_etilgan)
    VALUES (?, ?, ?, ?, ?)
    """, (nomi, top_kinolar, janrlar, vaqt, tavsiya_etilgan))

    db.commit()
    print("Kino qo'shildi!")


def qidirish():
    nomi = input("Kino nomini kiriting: ")

    cursor.execute(
        "SELECT * FROM sevimli_kinolar WHERE nomi LIKE ?",
        (f"%{nomi}%",)
    )

    natija = cursor.fetchall()

    if natija:
        for kino in natija:
            print(kino)
    else:
        print("Kino topilmadi!")


def ochirish():
    id = input("O'chiriladigan kino ID sini kiriting: ")

    cursor.execute(
        "DELETE FROM sevimli_kinolar WHERE id = ?",
        (id,)
    )

    db.commit()

    if cursor.rowcount > 0:
        print("Kino o'chirildi!")
    else:
        print("Bunday ID mavjud emas!")
