
def getAccountBalance(wallet_address, client) -> float |None :
    '''
        Fetch the account balance using the wallet_address of the sender and the Tron client library
    '''
    try : 
        # account = client.get_account(wallet_address)
        # balance = account['balance'] 
        balance = client.get_account_balance(wallet_address)
        print(f"Balance for {wallet_address}: {balance} TRX")
        return balance
    except Exception as e :
        print(e)
        return None

