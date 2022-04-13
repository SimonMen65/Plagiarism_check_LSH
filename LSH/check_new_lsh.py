from datasketch import MinHash
from nltk import ngrams
import utils

lsh = utils.load_lsh("./lsh_word_03.pickle")

def check_new_lsh(filename):
    # return a list of possible referenced files
    filename, text = utils.tokenize_file(filename)
    min_hash = MinHash(num_perm=128)

    for d in ngrams(text, 3):
        min_hash.update(" ".join(d).encode('utf-8'))

    return lsh.query(min_hash)

if __name__ == '__main__':
    # 需要等到redis设置完成了才能做
    check_file = './test_suspicious.txt'
    result = check_new_lsh(check_file)
    if len(result) == 0:
        print("The document is not plagiarized")
    else:
        print ("The document is plagiarized.\n" +\
              f"Here is the list of the files that were used:\n{result}")