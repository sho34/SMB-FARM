# *****************************************************************************************************************
# ********************** THE CAVEMAN ALGORITHM FOR ENCRYPTING PASSWORDS IN A DATABASE *****************************
# *                                                                                                               *
# * - Written by Mkayy (Vector coorp)                                                                             *
# * - not complete yet there is one final protocol to make it, at the very least secure for most use cases.       *
# * - The most efficient way of using this is updating the salt and the password every 2 seconds                  *
# *                                                                                                               *
# *****************************************************************************************************************

import os
from hashlib import pbkdf2_hmac, sha256
from hmac import compare_digest
from operator import mod

iterators = 500_000


# the random key is generated everytime a user creates a password.
# I then produce its 64 byte hex digest
# then encrypt the key along with the hex digest of the user's password.
# then store it in the database.

class CavemanCrypt:
    def __init__(self):
        self.salt_chunks = list()

    @staticmethod
    def split_digest(byte64_hash_string_salt_key: str) -> list:
        """
            --
        """
        chunk_cache_list = []
        for i in range(len(byte64_hash_string_salt_key)):
            # cache index 
            if mod(i, 2) == 0:
                # last indexes are [60, 64]
                x_index = i * 2
                y_index = (i * 2) + 4

                # print(f"index = [{x_index}:{y_index}]")
                chunk_cache_list.append(byte64_hash_string_salt_key[x_index:y_index])
                # print(salt_key[x_index:y_index])
                if x_index == 60 and y_index == 64:
                    break
        return chunk_cache_list

    def combine_stringify(self, salt: list, password_hash: list) -> str:
        tmp = []

        for x, y in enumerate(password_hash):
            tmp.append(salt[x] + y)

        return self.stringify(tmp)

    @staticmethod
    def stringify(data: list) -> str:
        tmp1 = ''
        for chunk in data:
            tmp1 = tmp1 + chunk

        return tmp1

    # use the two functions bellow to encrypt and decrypt your 64 bit password
    def caveman_crypt_2_0(self, password_key_in, salt_key_in):
        """
            --> Encrypts the password 
        """
        # returns the encrypted password 
        in1 = self.split_digest(salt_key_in)
        in2 = self.split_digest(password_key_in)

        return self.combine_stringify(in1, in2)

    def split_revert(self, byte128_hash_string_salt_key) -> list:
        """
            --> Returns the decrypted password 
        """
        chunk_list = []
        # salt 
        salt_key_ = []
        # password
        password_key = []
        for i in range(len(byte128_hash_string_salt_key)):
            # cache index 
            if mod(i, 2) == 0:
                # last indexes are [124, 128]
                x_index = i * 2
                y_index = (i * 2) + 4

                # print(f"index = [{x_index}:{y_index}]")
                chunk_list.append(byte128_hash_string_salt_key[x_index:y_index])
                # print(salt_key[x_index:y_index])
                if x_index == 124 and y_index == 128:
                    break

                # take every even number index and join them

        for i, chunk in enumerate(chunk_list):

            if mod(i, 2) == 0:
                # for all even numbers.
                salt_key_.append(chunk)
            else:
                password_key.append(chunk)

        return [self.stringify(password_key), self.stringify(salt_key_)]  # [password, key]

    def is_password_correct(self, stored_encrypted_password: bytes, password: bytes) -> bool:
        # fetch the encrypted password from the database
        # use split_revert function on the password
        password_and_key = self.split_revert(stored_encrypted_password)
        # the only problem with this method of verifying the password is that when using a different machine it may
        # produce a different p_word_cmp which will likely result in password verification errors.
        p_word_cmp = pbkdf2_hmac(
            'sha256', password.encode('utf-8'), password_and_key[1].encode('utf-8'), iterators
        )

        return compare_digest(password_and_key[0], p_word_cmp.hex())

    def start_encryption(self, password: str) -> str:
        encryption_salt = os.urandom(8) * 2  # generate a random salt
        encryption_salt_hex = sha256(encryption_salt)
        password_encrypt = pbkdf2_hmac('sha256', password.encode('utf-8'),
                                       encryption_salt_hex.hexdigest().encode('utf-8'), iterators)

        # store the value returned in the database
        return self.caveman_crypt_2_0(password_encrypt.hex(), encryption_salt_hex.hexdigest())
