def AddItem():
    if  ITEMCODE.get() == "" or ITEMNAME.get() == "" or STATUS.get() == "" or ITEMPRICE.get() == "" or ITEMQUANTITY.get() == "" or STOCKARRIVALDATE.get() == "" or MINIMUMORDER.get() == "" or MAXIMUMORDER.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (itemcode, lastname, status, itemprice, itemquantity, stockarrivaldate, minimumorder, maximumorder) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (str(ITEMCODE.get()), str(LASTNAME.get()), str(STATUS.get()), str(ITEMPRICE.get()), str(ITEMQUANTITY.get()), str(STOCKARRIVALDATE.get()), str(MINIMUMORDER.get()), str(MAXIMUMORDER.get())))
        tree.delete(*tree.get_children())
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
        conn.commit()
        ITEMCODE.set("")
        LASTNAME.set("")
        STATUS.set("")
        ITEMPRICE.set("")
        ITEMQUANTITY.set("")
        STOCKARRIVALDATE.set("")
        MINIMUMORDER.set("")
        MAXIMUMORDER.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Item has been added!", fg="green")
