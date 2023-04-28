from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk



class View_menu:



    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("1285x800")
        self.screen.title("Faaiz POS")
        self.screen.configure(bg='light blue')
        self.cart={}
        self.point=0
        self.price=0
        self.totalprice=[]
        self.val=''
        self.EntryTotal = StringVar()
        self.EntryGST=StringVar()

        self.Name = StringVar()
        self.Phone = StringVar()
        self.show=0
        self.g=0.13
        self.Contact()



        self.Total_show()

        label1 = Label(self.screen, text="Faaiz POS ", relief="groove", fg="#074466", bg="Yellow",
                       font=("times in roman", 20, "bold"), pady=2).place(x=600,y=15)

        self.bg_img = ImageTk.PhotoImage(file="products/image1.png")
        self.bg_img2 = ImageTk.PhotoImage(file="products/juice.png")


    # Row 1
        self.bg_img00 = ImageTk.PhotoImage(file="products/tshirt.jpg")
        self.bg_img01 = ImageTk.PhotoImage(file="products/shirt.jpg")
        self.bg_img02 = ImageTk.PhotoImage(file="products/Pant.jpg")
        self.bg_img03 = ImageTk.PhotoImage(file="products/cap.jpg")
        self.bg_img04 = ImageTk.PhotoImage(file="products/mask.jpg")
        self.bg_img05 = ImageTk.PhotoImage(file="products/watch.jpg")
        self.bg_img06 = ImageTk.PhotoImage(file="products/shoes.jpg")

    # Row 2

        self.bg_img10 = ImageTk.PhotoImage(file="products/boy.jpg")
        self.bg_img11 = ImageTk.PhotoImage(file="products/baby.jpg")
        self.bg_img12 = ImageTk.PhotoImage(file="products/kshoes.jpg")
        self.bg_img13 = ImageTk.PhotoImage(file="products/bag.jpg")
        self.bg_img14 = ImageTk.PhotoImage(file="products/car.jpg")
        self.bg_img15 = ImageTk.PhotoImage(file="products/powder.jpg")
        self.bg_img16 = ImageTk.PhotoImage(file="products/hand wash.jpg")

    # Row 3

        self.bg_img20 = ImageTk.PhotoImage(file="products/rice.jpg")
        self.bg_img21 = ImageTk.PhotoImage(file="products/wheat.jpg")
        self.bg_img22 = ImageTk.PhotoImage(file="products/masaly.jpg")
        self.bg_img23 = ImageTk.PhotoImage(file="products/sugar.jpg")
        self.bg_img24 = ImageTk.PhotoImage(file="products/harpic.jpg")
        self.bg_img25 = ImageTk.PhotoImage(file="products/tapal.jpg")
        self.bg_img26 = ImageTk.PhotoImage(file="products/surf excel.jpg")

    # Row 4

        self.bg_img30 = ImageTk.PhotoImage(file="products/water.jpg")
        self.bg_img31 = ImageTk.PhotoImage(file="products/pepsi.jpg")
        self.bg_img32 = ImageTk.PhotoImage(file="products/nesjuice.jpg")
        self.bg_img33 = ImageTk.PhotoImage(file="products/bread.jpg")
        self.bg_img34 = ImageTk.PhotoImage(file="products/egg.jpg")
        self.bg_img35 = ImageTk.PhotoImage(file="products/jam.jpg")
        self.bg_img36 = ImageTk.PhotoImage(file="products/milk.jpg")



        buttn00 = Button(self.screen, image=self.bg_img00,command=lambda :self.demo(0,0), width=130, height=130).place(x=460, y=80)
        buttn01 = Button(self.screen, image=self.bg_img01,command=lambda :self.demo(0,1), width=130, height=130).place(x=610, y=80)
        buttn02 = Button(self.screen, image=self.bg_img02,command=lambda :self.demo(0,2), width=130, height=130).place(x=760, y=80)
        buttn03 = Button(self.screen, image=self.bg_img03,command=lambda :self.demo(0,3), width=130, height=130).place(x=910, y=80)

        buttn04 = Button(self.screen, image=self.bg_img04,command=lambda :self.demo(0,4), width=130, height=130).place(x=1060, y=80)
        buttn05 = Button(self.screen, image=self.bg_img05,command=lambda :self.demo(0,5), width=130, height=130).place(x=1210, y=80)
        buttn06 = Button(self.screen, image=self.bg_img06,command=lambda :self.demo(0,6), width=130, height=130).place(x=1360, y=80)

        buttn10 = Button(self.screen, image=self.bg_img10,command=lambda :self.demo(1,0), width=130, height=130).place(x=460, y=230)
        buttn11 = Button(self.screen, image=self.bg_img11,command=lambda :self.demo(1,1), width=130, height=130).place(x=610, y=230)
        buttn12 = Button(self.screen, image=self.bg_img12,command=lambda :self.demo(1,2), width=130, height=130).place(x=760, y=230)
        buttn13 = Button(self.screen, image=self.bg_img13,command=lambda :self.demo(1,3), width=130, height=130).place(x=910, y=230)

        buttn14 = Button(self.screen, image=self.bg_img14,command=lambda :self.demo(1,4), width=130, height=130).place(x=1060, y=230)
        buttn15 = Button(self.screen, image=self.bg_img15,command=lambda :self.demo(1,5), width=130, height=130).place(x=1210, y=230)
        buttn16 = Button(self.screen, image=self.bg_img16,command=lambda :self.demo(1,6), width=130, height=130).place(x=1360, y=230)

        buttn20 = Button(self.screen, image=self.bg_img20,command=lambda :self.demo(2,0), width=130, height=130).place(x=460, y=380)
        buttn21 = Button(self.screen, image=self.bg_img21,command=lambda :self.demo(2,1), width=130, height=130).place(x=610, y=380)
        buttn22 = Button(self.screen, image=self.bg_img22,command=lambda :self.demo(2,2), width=130, height=130).place(x=760, y=380)
        buttn23 = Button(self.screen, image=self.bg_img23,command=lambda :self.demo(2,3), width=130, height=130).place(x=910, y=380)

        buttn24 = Button(self.screen, image=self.bg_img24,command=lambda :self.demo(2,4), width=130, height=130).place(x=1060, y=380)
        buttn25 = Button(self.screen, image=self.bg_img25,command=lambda :self.demo(2,5), width=130, height=130).place(x=1210, y=380)
        buttn26 = Button(self.screen, image=self.bg_img26,command=lambda :self.demo(2,6), width=130, height=130).place(x=1360, y=380)

        buttn30 = Button(self.screen, image=self.bg_img30,command=lambda :self.demo(3,0), width=130, height=130).place(x=460, y=530)
        buttn31 = Button(self.screen, image=self.bg_img31,command=lambda :self.demo(3,1), width=130, height=130).place(x=610, y=530)
        buttn32 = Button(self.screen, image=self.bg_img32,command=lambda :self.demo(3,2), width=130, height=130).place(x=760, y=530)
        buttn33 = Button(self.screen, image=self.bg_img33,command=lambda :self.demo(3,3), width=130, height=130).place(x=910, y=530)

        buttn34 = Button(self.screen, image=self.bg_img34,command=lambda :self.demo(3,4), width=130, height=130).place(x=1060, y=530)
        buttn35 = Button(self.screen, image=self.bg_img35,command=lambda :self.demo(3,5), width=130, height=130).place(x=1210, y=530)
        buttn36 = Button(self.screen, image=self.bg_img36,command=lambda :self.demo(3,6), width=130, height=130).place(x=1360, y=530)

        buttndel = Button(self.screen, text="Delete",bg="white",command=lambda :self.Delete(),width=10, height=1).place(x=590, y=700)
        buttncle = Button(self.screen, text="Clear",command=lambda :self.Clear(), bg="white", width=10, height=1).place(x=790, y=700)
        buttntot = Button(self.screen, text="Total",command=lambda :self.Total_Price(), bg="white", width=10, height=1).place(x=990, y=700)
        # buttngen = Button(self.screen, text="Generate", bg="orange", width=10, height=1).place(x=1190,y=700)

        column=(1, 2,3)
        self.tv = ttk.Treeview(self.screen, columns=column, show='headings', height=23)
        self.tv.heading("1", text="Items")
        self.tv.heading("2", text="QTY")
        self.tv.heading("3", text="Price")
        self.tv.column("1", width=220)
        self.tv.column("2", width=80, anchor=CENTER)
        self.tv.column("3", width=140, anchor=CENTER)
        self.tv.place(x=12, y=130)

    def demo(self,i,t):

        n = [["TShirt", "Shirt","Pant","Cap","Mask","Watch","Shoes"],
             ["Baby Suit", "Frock","Baby Shoes","Bag","Toy","Powder","Hand Wash"],
             ["Rice", "Wheat","Spices","Sugar","Harpic","Tapal","Surf Excel"],
             ["Water", "Pepsi","Juice","Bread","Egg","Jam","Milk"]]
        p = [[1000, 1600,2000,100,60,3000,1900],
             [500, 600,1200,1000,600,300,800],
             [150, 80,200,100,200,300,400],
             [50, 60,200,100,160,300,120]]

        self.val=(n[i][t])
        pr=p[i][t]

        if self.val not in self.cart:
            self.cart[self.val]=[pr]
            self.point=1
            self.price=pr
        else:

            self.cart[self.val].append(pr)
            cal=self.cart[self.val]
            self.point=len(cal)
            self.price=sum(cal)


        self.tv.insert('', i, values=(self.val, self.point, self.price))



    def Clear(self):
        x=self.tv.get_children()
        if x!="":
            for cl in x:
                self.tv.delete(cl)
        self.cart.clear()

    def Delete(self):
        t=self.tv.selection()
        for_del_itdic=(self.tv.item(t))
        del_it=for_del_itdic['values'][0]
        self.tv.delete(t)
        del self.cart[del_it]
        print(del_it)

        #selected_item = self.tv.selection()
        # selected_item = self.tv.selection_remove(items)
        # self.tv.delete(selected_item)
        #del self.cart[self.val]


    def Total_Price(self):

        sh=[]
        for_add_val = self.cart.values()
        for ad in for_add_val:
            self.totalprice.append(sum(ad))
        self.show=sum(self.totalprice)
        tg=self.show*self.g
        totalwithgst=tg+self.show
        self.EntryGST.set(totalwithgst)
        self.EntryTotal.set(self.show)

        self.n = self.Name.get()
        self.p = self.Phone.get()
        print(self.n, self.p)

    def Contact(self):
        labelName = Label(self.screen, text="Customer Name", relief="groove", fg="#074466",
                       font=("times in roman", 12, "bold"), pady=2).place(x=12,y=60)
        labelPhone = Label(self.screen, text="Contact No.", relief="groove", fg="#074466",
                          font=("times in roman", 12, "bold"), pady=2).place(x=12, y=92)

        EntryName = Entry(self.screen, relief="groove", textvariable=self.Name,width=25, font=("", "14")).place(x=150,y=60)
        EntryPhone = Entry(self.screen, relief="groove",textvariable=self.Phone, width=25, font=("", "14")).place(x=150, y=92)







        # a=["Pizza1","Pizza2"]
        # b=[1,1]
        # c=[200,500]
        # for i in range(2):
        #     tv.insert('',i,values=(a[i],b[i],c[i]))

    def Total_show(self):
        labelTotal = Label(self.screen, text="Total Price", relief="groove", fg="#074466",
                              font=("times in roman", 12, "bold"), pady=2).place(x=12, y=650)
        labelGST = Label(self.screen, text="With GST", relief="groove", fg="#074466",
                               font=("times in roman", 12, "bold"), pady=2).place(x=12, y=690)

        EntryTotal = Entry(self.screen, relief="groove",textvariable=self.EntryTotal, width=25, font=("", "14")).place(x=150, y=650)
        EntryGST = Entry(self.screen, relief="groove",textvariable=self.EntryGST, width=25, font=("", "14")).place(x=150, y=690)




font_color = "#074466"
screen = Tk()

obj1 = View_menu(screen)
screen.mainloop()
