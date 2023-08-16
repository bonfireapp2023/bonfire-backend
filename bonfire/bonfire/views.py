# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# Other imports
from web3 import Web3
from decouple import config
import json 
import os


# Create your views here.
def index(request) -> HttpResponse:
    directory = os.listdir(".")
    print(directory)
    API_KEY = config('API_KEY')
    html_content = "<html><body><h1>Welcome to Bonfire</h1><p> {} </p></body></html>".format(API_KEY)
    return HttpResponse(html_content)

def contract(request):
    """ """
    url = 'http://127.0.0.1:9545/'
    w3 = Web3(Web3.HTTPProvider(url))
    
    CONTRACT_ADDRESS = config('CONTRACT_ADDRESS')
    compile_json = json.load(open('bonfire/static/BonfireApp.json'))
    
    
    # Load Contract ABI and Address:
    contract_address = CONTRACT_ADDRESS             # Replace with your contract address
    contract_abi = compile_json['abi']              # Replace with your contract's ABI
    
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Interact with contract
    details = contract_details(w3, contract_address, contract)
    interact_with_contract(contract)
    
    return details

def contract_details(w3, contract_address, contract):
    """ Get contract details """
    print("ABI:", contract.abi)
    
    # Retrieve and print contract functions
    contract_functions = contract.all_functions()
    print("Contract Functions:")
    for function in contract_functions:
        print("Function:", function.fn_name)
        # print()
        
    # Display as HTML
    html_function_list = "<ul>"
    for function in contract_functions:
        html_function_list += f"<li>Function: {function.fn_name}</li>"
    html_function_list += "</ul>"
    html_body = f"<h1>Contract Address: {contract_address}</h1><p>Functions:</p>{html_function_list}"
    return HttpResponse(html_body)

def interact_with_contract(contract):
    """ 
    address _address,
    AccessLevel _accessLevel
    """
    address = config('ACCOUNT_ADDRESS')
    checksum_address = Web3.to_checksum_address(address)
    access_level = 2 # "READ_WRITE"
    result = contract.functions.getAllowedOwnersForRequester(checksum_address, access_level).call()
    print('getAllowedOwnersForRequester', result)
    
    
# ABI Functions
def getAllowedOwnersForRequester(request):
    """ """
# 
def addAccess(request):
    """ """
    
