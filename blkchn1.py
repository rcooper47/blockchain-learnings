'''
NewCoin (NC)

t1: nova sends ry 2 NC
transactions are stored in blocks
Block 1 ("Previous hash", t1,t2,t3)
can hash the block to receive an output
output for why?
hash result of a block is its signature / pointer

Block X(hash of X-1, transactions)

verification / validation relies on having the previous hash
if a transaction in a block is invalid, the following hash will be invalid
if a previous hash is invalid, one cannot navigate to a previous transaction


'''
import hashlib

class NewCoinBlock(object):
	def __init__(self, prev_block_hash, transaction_list):
		self.prev_block_hash = prev_block_hash
		self.transaction_list = transaction_list
		self.block_data = "---".join(transaction_list) + "---" + prev_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
t1 = "Ryan sends 2 NC to Nova"
t2 = "Nova sends 234 NC to Nova"
t3 = "Alma sends 100 NC to Ava"
t4 = "Ava sends 10 NC to Rj"

genesis_block = NewCoinBlock("Hello Blockchain", [t1,t2])

print(genesis_block.block_data)
print(genesis_block.block_hash)