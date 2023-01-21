input_id=input('id: ')
id='jiyoung'
input_password=input('password:')

password='010417'
#comment

if input_id == id:
    if input_password ==password:
        print('Welcome!')
    else:
        print('Wrong password')
else:
    print('Wrong id')