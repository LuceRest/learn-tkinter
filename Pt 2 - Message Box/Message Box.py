from tkinter import *
from tkinter import messagebox


root = Tk()


messagebox.showinfo('Notif informasi', 'Info geger geden')

messagebox.showerror('Notif error', 'error')

messagebox.showwarning('Notif warning', 'warning')

if messagebox.askquestion('Notif pertanyaan', 'pilih yes or no?') == 'yes':
    print('yes')

if messagebox.askokcancel('Ask ok cancel', 'pilih ok or cancel?') == 1:
    print('ok')

if messagebox.askretrycancel('Ask retry cancel', 'pilih retry or cancel?') == 1:
    print('retry')

if messagebox.askyesno('Ask yes no', 'pilih yes or no?') == 1:
    print('yes')
elif messagebox.askyesno('Ask yes no', 'pilih yes or no?') == 0:
    print('no')


root.mainloop()



'''
    NB :
        - messagebox.showinfo()		    ~> Berfungsi untuk menampilkan messagebox.
        - messagebox.showinfo("<nama window messagebox>", "<isi messagebox>")

        - messagebox.showerror()        ~> Berfungsi untuk menampilkan error messagebox.
        - messagebox.showerror("<nama window messagebox>", "<isi messagebox>")

        - messagebox.showwarning()	    ~> Berfungsi untuk menampilkan warning messagebox.
        - messagebox.showwarning("<nama window messagebox>", "<isi messagebox>")

        - messagebox.askquestion()	    ~> Berfungsi untuk menampilkan yes-no question. Akan mereturn string "yes" dan "no".
        - messagebox.askquestion("<nama window messagebox>", "<isi messagebox>")

        - messagebox.askokcancel()	    ~> Berfungsi untuk menampilkan ok-cancel question. Akan mereturn int 1 untuk tombol ok dan int 0 untuk tombol cancel.
        - messagebox.askokcancel("<nama window messagebox>", "<isi messagebox>")

        - messagebox.askretrycancel()	~> Berfungsi untuk menampilkan retry-cancel question. Akan mereturn int 1 untuk tombol retry dan int 0 untuk tombol cancel.
        - messagebox.askretrycancel("<nama window messagebox>", "<isi messagebox>")

        - messagebox.askyesno()	        ~> Berfungsi untuk menampilkan yes-no question. Akan mereturn int 1 untuk tombol yes dan int 0 untuk tombol no.
        - messagebox.askyesno("<nama window messagebox>", "<isi messagebox>")


'''

