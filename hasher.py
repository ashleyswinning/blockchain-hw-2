''' This program takes in a hash value and uses brute-force to decrypt a SHA-1 hash into a valid password.'''

import hashlib, urllib, time as t, random

common_passwords = open('10-million-password-list-top-1000000.txt')
password_lines = common_passwords.read().splitlines()
counter = 0

hash_value = raw_input("Please enter the hash value: ")
salt_value = raw_input("Please enter the salt value if applicable: ")

start = t.time()

def main():

    for password in password_lines:
        #counter += 1
        if ((hashlib.sha1(bytes(password)).hexdigest()) == hash_value):
            print "Password cracked! It's {}".format(password)
            end = t.time()
            total_time = end - start
            print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
            exit()
    
    salt_hash()

    space_hash()

def space_hash():
    print "space"
    for password in password_lines:
        for p in password_lines:
            #counter += 1
            validate_string = "".join(password.split()) + " " + "".join(p.split())
            if (((hashlib.sha1(bytes(validate_string)).hexdigest()) == hash_value.strip())):
                print validate_string
                end = t.time()
                total_time = end - start
                print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
                exit()
            else:
                print p

def salt_hash():
    print "salt"
    if salt_value:
        for password in password_lines:
            for pwd in password_lines:
                #counter += 1
                if ((hashlib.sha1(bytes(pwd.strip())).hexdigest()) == salt_value.strip()):
                    decoded_salt = pwd
                    for p in password_lines:
                        pre_salted_password = p.strip() + decoded_salt.strip()
                        post_salted_password = decoded_salt.strip() + p.strip()

                        if (((hashlib.sha1(bytes(pre_salted_password)).hexdigest()) == hash_value.strip()) | ((hashlib.sha1(bytes(post_salted_password)).hexdigest()) == hash_value.strip())):
                            print "The cracked salt is {} and the actual password is {}".format(decoded_salt.strip(), p.strip())
                            end = t.time()
                            total_time = end - start
                            print "The number of iterations it took to decode the hash was {} and the time elapsed was {}.".format(counter, total_time)
                            exit()

main()
