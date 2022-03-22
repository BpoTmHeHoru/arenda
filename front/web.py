from web3 import Web3
import json

config = json.load(open('./config.json'))
w3 = Web3(Web3.HTTPProvider(f'http://{config["node2"]["ip"]}:{config["node2"]["port"]}'))

if not w3.isConnected():
    print('пиздец')


contract = w3.eth.contract(address=config["contract"]["address"], abi=config["contract"]["abi"])

print(contract.all_functions())

print(w3.eth.accounts)

def unlock(acc, key):
    account = Web3.toChecksumAddress(acc)
    w3.eth.default_account = account
    w3.geth.personal.unlock_account(acc, key, 10)

def auth(acc, key, email, number):
    try:        
        w3.eth.default_account = w3.toChecksumAddress(acc)
        res = contract.functions.auth(email, number)
        return res, None
    except Exception as e:
        return None, str(e)

def reg(acc, key, fio, email, number):
    try:
        unlock(acc, key)
        res = contract.functions.reg(fio, email, number)
        return True, None
    except Exception as e:
        return False, str(e)


def returnhomes():
    try:
        w3.eth.default_account = w3.eth.accounts[0]
        homes = contract.functions.Returnhome().call()
        return [homes, None]
    except Exception as e:
        return [None, str(e)]

def addHouseInSystem(acc, key, kdn, area, usearea, rooms, amount):
    try:
        w3.eth.default_account = w3.toChecksumAddress(acc)
        unlock(acc, key)
        contract.functions.addHouseInSystem(kdn, area, usearea, rooms, amount).transact()
        return True
    except Exception as e:
        return str(e)

def removeHouseInSystem(acc, key):
    try:
        w3.eth.default_account = w3.toChecksumAddress(acc)
        unlock(acc, key)
        contract.functions.removeHouseInSystem().transact()
        return True
    except Exception as e:
        return str(e)

def addNewAdmin(acc, key, data):
    try:
        unlock(acc, key)
        addadmin = contract.functions.addNewAdmin(data).transact()
        return True
    except Exception as e:
        return str(e)

def addNewManager(acc, key, data):
    try:
        unlock(acc, key)
        addnewmanager = contract.functions.addNewManager(data).transact()
        return True
    except Exception as e:
        return str(e)

def delAdminManager(acc, key):
    try:
        unlock(acc, key)
        deladmin = contract.functions.delAdminManager().transact()
        return True
    except Exception as e:
        return str(e)