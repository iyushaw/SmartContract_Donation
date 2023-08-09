from web3 import Web3

# Connect to a local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Check if the connection is successful
if w3.isConnected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect to Ethereum node")

contract_address = "YOUR_CONTRACT_ADDRESS"
contract_abi = [...]  # Your contract's ABI
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Call the getDonationCount() function
donation_count = contract.functions.getDonationCount().call()

# Call the getDonationDetails() function
index = 0  # Replace with the desired donation index
donation_details = contract.functions.getDonationDetails(index).call()

# Send a donation using the donate() function
sender_address = "SENDER_ADDRESS"
value_in_wei = w3.toWei(1, 'ether')  # Donation amount in Wei
tx_hash = contract.functions.donate().transact({'from': sender_address, 'value': value_in_wei})

# Call the getTotalDonated() function
total_donated = contract.functions.getTotalDonated().call()
