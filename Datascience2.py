
const crypto = require('crypto');

class Block {
  constructor(index, previousHash, timestamp, data, hash) {
    this.index = index;
    this.previousHash = previousHash;
    this.timestamp = timestamp;
    this.data = data;
    this.hash = hash;
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    return new Block(0, '0', Date.now(), 'Genesis Block', this.calculateHash(0, '0', Date.now(), 'Genesis Block'));
  }

  getLastBlock() {
    return this.chain[this.chain.length - 1];
  }

  calculateHash(index, previousHash, timestamp, data) {
    return crypto.createHash('sha256').update(index + previousHash + timestamp + data).digest('hex');
  }

  addBlock(newBlock) {
    newBlock.index = this.getLastBlock().index + 1;
    newBlock.previousHash = this.getLastBlock().hash;
    newBlock.timestamp = Date.now();
    newBlock.hash = this.calculateHash(newBlock.index, newBlock.previousHash, newBlock.timestamp, newBlock.data);
    this.chain.push(newBlock);
  }

  isChainValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== this.calculateHash(currentBlock.index, currentBlock.previousHash, currentBlock.timestamp, currentBlock.data)) {
        return false;
      }

      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }
    }
    return true;
  }
}

// Creating a new blockchain and adding blocks
const myBlockchain = new Blockchain();
myBlockchain.addBlock(new Block(1, myBlockchain.getLastBlock().hash, Date.now(), 'Data 1', ''));
myBlockchain.addBlock(new Block(2, myBlockchain.getLastBlock().hash, Date.now(), 'Data 2', ''));

// Printing the blockchain and checking its validity
console.log(JSON.stringify(myBlockchain, null, 2));
console.log('Is the blockchain valid? ' + myBlockchain.isChainValid());
