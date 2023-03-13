import datetime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:
    def __init__(self) -> None:
        self.chain= list()
        genesis_block = self._create_block(data="This is a the first information to create genesis block", proof= 1 , previous_hash="0", index=1)
        self.chain.append(genesis_block)

    def curr_block(self, data:str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        previous_index = previous_block["index"]
        index = len(self.chain) + 1
        proof = None
        pass

    def get_previous_block(self) -> dict:
        return self.chain[-1]
         
    
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
             "index" : index,
             "timestamp": str(_dt.datetime.now()),
             "data":  data,
             "proof": proof,
             "previous_hash": previous_hash,

        }

        return block