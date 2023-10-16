import random
import string
import time
import pandas as pd

# from passlib.hash import sha256_crypt
import hashlib


def main():
	t = time.time()
	# Generate the 20 random datasets
	run_datasets_on(dictionary=string.ascii_lowercase, name="min")
	run_datasets_on(dictionary=string.ascii_uppercase, name="may")
	run_datasets_on(dictionary=string.digits, name="num")
	run_datasets_on(
		dictionary=string.ascii_lowercase
		+ string.ascii_uppercase
		+ string.digits
		+ string.punctuation,
		name="alphanumsym",
	)
	# Generate the 5 dictionary based datasets.
	# Import password tables and select them randomly.
	word_list = [line.strip() for line in open("rockyou.txt", encoding="latin-1")]

	# random rockyou passwords dict passwd #1
	data_set = generate_dataset(1, word_list)
	data_set.to_csv("passwd_rckyou_plain.csv", header=False, index=False)

	# random rockyou passwords with random modificatios to their case.
	data_set = generate_rockyou2_dataset(word_list)
	data_set.to_csv("passwd_rckyou_cased.csv", header=False, index=False)

	# random rockyou password with Letter randomly capitalized and 3 random digits appended.
	data_set = generate_rockyou5_dataset(2, word_list)
	data_set.to_csv("passwd_rckyou_mashed.csv", header=False, index=False)

	# random rockyou password turned over
	data_set = generate_rockyou3_dataset(word_list)
	data_set.to_csv("passwd_rckyou_reverse.csv", header=False, index=False)

	# random rockyou password randomly capitalized turned over and randomly added digits to the begining and to the end
	data_set = generate_rockyou4_dataset(word_list)
	data_set.to_csv("passwd_rckyou_multi.csv", header=False, index=False)

	print("Finished on :", time.time() - t, " sec")


def run_datasets_on(dictionary, name):
	for i in range(3, 8):
		data_set = generate_dataset(len=i, dictionary=dictionary)
		data_set.to_csv(f"passwd_{name}_{i}.csv", header=False, index=False)


def generate_rockyou5_passwd(dict):
	base_word = random.choice(dict)
	word = base_word if random.choice([True, False]) else base_word.capitalize()
	word = word + str(random.randint(0, 999))
	return word


def generate_rockyou5_dataset(dict):
	pwd_gemerated = 0
	pwds = []
	hashs = []

	while pwd_gemerated < 100:
		pwd = generate_rockyou5_passwd(dict)
		if pwd not in pwds:
			pwds.append(pwd)
			pwd_gemerated += 1
			m = hashlib.sha256()
			m.update(bytes(pwd, "utf-8"))
			hashs.append(m.hexdigest())
	df = pd.DataFrame(hashs, columns=["hash"])
	return df


def generate_rockyou2_dataset(dictionary):
	pwd_gemerated = 0
	pwds = []
	hashs = []
	while pwd_gemerated < 100:
		pwd = generate_rockyou2_passwd(dictionary)
		if pwd not in pwds:
			pwds.append(pwd)
			pwd_gemerated += 1
			m = hashlib.sha256()
			m.update(bytes(pwd, "utf-8"))
			hashs.append(m.hexdigest())
	df = pd.DataFrame(hashs, columns=["hash"])
	return df


def generate_rockyou2_passwd(dictionary):
	# Change case randomly
	base_word = random.choice(dictionary)
	word = ""
	for (
		char
	) in base_word:  # for each char in the word, randomly uppercase it if possible.
		word += (
			char.upper() if char.isalpha() and random.choice([True, False]) else char
		)
	return word


def generate_rockyou3_passwd(dictionary):
	word = random.choice(dictionary)
	return word[::-1]


def generate_rockyou3_dataset(dictionary):
	pwd_gemerated = 0
	pwds = []
	hashs = []
	while pwd_gemerated < 100:
		pwd = generate_rockyou3_passwd(dictionary)
		if pwd not in pwds:
			pwds.append(pwd)
			pwd_gemerated += 1
			m = hashlib.sha256()
			m.update(bytes(pwd, "utf-8"))
			hashs.append(m.hexdigest())
	df = pd.DataFrame(hashs, columns=["hash"])
	return df


def generate_rockyou4_password(dictionary):
	word = random.choice(dictionary)
	word = word if random.choice([True, False]) else word[::-1]  # randomly turnover
	word = word if random.choice([True, False]) else word.capitalize()  # randomly case
	word = word + str(random.randint(0, 999)) # randomly added number
	return word


def generate_rockyou4_dataset(dictionary):
	pwd_gemerated = 0
	pwds = []
	hashs = []
	while pwd_gemerated < 100:
		pwd = generate_rockyou4_password(dictionary)
		if pwd not in pwds:
			pwds.append(pwd)
			pwd_gemerated += 1
			m = hashlib.sha256()
			m.update(bytes(pwd, "utf-8"))
			hashs.append(m.hexdigest())
	df = pd.DataFrame(hashs, columns=["hash"])
	return df


def generate_dataset(len: int, dictionary: str):
	pwd_gemerated = 0
	pwds = []
	hashs = []
	while pwd_gemerated < 100:
		pwd = generate_passwd(len, dictionary)
		if pwd not in pwds:
			pwds.append(pwd)
			pwd_gemerated += 1
			m = hashlib.sha256()
			m.update(bytes(pwd, "utf-8"))
			hashs.append(m.hexdigest())
	df = pd.DataFrame(hashs, columns=["hash"])
	return df


def generate_passwd(len: int, dictionary: str):
	# Returns a len sized string generated by randomly picking chars in dictionary
	return "".join([random.choice(dictionary) for _ in range(len)])


if __name__ == "__main__":
	main()
