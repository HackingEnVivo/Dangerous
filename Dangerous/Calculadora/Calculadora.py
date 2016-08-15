from Tkinter import*
def suma():
	total=int(entrada1.get())+int(entrada2.get())
	Label(root,text=total).pack()
def resta():
	total=int(entrada1.get())-int(entrada2.get())
	Label(root,text=total).pack()
def multiplicacion():
	total=int(entrada1.get())*int(entrada2.get())
	Label(root,text=total).pack()
def division():
	total=int(entrada1.get())/int(entrada2.get())
	Label(root,text=total).pack()
root=Tk()
root.title="suma"
root.title="resta"
root.title="multiplicacion"
root.title="division"
num1=IntVar()
num2=IntVar()
entrada1=Entry(root,textvariable=num1)
entrada1.pack()
entrada2=Entry(root,textvariable=num2)
entrada2.pack()
suma=Button(root,text="Suma",command=suma)
resta=Button(root,text="Resta",command=resta)
multiplicacion=Button(root,text="Multiplicacion",command=multiplicacion)
division=Button(root,text="Division",command=division)
suma.pack()
resta.pack()
multiplicacion.pack()
division.pack()
root.mainloop()
