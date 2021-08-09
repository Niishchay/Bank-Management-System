import mysql.connector
import random
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='bank_management')


def OpenAcc():
    x = mydb.cursor()
    name = input("Enter your Name: ")
    acno = random.randint(1000000000, 9999999999)
    while True:
        d1 = (acno,)
        q1 = 'select * from account where AccNo = %s'
        x.execute(q1, d1)
        r = x.fetchone()
        if r:
            acno = random.randint(1000000000, 9999999999)
        else:
            break
    dob = input("Enter your date of birth (yyyy-mm-dd): ")
    add = input("Enter your address: ")
    contact = input("Enter your contact no: ")
    bal = input("Enter the minimum balance you wish to deposit: ")
    data1 = (name, acno, dob, add, contact, bal)
    data2 = (name, acno, bal)
    sql1 = 'insert into account values (%s, %s, %s, %s, %s, %s)'
    sql2 = 'insert into amount values(%s, %s, %s)'
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print(f"Data is Entered Successfully your account number is {acno}")


def DepoAmt():
    acno = input("Enter the account number: ")
    sql1 = 'select Balance from amount where AccNo = %s'
    data1 = (acno,)
    x = mydb.cursor()
    x.execute(sql1, data1)
    result = x.fetchone()
    if not result:
        print("invalid account number!")
    else:
        amount = input("Enter the amount you want to deposit: ")
        total = int(amount) + result[0]
        data2 = (total, acno)
        sql2 = 'update amount set Balance = %s where AccNo = %s'
        x.execute(sql2, data2)
        mydb.commit()
        print(f"{amount} rupees credited to your account number {acno}")


def WithAmt():
    acno = input("Enter the account number: ")
    sql1 = 'select Balance from amount where AccNo = %s'
    data1 = (acno,)
    x = mydb.cursor()
    x.execute(sql1, data1)
    result = x.fetchone()
    if not result:
        print("invalid account number!")
    else:
        amount = input("Enter the amount you want to deposit: ")
        total = result[0] - int(amount)
        data2 = (total, acno)
        sql2 = 'update amount set Balance = %s where AccNo = %s'
        x.execute(sql2, data2)
        mydb.commit()
        print(f"{amount} rupees amount debited from your account number {acno}")


def BalEnq():
    acno = input("Enter the account number: ")
    sql1 = 'select Balance from amount where AccNo = %s'
    data1 = (acno,)
    x = mydb.cursor()
    x.execute(sql1, data1)
    result = x.fetchone()
    if not result:
        print("invalid account number!")
    else:
        print(f"{result[0]} rupees is in your account number {acno}")


def DisDet():
    acno = input("Enter the account number: ")
    sql1 = 'select * from account where AccNo = %s'
    data1 = (acno,)
    x = mydb.cursor()
    x.execute(sql1, data1)
    result = x.fetchone()
    if not result:
        print("invalid account number!")
    else:
        print(f'''
                Name : {result[0]}
                Account Number : {result[1]}
                Date of Birth : {result[2]}
                Address : {result[3]}
                Contact Number: {result[4]}
                Balance : {result[5]}
            ''')


def CloseAcc():
    acno = input("Enter the account number: ")
    sql1 = 'delete from account where AccNo = %s'
    sql2 = 'delete from amount where AccNo = %s'
    data1 = (acno,)
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data1)
    mydb.commit()
    print(f"Your account number {acno} from this bank is closed")


if __name__ == '__main__':

    print('''
            1. OPEN NEW ACCOUNT
            2. DEPOSIT AMOUNT
            3. WITHDRAW AMOUNT
            4. BALANCE ENQUIRY
            5. DISPLAY CUSTOMER DETAILS
            6. CLOSE ACCOUNT
            7. EXIT
            ''')
    choice = int(input("Enter the task number you want to perform: "))
    if choice == 1:
        OpenAcc()
    elif choice == 2:
        DepoAmt()
    elif choice == 3:
        WithAmt()
    elif choice == 4:
        BalEnq()
    elif choice == 5:
        DisDet()
    elif choice == 6:
        CloseAcc()
    elif choice == 7:
        print("Thank you for Visiting")
    else:
        print("Invalid Choice!")
