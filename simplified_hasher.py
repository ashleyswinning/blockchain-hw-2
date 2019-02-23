'''hasher.py: This program takes in a hash value and uses brute-force to decrypt a SHA-1 hash into a valid password.'''

import hashlib, time as t

common_passwords = open('10-million-password-list-top-1000000.txt').read().splitlines()

hash_value = raw_input("Please enter the hash value: ").strip()
salt_value = raw_input("Please enter the salt value if applicable: ").strip()

def main():
    start = t.time()
    counter = 0
    if salt_value:
        for password in common_passwords:
            for pwd in common_passwords:
                counter += 1
                if ((hashlib.sha1(bytes(pwd.strip())).hexdigest()) == salt_value):
                    decoded_salt = pwd.strip()
                    for p in common_passwords:
                        counter += 1
                        pre_salted_password = p.strip() + decoded_salt
                        post_salted_password = decoded_salt + p.strip()
                        if (((hashlib.sha1(bytes(pre_salted_password)).hexdigest()) == hash_value) | ((hashlib.sha1(bytes(post_salted_password)).hexdigest()) == hash_value)):
                            print "The cracked salt is {} and the actual password is {}".format(decoded_salt, p.strip())
                            end = t.time()
                            total_time = end - start
                            print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
                            exit()

    for password in common_passwords:
        counter += 1
        if ((hashlib.sha1(bytes(password)).hexdigest()) == hash_value):
            print "Password cracked! It's {}".format(password)
            end = t.time()
            total_time = end - start
            print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
            exit()

if __name__ == '__main__':
    main()
