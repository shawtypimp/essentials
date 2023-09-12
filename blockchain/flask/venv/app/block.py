import json
import os
import hashlib

blocks_dir = os.curdir + '/blocks/' # директория блоков

def get_hash(filename):
    file = open(blocks_dir + filename, 'rb').read()

    return hashlib.md5(file).hexdigest() # получаю хэш

def get_files():
    files = os.listdir(blocks_dir) # список файлов в папке blocks
    return sorted([int(i) for i in files]) # преобразовываем строчные названия файлов в числа и сортируем их по возрастанию

def check_integrity():
    files = get_files()

    results =[]

    for file in files[1:]:
        f = open(blocks_dir + str(file))
        h = json.load(f)['hash'] # получаем хэши предыдуших блоков

        prev_block = str(file - 1)

        actual_hash = get_hash(prev_block) # снова вычисленные хэши предыдущих блоков для сравнения

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted' # конечная проверка целости блоков 

        results.append({'block': prev_block, 'result': res})

    return results


def write_block(sender, recipient, amount, prev_hash=''):
    files = get_files()
    prev_file = files[-1] # берём номер последнего блока

    filename = str(prev_file + 1) # формирование имени нового блока

    prev_hash = get_hash(str(prev_file)) # переопределяю хэш

    data = {'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'hash': prev_hash}
    
    with open(blocks_dir + filename, 'w') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)



def main():
    write_block(sender ='frog', recipient = 'dog', amount = 3)


if __name__ == '__main__':
    main()