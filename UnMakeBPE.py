import sentencepiece as spm
import os


sp = spm.SentencePieceProcessor()

sp.load('joint.model')

with open('model_translations.txt', 'r', encoding="utf-8") as f:
    target = open('model_translations_BPE.txt', 'w', encoding="utf-8")
    for line in f:
            target.write(' '.join(sp.encode_as_pieces(line)) + '\n')
    target.close()


exit()