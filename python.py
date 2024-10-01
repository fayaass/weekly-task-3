user=[{'name': 'aaa', 'id': 101, 'email': 'a@', 'fwrs': [201,202], 'phone': 123, 'password': 'asd'}]
fwr=[{'name':'shoe','id':201,'price':2500,'stock':10},{'name':'slider','id':202,'price':1000,'stock':5}]

def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    
    email=str(input('enter email :'))
    f1=0
    for i in user:
            if i['email']==email:
                f1=1
                register()
    if f1==0:
            name=str(input('enter the name :'))
            username=email
            phone=int(input('enter phone no :'))
            password=input('enter the password :')
            user.append({'name':name,'id':id,'email':email,'fwrs':[],'phone':phone,'password':password})


def login():
    uname=input('enter uname')
    passw=input('enter passw')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    log=''
    for i in user:
        if uname==i['email'] and passw==i['password']:
            f=2
            log=i
    return f,log   


def add_fwr():
    if len(fwr)==0:
        id=201
    else:
        id=fwr[-1]['id']+1
    f1=0
    for i in fwr:
        if i['id']==id:
            f1=1
            add_book()
    if f1==0:
        name=str(input('enter the name :'))
        price=int(input('enter the price :'))
        stock=int(input('enter the stock'))
        fwr.append({'name':name,'id':id,'price':price,'stock':stock})


def view_fwr():
    for i in fwr:
        print(i)


def update_fwr():
    id=int(input('enter id :'))                                                         
    f1=0
    for i in fwr:
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
    for i in fwr:
        if i['id']==id:
            f1=1
            fwr.remove(i)

    if f1==0:
        print('invalid id')


def view_user():
    for i in  user:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])








def view_profile(log):
    print(log)


def update_profile(log):

    name=str(input('enter name :'))
    phone=int(input('enter phone :'))
    log['name']=name
    log['phone']=phone
  


def buy_fwr(log):
    id=int(input('enter id :'))
    f=0
    for i in fwr:
        if i['id']==id:
            f=1
            i['stock']-=1
            log['fwrs'].append(id)
            print('shoes added')
    if f==0:
        print('invalid id')




def fwr_in_hand(log):
    print(log['fwrs'])





while True:
    print('''
1.register
2.login
3.exit
    ''')
    choice=int(input('enter the choice'))
    if choice==1:
        register()
    elif choice==2:
        f,log=login()

        if f==1:
            while True:
                print('''
                1.add fwr
                2.view fwr
                3.update fwr
                4.delete
                5.view user
                6.exit
                ''')
                sub_ch=int(input('enter the choice :'))
                if sub_ch==1:
                    add_fwr()
                elif sub_ch==2:
                    view_fwr()
                elif sub_ch==3:
                    update_fwr()
                elif sub_ch==4:
                    delete()
                elif sub_ch==5:
                    view_user()
                elif sub_ch==6:
                    break

        elif f==2:
            while True:
                print('''
                1.view profile
                2.view fwr
                3.update profile
                4.buy fwr
                5.fwr in hand
                6.exit
                ''')
                sub_ch=int(input('enter the choice :'))
                if sub_ch==1:
                    view_profile(log)
                elif sub_ch==2:
                    view_fwr()
                elif sub_ch==3:
                    update_profile(log)
                elif sub_ch==4:
                    buy_fwr(log)
                elif sub_ch==5:
                    fwr_in_hand(log)
                elif sub_ch==6:
                    break


        elif f==0:
            print('invalid uname or passw')
    elif choice==3:
        break
    else:
        print('invalid')