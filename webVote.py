'''This will be the backend code for a web-based ranked choice voting system.  I think it could either have ID's as
private keys or it could have votes as private keys?

V1 Will allow citizens to send ranked votes to candidates.
V2 Will include wallets so candidates' votes will be properly attributed
V3 Will eliminate double spending and prevent citizens from sending more than the allowed amount to each candidate
V4 Will (hopefully) include front-end to allow for web voting through an interface
'''
import hashlib
import blkchn1.py
class VoteBlock(object):
	def __init__(self, prev_block_hash, vote_list):
		self.prev_block_hash = prev_block_hash
		self.vote_list = vote_list
		self.hash_data = hash_data
		self.block_data = block_data
		self.block_data = "---".join(transaction_list) + "---" + prev_block_hash
		self.hash_data = hashlib.sha256(self.block_data.encode()).hexdigest()
t1 = "Ryan sends 5 VOTE to Nova"
t2 = "Nova sends 2 VOTE to Nova"
t3 = "Alma sends 1 VOTE to Ava"
t4 = "Ava sends 3 VOTE to Rj"

genesis_block = NewCoinBlock("Hello Blockchain", [t1,t2])

print(genesis_block.block_data)
print(genesis_block.block_hash)