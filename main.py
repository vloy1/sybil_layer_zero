import requests
from eth_account import Account
from eth_account.messages import encode_defunct

def wallet_adress(private_key):
    return  Account.from_key(private_key=private_key)

def run(private_key_):
    message = "This is a sybil address"
    adress = wallet_adress(private_key_).address
    signature = Account.sign_message(signable_message=encode_defunct(text=message),private_key=private_key_).signature.hex()
    response =  requests.post("https://sybil.layerzero.network/api/report", json={
        "chainType": "evm",
        "signature": signature,
        "message": message,
        "address": adress
    })
    print(response.text)
    return response.text


def write_t(text):
    with open('wal_true.txt', 'a') as f:
        f.write(f'{text}\n')

def wallett(file):
    try:
        private = open(file,'r').read().splitlines()
        wallet = private[00]
        return wallet
    except:
        print('Кошельки кончились')

def wallett_del(file):
    ish = open(file,'r').readlines()
    del ish[00]
    with open(file, "w") as file:
        file.writelines(ish)

def main():
    while True:
        wal = wallett('wal.txt')
        res = run(wal)
        write_t(f'{wal} {res}')
        wallett_del('wal.txt')

if __name__ == '__main__':
    main()       
    
