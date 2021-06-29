'''This will be the backend code for a web-based ranked choice voting system.  I think it could either have ID's as
private keys or it could have votes as private keys?

V1 Will allow citizens to send ranked votes to candidates.
V2 Will include wallets so candidates' votes will be properly attributed
V3 Will eliminate double spending and prevent citizens from sending more than the allowed amount to each candidate
V4 Will (hopefully) include front-end to allow for web voting through an interface
'''
import hashlib

class VoteBlock(object):
	def __init__(self, prev_block_hash, transaction_list):
		self.prev_block_hash = prev_block_hash
		self.transaction_list = transaction_list
		self.block_data = "---".join(transaction_list) + "---" + prev_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Account(object):
	def __init__(self):
		self.walletId = [num for num in range(10)]
		self.Wallet = Wallet(walletId)
	def sendVote(self, id, recipientId):
		pass
class Wallet:
	"""Wallet for candidates to hold votes they receive
		walletId, identifier for each wallet (public key)
		balance starts at 10 for each citizen"""
	def __init__(self, walletId):
		self.id = walletId
		self.balance = 10
	def set_account_balance(self, id, amount):
		"""Sets account balances after object instantiation"""
		self.balance += amount
	def get_account_balance(self, id):
		"""Prints an int of account balance"""
		return int(self.balance)
	def sendVote(self, amount, id, other):
		"""Allows one citizen to send votes to another"""
		if self.get_account_balance(id) >= amount:
			other.set_account_balance(id, amount)
			self.set_account_balance(id, (0-amount))
		

	



mine = Wallet(11)
yours = Wallet(12)
mine.sendVote(10, mine, yours)
print(mine.get_account_balance(11))
#mine.sendVote(10, mine, yours)
print(yours.get_account_balance(12))



t1 = "Ryan sends 2 NC to Nova"
t2 = "Nova sends 234 NC to Nova"
t3 = "Alma sends 100 NC to Ava"
t4 = "Ava sends 10 NC to Rj"

genesis_block = VoteBlock("Hello Blockchain", [t1,t2])

print(genesis_block.block_data)
print(genesis_block.block_hash)