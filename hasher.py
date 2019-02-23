'''hasher.py: This program takes in a hash value and uses brute-force to decrypt a SHA-1 hash into a valid password.'''

import hashlib
import time as t

common_passwords = open('10-million-password-list-top-1000000.txt')
password_lines = common_passwords.read().splitlines()

hash_value = raw_input("Please enter the hash value: ")
salt_value = raw_input("Please enter the salt value if applicable: ")

def main():
    start = t.time()
    counter = 0

    if salt_value:
        salt_hash(start, counter)

    for i in range(len(password_lines)):
        counter += 1
        if ((hashlib.sha1(bytes(password_lines[i].strip())).hexdigest()) == hash_value.strip()):
            print "Password cracked! It's {} ".format(password_lines[i].strip())
            end = t.time()
            total_time = end - start
            print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
            exit()
    
    end = t.time()
    total_time = end - start
    print "Password not found! Total time elapsed {}.".format(total_time)


def salt_hash(start, counter):
    for i in range(len(password_lines)):
        for j in range(len(password_lines)):
            counter += 1
            if ((hashlib.sha1(bytes(password_lines[j].strip())).hexdigest()) == salt_value.strip()):
                decoded_salt = password_lines[j]
                for k in range(len(password_lines)):
                    counter += 1
                    pre_salted_password = password_lines[k].strip() + decoded_salt.strip()
                    post_salted_password = decoded_salt.strip() + password_lines[k].strip()

                    if (((hashlib.sha1(bytes(pre_salted_password)).hexdigest()) == hash_value.strip()) | ((hashlib.sha1(bytes(post_salted_password)).hexdigest()) == hash_value.strip())):
                        print "The cracked salt is {} and the actual password is {}".format(decoded_salt.strip(), password_lines[k].strip())
                        end = t.time()
                        total_time = end - start
                        print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
                        exit()

if __name__ == '__main__':
    main()
