import mysql.connector
from mysql.connector import connect

def admin_consol():
    user_input = input("Welcome administrator.\nPlease input 1 if you would like to input and execute an SQL script."
    "\nPlease input 2 if you would like to provide the program with an sql file path for execution.")

    if user_input == '1':
        query = input("Please type in your query: ")
        cur.execute(query)
        print("\nThe requested query is:")
        for i in cur:
            print(i)
    if user_input == '2':
        file_name = input("Please input the path of your SQL query file now:")
        file = open(file_name, "r")
        tester = file.read()
        cur.execute(tester)
        print(f"\nThe inputted query is: {tester}")
        print("\nThe requested query is:")
        for i in cur:
            print(i)
  
def guest_view(cur):
    print("What information are you looking for?")
    print("1 - Art Object Information")
    print("2 - Exhibition Information")
    print("3 - Collection Information")
    print("4 - Artist Information")
    print("5 - Quit Program")

    selection = input()
    if selection == '1':
        table_list = ['Art_Object', 'Painting', 'Sculpture', 'Other']
        for x in table_list:
            print(x)
        user_table_name = input("These are the available tables. Which table would you like to select?")
        table_info(cur, user_table_name)
    elif selection == '2':
        user_table_name = 'Exhibitions'
        print(user_table_name)
        table_info(cur, user_table_name)
    elif selection == '3':
        table_list = ['Collections', 'Permanent_collection', 'Borrowed']
        for x in table_list:
            print(x)
        user_table_name = input("These are the available tables. Which table would you like to select?")
        table_info(cur, user_table_name)
    elif selection == '4':
        user_table_name = 'Artist'
        print(user_table_name)
        table_info(cur, user_table_name)
    elif selection == '5':
        print("Thank you for using this application.")
        return

def table_info(cur, table_name):
    selection = input(f"Would you like to see all entries for {table_name} in the database or specify a condition? (Enter A or C) ")
    if selection == 'A':
        cur.execute(f'SELECT * FROM {table_name}')
        for x in cur:
            print(x)
    if selection == 'C':
        cur.execute(f"DESCRIBE {table_name}")
        for x in cur:
            print(x)
        user_attribute = input("Please enter desired attribute for search: ")
        user_attribute2 = input("Please enter attribute for WHERE condition: ")
        user_attributetype = input("Please enter conditional attribute type (char, varchar, int, date, decimal): ")
        user_operator = input("Please enter operator for condition (=, <>): ")

        if user_attributetype == 'char' or user_attributetype == 'varchar':
            user_value = input('What is the value being used for the condition?')
            cur.execute(f'SELECT {user_attribute} FROM {table_name} WHERE {user_attribute2}{user_operator}"{user_value}"')
            for x in cur:
                print(x)
        elif user_attributetype == 'int':
            user_value = int(input('What is the value being used in the condition?'))
            cur.execute(f'SELECT {user_attribute} FROM {table_name} WHERE {user_attribute2}{user_operator}{user_value}')
            for x in cur:
                print(x)
        elif user_attributetype == 'decimal':
            user_value = float(input('What is the value being used in the condition?'))
            cur.execute(f'SELECT {user_attribute} FROM {table_name} WHERE {user_attribute2}{user_operator}{user_value}')
            for x in cur:
                print(x)
        elif user_attributetype == 'date':
            user_value = input('What is the value being used for the condition? (YYYY-MM-DD)')
            cur.execute(f'SELECT {user_attribute} FROM {table_name} WHERE {user_attribute2}{user_operator}"{user_value}"')
            for x in cur:
                print(x)

def data_entry():
    print("OPTIONS:\n1. Insert\n2. Update\n3. Delete")
    select = input("Select 1 for insert, select 2 for update, or select 3 for delete: ")
    
    if select == '1':
        print("\nList of table names:\na. Artist\nb.Exhibitions\nc. Art_object\nd. Permanent_collection\ne. Collections\nf. Borrowed\ng. Painting\nh. Sculpture\ni. Other\n")
        table_name = input("Which table would you like to insert data to? ")
        
        while table_name not in ['Artist','Exhibitions','Art_object','Permanent_collection', 'Collections', 'Borrowed', 'Painting', 'Sculpture', 'Other']:
            print("Invalid table name.")
            table_name = input("Which table would you like to insert data to? ")

        if table_name == "Artist":
            AName = input("Please enter the name of the artist(cannot be null): ")
            DateBorn = input("Please enter the birth date of the artist in the form yyyy-mm-dd: ")
            Date_died = input("Please enter the death date of the artist in the form yyyy-mm-dd (if still alive, type null): ")
            Country_of_origin = input("Please enter the artist's country of origin: ")
            Epoch = input("Please enter the artist's epoch: ")
            Main_style = input("Please enter the artist's main style: ")
            Description = input("Please enter a short description of the artist(under 150 words): ")
            insert = ("insert into Artist values(%s, %s, %s, %s, %s, %s, %s);")
            data = (AName, DateBorn, Date_died, Country_of_origin, Epoch, Main_style, Description)

        elif table_name == 'Exhibitions':
            EName = input("Please enter the name of the exhibition(cannot be null): ")
            Start_date = input("Please enter the start date of the exhibition in the form yyyy-mm-dd: ")
            End_date = input("Please enter the end date of the exhibition in the form yyyy-mm-dd: ")
            insert = ("insert into Exhibitions values(%s, %s, %s);")
            data = (EName, Start_date, End_date)

        elif table_name == 'Art_object':
            Id_no = input("Please enter the Id number of the art object(cannot be null): ")
            Year_ = input("Please enter the year that the art object was created: ")
            Title = input("Please enter the title of the art object(cannot be null therefore type 'Untitled' if necessary): ")
            Origin = input("Please enter the origin of the art object: ")
            Epoch = input("Please enter the art object's epoch: ")
            Artist = input("Please enter the name of the artist of the art object(cannot be null therefore type 'Unknown' if necessary): ")
            Exhibition = input("Please enter the name of the exhibition that this art object is featured in (if applicable): ")
            insert = ("insert into Art_object values(%s, %s, %s, %s, %s, %s, %s);")
            data = (Id_no, Year_, Title, Origin, Epoch, Artist, Exhibition)

        elif table_name == 'Permanent_collection':
            Id_no = input("Please enter the Id number of the art object(cannot be null): ")
            Date_acquired = input("Please enter the date that this art object was acquired in the form yyyy-mm-dd: ")
            Status_ = input("Please enter the status of this object (on display, stored, or on loan): ")
            Cost = input("Please enter the cost of this object to two decimal places: ")
            insert = ("insert into Permanent_collection values(%s, %s, %s, %s);")
            data = (Id_no, Date_acquired, Status_, Cost)

        elif table_name == 'Collections':
            CName = input("Please enter the name of the collection(cannot be null): ")
            Type_ = input("Please enter the type of the collection: ")
            Description_ = input("Please enter a short description of the collection (under 200 words): ")
            Address = input("Please enter the address of where the collection is stored: ")
            Phone = input("Please enter the phone number of who is in posession of the collection: ")
            Contact_person = input("Please enter the name of the contact person: ")
            insert = ("insert into Collections values(%s, %s, %s, %s, %s, %s);")
            data = (CName, Type_, Description_, Address, Phone, Contact_person)

        elif table_name == 'Borrowed':
            Id_no = input("Please enter the Id number of the borrowed art object(cannot be null): ")
            Date_borrowed = input("Please enter the date that this art object was borrowed in the form yyyy-mm-dd: ")
            Date_returned = input("Please enter the date that this art object was returned, if applicable, in the form yyyy-mm-dd: ")
            Collection = input("Please enter the name of the collection that this art object was borrowed from: ")
            insert = ("insert into Borrowed values(%s, %s, %s, %s);")
            data = (Id_no, Date_borrowed, Date_returned, Collection)

        elif table_name == 'Painting':
            Id_no = input("Please enter the Id number of the painting (cannot be null): ")
            Paint_type = input("Please enter the paint type: ")
            Drawn_on = input("Please enter the material that the painting was drawn on: ")
            Style = input("Please enter the style of the painting: ")
            insert = ("insert into Painting values(%s, %s, %s, %s);")
            data = (Id_no, Paint_type, Drawn_on, Style)

        elif table_name == 'Sculpture':
            Id_no = input("Please enter the Id number of the sculpture (cannot be null): ")
            Material = input("Please enter the sculpture's material: ")
            Height = input("Please enter the sculpture's height in cm: ")
            Weight = input("Please enter the sculpture's weight in kg: ")
            Style = input("Please enter the sculpture's style: ")
            insert = ("insert into Sculpture values(%s, %s, %s, %s, %s);")
            data = (Id_no, Material, Height, Weight, Style)

        elif table_name == 'Other':
            Id_no = input("Please enter the Id number of the art object (cannot be null): ")
            Type_ = input("Please enter the type of the art object: ")
            Style = input("Please enter the art object's style: ")
            insert = ("insert into Other values(%s, %s, %s);")
            data = (Id_no, Type_, Style)
        
        cur.execute(insert, data)
        cnx.commit()
        cur.execute("select * from {}".format(table_name))
        print("You have successfully inserted an entry into the table:\n")
        for i in cur:
            print(i)
        print()

    elif select == '2':
        print("\nList of table names: artist, exhibitions, art_object, permanent_collection, collections, borrowed, painting, sculpture, other\n")
        table_name = input("Which table would you like to update? ")
        
        if table_name == "artist":
            print("\nList of attributes: AName, DateBorn, Date_died, Country_of_origin, Epoch, Main_style, Description_\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            artist = input("Which artist would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE AName = '{artist}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()
            
        elif table_name == "exhibitions":
            print("\nList of attributes: EName, Start_date, End_date\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            exhib = input("Which exhibition name would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE EName = '{exhib}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()
            
        elif table_name == "art_object":
            print("\nList of attributes: ID_no, Year_, Title, Origin, Epoch, Artist, Exhibition\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()
            
        elif table_name == "permanent_collection":
            print("\nList of attributes: ID_no, Date_acquired, Status_, Cost\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()
            
        elif table_name == "collections":
            print("\nList of attributes: CName, Type_, Description_, Address, Phone, Contact_person\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            cname = input("Which collection would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE CName = '{cname}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()

        elif table_name == "borrowed":
            print("\nList of attributes: ID_no, Date_Borrowed, Date_returned, Collection\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()

        elif table_name == "painting":
            print("\nList of attributes: ID_no, Paint_type, Drawn_on, Style\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()
        
        elif table_name == "sculpture":
            print("\nList of attributes: ID_no, Material, Height, Weight, Style\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()

        elif table_name == "other":
            print("\nList of attributes: ID_no, Type, Style\n")
            cur.execute("select * from {}".format(table_name))
            for i in cur:
              print(i)
            print()
            att = input("Please enter the attribute you would like to update (cannot be null): ")
            IDno = input("Which ID Number would you like to update: ")
            change = input("What would you like to update this to?: ")
            sql = f"UPDATE {table_name} SET {att} = '{change}' WHERE ID_no = '{IDno}'"
            cur.execute(sql)
            cnx.commit()
            cur.execute("select * from {}".format(table_name))
            print("Update successful!\n")
            for i in cur:
              print(i)
            print()

        else:
            print("Invalid table name.")
      
    elif select == '3':
        print("The following is a list of all current tables:")

        query = ("SHOW TABLES")
        cur.execute(query)
        tables = []
        for i in cur:
            proper = str(i)[2:-3]
            print(proper)
            tables.append(proper)
                
        table_name = input("\nWhich table would you like to delete data from?")

        while (1):
            if table_name not in tables:
                table_name = input("Unfortunately the provided input is invalid. Please retry providing a valid input from the provided list of tables now:")
            else:
                break

        print("The following information is the names of all columns within the chosen table of data available to query.\n")
        teams = []
        query = (f"SHOW COLUMNS FROM {table_name}")
        cur.execute(query)
        for i in cur:
            teams.append(str(i[0]))
        for i in teams:
            print(i)
        
        column = input("\nWhich column would you like to delete data from?")

        while (1):
            if column not in teams:
                column = input("Unfortunately the provided input is invalid. Please retry providing a valid input from the provided list of columns now:")
            else:
                break
        
        print("The following is a list of all data in the selected table and column:")
        datas = []
        query = (f'SELECT {column} FROM {table_name}')
        cur.execute(query)
        for i in cur:
            datas.append(str(i[0]))
        for i in datas:
            print(i)

        datatodelete = str(input("Please select the data you would like to remove:"))
        while (1):
            if datatodelete not in datas:
                datatodelete = input("Unfortunately the provided input is invalid. Please retry providing a valid input from the provided list of data now:")
            else:
                break

        query = (f'USE ARTMUSEUM;DELETE FROM {table_name} WHERE {column} = "{datatodelete}"')
        cur.execute(query)
        print("Data successfully deleted. Thank you for using the program.")

if __name__ == '__main__':
    print("Welcome to the Arts Museum Database")
    print("In order to proceed please select your role from the list below:")
    print("1-DB Admin\n2-Data Entry\n3-End User")

    selection = input("Please type 1, 2, or 3 to select your role: ")

    if selection in ['1', '2', '3']:
        username = input('User name: ')
        passcode = input('Password: ')
    
    cnx = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passcode)

    cur = cnx.cursor()
    cur.execute("USE ARTMUSEUM")

    if selection == '1':
        admin_consol()
    elif selection == '2':
        data_entry()
    elif selection == '3':
        guest_view(cur)
