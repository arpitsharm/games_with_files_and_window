from tkinter import *

with open("file/geo.txt", 'r') as f:
    r_g = f.read()


# with open('file/title.txt', 'w') as f:
#     a = input("Enter Title of Window :-")
#     f.write(a)

with open("file/title.txt", 'r') as f:
    r_t = f.read()

root = Tk()
root.title(r_t)
root.geometry(r_g)

with open('file/truef') as f:
    r = f.read().lower().strip() # TRUE - true


litewatelabel = Label(root, text="")
litewatelabel.pack()

if r == 'true':
    litewatelabel.config(text="Yes You Can Do It")

elif r == 'false':
    litewatelabel.config(text="Sorry Try Again")

else:
    litewatelabel.config(text="I will Anger")




root.mainloop()