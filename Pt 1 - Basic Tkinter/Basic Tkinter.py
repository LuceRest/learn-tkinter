from tkinter import *
from tkinter import font

root = Tk()
root.config(background="light blue")

label = Label(text="Label1", font="Normal 30", background='Light blue')
label.grid(row=0, column=0, columnspan=2)

data = Entry(font="Normal 30", bd=10)
data.grid(row=1, column=0)

def perintah():
    print(data.get())
    data.delete(0, END)

btn = Button(text="Tekan", font="Normal 30", activebackground="blue", command=perintah)
btn.grid(row=1, column=1)

teks = Text(width=50, height=10, bd=10, font="Normal 30")
teks.grid(row=2, column=0, columnspan=2)


root.mainloop()



'''
    NB :
        - Tk().config(background="<warna>")	
            ~> Berfungsi untuk mengubah warna background.

        - <variabel label> = Label(text="<isi teks>", font="<style font> <ukuran font>, background="<warna>")
            ~> Berfungsi untuk membuat label.

        - .pack()	~> Berfungsi untuk menaruh label pada window.
        - <variabel label>.pack()

        - .grid()	~> Berfungsi untuk menaruh label pada window dengan menggunakan grid system.
        - <variabel label>.grid(row=<letak baris [int]>, column=<letak kolom [int]>, columnspan=<kolom yg ingin digabung>)
            - columnspan	-> Menggabungkan beberapa kolom.

        - Entry()	~> Berfungsi untuk menginputkan suatu data dalam satu baris.
        - <variabel entry> = Entry(font="<style font> <ukuran font", bd=<nilai border>)
            - bd	-> Border.

        - Button()	~> Berfungsi untuk membuat suatu button.
        - <variabel button> = Button(text="<isi teks>", font="<style font> <ukuran font>", activebackground="<warna>", command=<nama fungsi>)
            - activebackground	-> Efek background ketika diklik.
            - command		    -> Fungsi yg akan dijalankan ketika tombol diklik.

        - .get()	~> Berfungsi untuk mengambil nilai dari suatu input Entry().
        - <variabel entry>.get()

        - Text()	~> Berfungsi untuk menginputkan suatu teks.
        - <variabel teks> = Text(width=<lebar teks>, height=<tinggi teks>, bd=<border>, font="<style font> <ukuran font>")


'''

