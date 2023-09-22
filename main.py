import random
import bcrypt
import pandas as pd

N_PASSWD_DATASET = 100

def main():
    print(generate_dataset(len=5, dictionary="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def generate_dataset(len:int, dictionary: str):
    df = pd.DataFrame()
    df.columns = ["passwd", "hash"]
    for _ in range(NUMBER_OF_PASSWORDS):
        passwd = generate_passwd(len, dictionary)
        df.loc[len(df)] = {
            "passwd": passwd
            "hash": #TODO: hash the password
        }
    return 
    
def generate_passwd(len:int, dictionary: str):
    return  "".join([random.choice(dictionary) for _ in range(len)])


if __name__ == "__main__":
    main()