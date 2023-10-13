import qrcode


PRODUCTS = []
def read_from_database():
    f = open("assignment7\database.txt" , "r")
    for line in f:
        result = line.split(",")
        my_dic = {"code" : result[0] , "name" : result[1] , "price" : result[2] ,"count" : result[3]   }     
        PRODUCTS.append(my_dic)
    f.close()  



def write_to_database():
     f = open("assignment7\database.txt" , "w")
     for i in range(len(PRODUCTS)):
        data=str(PRODUCTS[i]['code'])+ ',' +PRODUCTS[i]['name']+','+str(PRODUCTS[i]['price'])+','+str(PRODUCTS[i]['count'])+'\n'  
        f.write(data)
     f.close()



def Qr_code():
    name=input('enter name or code product : ')
    for product in PRODUCTS:
        if product['name'] == name or (product['code'] ) == name:
          QR=[]
          QR.append(product['name'])
          QR.append(product['code'])
          img=qrcode.make(QR)
          img.save("qrcode.png")
          print('Done')


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- ShowList")
    print("6- Buy")
    print("7- exit")


def add():
    code = input("enter code")
    name = input("enter name")
    price = input("enter price")
    count  = input("enter count")
    new_product ={ 'code':code , 'name':name , 'price':price ,'count':count }
    PRODUCTS.append(new_product)



def edit():
   user_input = input("enter name or code to edit: ")
   for product in PRODUCTS:
        if product['name'] == user_input or product['code'] == user_input:
                print('1 for  edit product name')
                print('2 for  edit product price')
                print('3 for  edit product count')
                print('4 for exit')
                number = int(input())
                if number == 1:
                    product['name'] = input(' enter new product name : ')
                    print('Done')
                elif number ==2:
                    product['price'] = float(input(' enter new  product price : '))
                    print('Done')
                elif number == 3:
                    product['count']=int(input(' enter new  product count : '))
                    print('Done')
                elif number == 4:
                    break  
                else:
                    print('Does not exist')



def remove():
    user_input = input("enter name or code to remove: ")
    for product in PRODUCTS:
        if product['name'] == user_input or product['code']== user_input:
            PRODUCTS.remove(product)
            print('Done')
            break
    else:
        print('Does not exist')





def search():
    user_input = input("enter name or code to search: ")
    for product in PRODUCTS:
        if product['code'] == user_input or product['name'] == user_input:
            print(product["code"] ,"\t\t", product["name"] ,"\t\t" , product["price"])
            break
    else:
         print("not found")



def show_list():
    print ("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t\t",product["name"] ,"\t\t" ,product["price"])




def buy():
    pri=[]
    while True:
        user_buy=input('name or id of product ? : ')
        for product in PRODUCTS:
            if product['name'] == user_buy  or product['id']== user_buy:
                buy_count=int(input('enter count of product to buy : '))
                if int(product['count']) >= buy_count:
                    pri.append({'name':product['name'],
                                'price':product['price'],
                                'count':buy_count})
                    product['count'] = product['count'] - buy_count
                else:
                    print('The number of products is not enough')
                    print('we have',product['count'])
                
        else:
            print('Does not exist')
       

        t=0
        for j in range(len(pri)):
            t += pri[j]['price']*pri['count']
        print('all price : ', t)
        break





print("Welcome To Setayesh Store")
print("Loading...")
read_from_database()
print(" Data Loaded.")

while True:
    show_menu()
    choice =int (input(" please enter your choice : "))

    if choice==1 :
        add()
    elif choice==2 :
        edit()
    elif choice==3 :
        remove()    
    elif choice==4 :
        search()
    elif choice==5 :
        show_list()
    elif choice==6 :
        buy()
    elif choice==7 :
        write_to_database()
        exit(0)
    else :
        print(" mesle adam vared kon")