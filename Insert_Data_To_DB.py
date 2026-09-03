import sqlite3


def Insert_Into_DB(choice,list1):
    conn=sqlite3.connect("Elections2024India.db")
    cursor=conn.cursor()
    match choice:
        case "states":
            cursor.execute("insert into states values(?,?)",list1)

        case "constituencies":
            cursor.execute("insert into constituencies values(?,?,?)",list1)
    
        case "candidates":
            cursor.execute("insert into candidates values(?,?,?,?,?,?,?)",list1)

    conn.commit()
    conn.close()