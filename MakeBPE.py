import sentencepiece as spm
import os

spm.SentencePieceTrainer.train('--input=baseline/raw_data/train.de,baseline/raw_data/train.en --model_prefix=joint --vocab_size=4000 --model_type=bpe')

sp = spm.SentencePieceProcessor()

sp.load('joint.model')

files = os.listdir('baseline/raw_data')

for file in files:
    target = open('baseline/experimentBPE/'+file, 'w', encoding="utf-8")
    with open('baseline/raw_data/'+file, 'r', encoding="utf-8") as f:
        for line in f:
                target.write(' '.join(sp.encode_as_pieces(line)) + '\n')
    target.close()


exit()