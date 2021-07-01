'''This will be the backend code for a web-based ranked choice voting system.  I think it could either have ID's as
private keys or it could have votes as private keys?

V1 Will allow citizens to send ranked votes to candidates.
V2 Will include wallets so candidates' votes will be properly attributed
V3 Will eliminate double spending and prevent citizens from sending more than the allowed amount to each candidate
V4 Will (hopefully) include front-end to allow for web voting through an interface
'''
import hashlib
'''TODO: CONNECT WALLET CLASS TO VOTEBLOCKCHAIN by making transaction into a class that includes Account'''
class VoteBlockChain(object):
	'''The blockchain with the record of all votes.
	Make transaction into a class that includes Account'''
	def __init__(self, prev_block_hash, transaction_list):
		self.prev_block_hash = prev_block_hash
		self.transaction_list = transaction_list
		self.block_data = "---".join(transaction_list) + "---" + prev_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Account(object):
	"""Account object that takes in a wallet"""
	def __init__(self, name, Wallet, nonce = 0):
		self.name = name
		self.walletId = [num for num in range(10)]
		self.Wallet = Wallet
		self.nonce = nonce
	def sexndVote(self, id, recipientId):
		pass
class Wallet:
	"""Wallet for candidates to hold votes they receive
		walletId, identifier for each wallet (public key)
		balance starts at 10 for each citizen
		Can send votes to candidates"""
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
		

	


def main():
	mine = Wallet(11)
	yours = Wallet(12)
	print(mine.sendVote(10, mine, yours))


if __name__ == '__main__':
	main()
mine = Wallet(11)
yours = Wallet(12)
mine.sendVote(10, mine, yours)
print(mine.get_account_balance(11))
#mine.sendVote(10, mine, yours)
print(yours.get_account_balance(12))
he = Account("coop", Wallet(13))


t1 = "Ryan sends 2 NC to Nova"
t2 = "Nova sends 234 NC to Nova"
t3 = "Alma sends 100 NC to Ava"
t4 = "Ava sends 10 NC to Rj"

genesis_block = VoteBlockChain("Hello Blockchain", [t1,t2])

print(genesis_block.block_data)
print(genesis_block.block_hash)