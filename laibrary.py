user=[]
lib=[]

def register():
    if len(user)==0:
        id=100
    else:
        id=user[-1]['id']+1
    print(id)

    email=str(input("enter the email :"))
    f1=0
    for i in user:
        if i['email']==email:
            f1=1
            register()
    if f1==0:
    
            name=str(input("enter the name :"))
            phone=int(input("enter the  phone number:"))
            username=email
            password=input('enter the password:')
            user.append({'name':name,'id':id,'phone':phone,'email':email,'password':password})

def login():
    uname=input('enter username:')
    passw=input('enter password:')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    log=''
    for i in user:
        if uname==i['email'] and passw==i['password']:
            f=2
            log=i
    return f,user
def add_book():
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            add_book()
    
   
    name=str(input("enter the name :"))
    price=int(input("enter the  price:"))
    stock=int(input('enter the stock:'))
    lib.append({'name':name,'price':price,'stock':stock,'id':id})
def view_book():
    print(lib)
def ubdate_book():
    id=int(input('enter id :'))                                                         
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            price=int(input('enter price :'))                                   
            stock=str(input('enter stock :'))
            i['price']=price
            i['stock']=stock
    if f1==0:
        print('invalid id')
    
def delete():
    id=int(input('enter id :'))
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            lib.remove(i)

    if f1==0:
        print('invalid id')


def  view_user():
    for i in user:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])
        
    


while True:
    print('''
1.register
2.login
3.exit
''')
    choice=int(input('enter your choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add book
                2.view book
                3.ubdate book
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice :"))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:
                    ubdate_book()
                elif sub_choice==4:
                    delete()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
                else:
                    print('invalid')



            
        elif f==2:
            print('user login')
        elif f==0:
            print('invalid username or password')

    elif choice==3:
        break
    else:
        print('invalid')
   
       