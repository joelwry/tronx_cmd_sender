from datetime import datetime

def __documentTransfer(details):
    try :
        with open('./transfer_details.txt', 'a') as fp :
            dated = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            fp.write(f'{details}\n')
            fp.write(f'{dated}\n')
            fp.write('--------------------------------------\n')
            
    except Exception as e :
        print(f'Error : {e}')

def send_trx(to_address, amount, client, private_key) -> int:
    '''
        to_address  : the tron wallet recieving the fund 
        amount : float the amount to send
        client : the tron api client. gotten like this client = Tron(network="shasta") 
        private_key : this is a PRIVATE KEY OBJECT created from the sender private key that will be used to sign the transaction
    '''
    try : 
        txn = (
            client.trx.transfer(private_key.public_key.to_base58check_address(), to_address, int(amount * 1_000_000))
            .build()
            .sign(private_key)
        )
        txn.broadcast()
        detail = f"Sent {amount} TRX to {to_address}. Transaction ID: {txn.txid}"
        print(detail)
        __documentTransfer(detail)
        return 1
    except Exception as e :
        print(e)
        return 0

