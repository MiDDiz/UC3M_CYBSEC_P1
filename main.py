import random
import string
import time
import pandas as pd
from passlib.hash import sha256_crypt


def main():
    t = time.time()
    # Generate the 20 random datasets
    run_datasets_on(dictionary=string.ascii_lowercase, name="min")
    run_datasets_on(dictionary=string.ascii_uppercase, name="may")
    run_datasets_on(dictionary=string.digits, name="num")
    run_datasets_on(dictionary=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, name="alphanumsym")
    # Generate the 5 dictionary based datasets. 
    # Import password tables and select them randomly.
    word_list = [line.strip() for line in open('rockyou.txt', encoding='latin-1')]
    
	# random rockyou passwords dict passwd #1
    data_set = generate_dataset(1, word_list)
    data_set.to_csv("passwd_rckyou_plain.csv", header=False, index=False)
    
	# random rockyou passwords with modificatios to their case.
    data_set = generate_rockyou2_dataset(word_list)
    data_set.to_csv("passwd_rckyou_cased.csv", header=False, index=False)
    
    # random rockyou password combined together
    data_set = generate_dataset(2, word_list)
    data_set.to_csv("passwd_rckyou_mashed.csv", header=False, index=False)
    
    # random rockyou password tuned over
    data_set = generate_rockyou3_dataset(word_list)
    data_set.to_csv("passwd_rckyou_reverse.csv", header=False, index=False)
    
	# random rockyou password changed case and mashed between 1 to 4 words.
    data_set = generate_rockyou4_dataset(word_list)
    data_set.to_csv("passwd_rckyou_multi.csv", header=False, index=False)
    
    print("Finished on :", time.time() - t, " sec")
    

def run_datasets_on(dictionary, name):
    for i in range(3, 8):
        data_set = generate_dataset(len=i, dictionary=dictionary)
        data_set.to_csv(f"passwd_{name}_{i}.csv", header=False, index=False)



"""
passwd = generate_passwd(len, dictionary) # gen new passwd
data = {
    "passwd": passwd,
    "hash": bcrypt.hashpw(bytes(passwd, 'ascii'), bcrypt.gensalt()) # append hashed passwd
}
df = pd.DataFrame(data, index=[0])
for _ in range(N_PASSWD_DATASET - 1):
    passwd = generate_passwd(len, dictionary) # gen new passwd
    new_df = pd.DataFrame({
        "passwd": passwd,
        "hash": bcrypt.hashpw(bytes(passwd, 'ascii'), bcrypt.gensalt()) # append hashed passwd
    }, index=[0])
    df = pd.concat([df, new_df], ignore_index=True)
"""

def generate_rockyou2_dataset(dictionary):
    pwd_gemerated = 0
    pwds = []
    hashs = []
    hashs_b = []
    while pwd_gemerated < 100:
        pwd = generate_rockyou2_passwd(dictionary)
        if pwd not in pwds:
            pwds.append(pwd)
            pwd_gemerated += 1
            hashs.append(sha256_crypt.using(rounds=1000).hash(pwd))
            #hashs_b.append(bcrypt.hashpw(bytes(pwd, 'ascii'), bcrypt.gensalt()))
            #hashs_b.append(crypt.crypt(pwd, crypt.METHOD_MD5))
            
    df = pd.DataFrame(hashs, columns=["hash"])
        
    return df

def generate_rockyou2_passwd(dictionary):
	# Change case randomly
	word = random.choice(dictionary)
	word = word.split()
	for idx, elem  in enumerate(word): # for each char in the word, randomly uppercase it if possible.
		word[idx] = elem.upper() if elem.isalpha() and random.choice([True, False]) else elem
	return "".join(word)


def generate_rockyou3_passwd(dictionary):
    word = random.choice(dictionary)
    return word[::-1]
    
def generate_rockyou3_dataset(dictionary):
    pwd_gemerated = 0
    pwds = []
    hashs = []
    hashs_b = []
    while pwd_gemerated < 100:
        pwd = generate_rockyou3_passwd(dictionary)
        if pwd not in pwds:
            pwds.append(pwd)
            pwd_gemerated += 1
            hashs.append(sha256_crypt.using(rounds=1000).hash(pwd))
            #hashs_b.append(bcrypt.hashpw(bytes(pwd, 'ascii'), bcrypt.gensalt()))
            #hashs_b.append(crypt.crypt(pwd, crypt.METHOD_MD5))
    df = pd.DataFrame(hashs, columns=["hash"])
    return df

def generate_rockyou4_dataset(dictionary):
    pwd_gemerated = 0
    pwds = []
    hashs = []
    hashs_b = []
    while pwd_gemerated < 100:
        pwd = "".join([generate_rockyou2_passwd(dictionary) for _ in range(random.randrange(3))])
        if pwd not in pwds:
            pwds.append(pwd)
            pwd_gemerated += 1
            hashs.append(sha256_crypt.using(rounds=1000).hash(pwd))
            #hashs_b.append(bcrypt.hashpw(bytes(pwd, 'ascii'), bcrypt.gensalt()))
            #hashs_b.append(crypt.crypt(pwd, crypt.METHOD_MD5))
            
    df = pd.DataFrame(hashs, columns=["hash"])
    return df


def generate_dataset(len:int, dictionary: str):
    pwd_gemerated = 0
    pwds = []
    hashs = []
    hashs_b = []
    while pwd_gemerated < 100:
        pwd = generate_passwd(len, dictionary)
        if pwd not in pwds:
            pwds.append(pwd)
            pwd_gemerated += 1
            hashs.append(sha256_crypt.using(rounds=1000).hash(pwd))
            
			
			#hashs_b.append(bcrypt.hashpw(bytes(pwd, 'ascii'), bcrypt.gensalt()))
            #hashs_b.append(crypt.crypt(pwd, crypt.METHOD_MD5))
            
    df = pd.DataFrame(hashs, columns=["hash"])
        
    return df
    
def generate_passwd(len:int, dictionary: str):
    # Returns a len sized string generated by randomly picking chars in dictionary
    return  "".join([random.choice(dictionary) for _ in range(len)])


if __name__ == "__main__":
    main()