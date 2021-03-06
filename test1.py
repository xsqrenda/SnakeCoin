from nextBlock import *
from initBlock import *
# 最简单的区块链
# Create the blockchain and add the genesis block
block_chain = [create_genesis_block()]
previous_block = block_chain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 2

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    block_chain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}".format(block_to_add.hash))
    print("Hash: {}\n".format(block_to_add.data))
