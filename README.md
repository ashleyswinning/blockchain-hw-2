### blockchain-hw-2
Ashley Huynh
CSC 4980 Assignment #2

### How to Run Programs:
###### The regular python file is `hasher.py`, simplified (bonus) file is `simplified_hasher.py`
* Please note: the included programs utilize an additional library to `hashlib`, which is `time`, in order to time the length of the program. The `time` library comes built in to Python, so in order to install `time` Python must be installed.

###### To run `hasher.py`:
* Make sure you are in the `blockchain-hw-2` directory and run `python hasher.py`

###### To run `simplified_hasher.py`:
* Make sure you are in the `blockchain-hw-2` directory and run `python simplified_hasher.py`


### Solutions
###### Example 1: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
* **Actual password**: letmein
* The number of iterations it took `hasher.py` to decode the hash was 16 and the time elapsed was 0.0251660346985.
* The number of iterations it took `simplified_hasher.py`  to decode the hash was 16 and the time elapsed was 0.000162124633789.

###### Example 2: 801cdea58224c921c21fd2b183ff28ffa910ce31
* **Actual password**: vjhtrhsvdctcegth
* The number of iterations it took `hasher.py` to decode the hash was 999968 and the time elapsed was 1.71048903465.
* The number of iterations it took `simplified_hasher.py` decode the hash was 999968 and the time elapsed was 1.43165707588.

###### Example 3: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
* **Actual password**: harib
* **Salt value cracked**: slayer
* The number of iterations it took `hasher.py` to decode the hash was 546373 and the time elapsed was 2.05584907532.
* The number of iterations it took `simplified_hasher.py` to decode the hash was 546373 and the time elapsed was 1.73734498024.



