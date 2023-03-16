import datetime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(
            data="This is a the first information to create genesis block", proof=1, previous_hash="0", index=1)
        self.chain.append(genesis_block)

    def _hash(self, block: dict) -> str:
        encoded_block = _json.dumps(block, sort_keys= True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()

    def curr_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        previous_index = previous_block["index"]
        index = len(self.chain) + 1
        proof = self._proof_of_work(previous_proof,index,data)
        previous_hash = self._hash(block=previous_block)
        block = self._create_block(data=data, proof=proof, previous_hash=previous_hash,index=index)

        self.chain.append(block)
        return block

    def _to_digest(self, new_proof: int, previous_proof: int, index: str, data: str) -> bytes:
        to_digest = str(new_proof**2 - previous_proof**2 + index) + data
        return to_digest.encode()

    def _proof_of_work(self, previous_proof: str, index: int, data: str) -> int:
        new_poof = 1
        check_proof = False

        while not check_proof: 
            to_digest = self._to_digest(
                new_proof=new_poof, previous_proof=previous_proof, index=index, data=data,)
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if hash_value[:4] =="0000":
                check_proof = True
            else:
               new_poof += 1 
        return new_poof


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