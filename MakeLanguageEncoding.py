import os


files = os.listdir('baseline/preprocessed_data')

for file in files:
    filename, file_extension = os.path.splitext(file)
    if filename != 'tm':
        target = open('baseline/experimentLanguageEnc/'+file, 'w', encoding="utf-8")
        with open('baseline/preprocessed_data/'+file, 'r', encoding="utf-8") as f:
            for line in f:
                    target.write(line)
        if filename == 'train' or filename == 'tiny_train':
            if file_extension == '.de':
                file_extension = '.en'
            else:
                file_extension = '.de'
            with open('baseline/preprocessed_data/'+filename+file_extension, 'r', encoding="utf-8") as f:
                for line in f:
                        target.write(line)
        target.close()


exit()