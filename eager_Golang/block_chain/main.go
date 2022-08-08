package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
)

// block

type Block struct {
	Hash     []byte `hash:"hash"`
	Data     []byte `data:"data"`
	PrevHash []byte `prev_hash:"prev_hash"`
}

func (b *Block) DeriveHash() {
	info := bytes.Join([][]byte{b.Data, b.PrevHash}, []byte{})
	hash := sha256.Sum256(info)
	b.Hash = hash[:]
}

func CreateBlock(data string, prevHash []byte) *Block {
	block := &Block{[]byte{}, []byte(data), prevHash}
	block.DeriveHash()
	return block

}

func Genesis() *Block {
	return CreateBlock("1", []byte{})
}

// blockchain

type BlockChain struct {
	blocks []*Block `blocks:"blocks"`
}

func (chain *BlockChain) AddBlock(data string) {
	prevBlock := chain.blocks[len(chain.blocks)-1]
	newBlock := CreateBlock(data, prevBlock.Hash)
	chain.blocks = append(chain.blocks, newBlock)
}

func InitBlockChain() *BlockChain {
	return &BlockChain{[]*Block{Genesis()}}
}

func main() {
	chain := InitBlockChain()

	chain.AddBlock("data2")
	chain.AddBlock("data3")
	chain.AddBlock("data4")
	chain.AddBlock("data5")

	GetBlockChain(chain)
}

func GetBlockChain(chain *BlockChain) {
	for index, block := range chain.blocks {
		ShowAllBlocks(block, index)
	}
}
func ShowAllBlocks(block *Block, index int) {
	fmt.Printf("index: %x \n", index)
	fmt.Printf("PrevHash: %x \n", block.PrevHash)
	fmt.Printf("Hash: %x \n", block.Hash)
	fmt.Printf("Data: %x \n", block.Data)
	fmt.Println("__________________________________________")
}
