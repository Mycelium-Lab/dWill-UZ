import web3

def get_balance(wallet, network):
    if network == 3:
        web = web3.Web3(web3.Web3.HTTPProvider("https://ropsten.infura.io/v3/68b94f4d67f24e118b81ffd94dd0a0ee"))
    wallet = web.eth.getBalance(wallet)
    return wallet

print(get_balance("0x83297A98cAcc92743F58e90ce0E7373a22A0aaFA", 3))