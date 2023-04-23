# # from  tkinter import *
# #
# # def knopka(event):
# #     lab["text"] = message
# # root = Tk()
# # root.geometry("400x500")
# #
# # lab = Label(root,text="...")
# # lab.pack()
# #
# # ent = Entry(root)
# # ent.bind("<Button-3>", knopka)
# # ent
# # ent.pack()
# #
# # root.mainloop()
#
# from tkinter import *
#
# def h_i(event):
#     user_choose = rb_val.get()
#     if user_
#
#     root = Tk()
#
# lab = Label(root, text="hi")
# lab.pack()
#
# rb_val = IntVar()
#
# rb1 = Radiobutton(root, text="world", variabie=rb_val, value=1)
# rb1.pack()
#
# rb2 = Radiobutton(root, text="Python")
def activation():
    if cb_val.get() == True:
    b["text"] = "активна"
    b["state"] = "normal"
    else:
    b["text"]
win = Tk()

cb = Checkbutton(win, text="активатор", variable=cb_val, onvalue=True, offvalue=False)

cb.pack()

b = Button(win, text="не акив", state= "disabled")
b.pack()
win.mainloop()