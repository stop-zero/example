input_id=input('id: ')
id='jiyoung'
input_password=input('password:')

password='0000'
#comment

if input_id == id:
    if input_password ==password:
        print('Welcome!')
    else:
        print('Wrong password')
else:
    print('Wrong id')