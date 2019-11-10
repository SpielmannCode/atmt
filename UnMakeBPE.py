import sentencepiece as spm
import os


sp = spm.SentencePieceProcessor()

sp.load('joint.model')

with open('model_translations.txt', 'r', encoding="utf-8") as f:
    target = open('model_translations.out', 'w', encoding="utf-8")
    for line in f:
        BPE = line.split()
        target.write((sp.decode_pieces(BPE)) + '\n')
    target.close()


exit()