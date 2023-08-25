
"""
This code demonstrates a simple blockchain structure in Python.
"""

import hashlib
import json
from time import time


class Block:
    """
    A block in the blockchain.

    Args:
        index (int): The index of the block in the blockchain.
        timestamp (int): The timestamp of the block.
        data (str): The data in the block.
        previous_hash (str): The hash of the previous block.

    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    A blockchain.

    Args:
        chain (list): The list of blocks in the blockchain.

    """

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis block of the blockchain.
        """
        block = Block(0, time(), "Genesis block", "")
        self.chain.append(block)

    def add_block(self, data):
        """
        Adds a new block to the blockchain.

        Args:
            data (str): The data in the block.

        Returns:
            Block: The newly added block.
        """
        previous_hash = self.chain[-1].hash
        block = Block(len(self.chain), time(), data, previous_hash)
        self.chain.append(block)
        return block

    def is_valid(self):
        """
        Checks if the blockchain is valid.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.hash != current_block.calculate_hash():
                return False

        return True


def main():
    """
    The main function.
    """
    blockchain = Blockchain()

    blockchain.add_block("This is the first block")
    blockchain.add_block("This is the second block")

    print("The blockchain is valid:", blockchain.is_valid())


if __name__ == "__main__":
    main()
