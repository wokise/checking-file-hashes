import hashlib
import os
import sys
import codecs


if __name__ == '__main__':
    BLOCKSIZE = 65536

    if len(sys.argv) != 3:
        raise Exception("An error occured: Invalid number of arguments specified!")
    else:
        file_path = sys.argv[1]
        dir_path = sys.argv[2]

        if not os.path.exists(file_path):
            raise Exception("An error occured: An error occurred: the path to a non-existent file was specified!")

        with codecs.open(file_path, 'r', 'utf-8') as f:
            file_data = f.readlines()

        for line in file_data:
            values = line.split()
            if len(values) != 3:
                raise Exception("An error occured: the specified file does not match the set format!")

            file_name = values[0]
            file_path = os.path.join(dir_path, file_name)
            if not os.path.exists(file_path):
                print(file_name, 'NOT FOUND')
            else:

                hash_type = values[1]
                hash_value = values[2]

                md5 = hashlib.md5()
                sha1 = hashlib.sha1()
                sha256 = hashlib.sha256()

                with codecs.open(file_path, 'rb') as f2:
                    file_buffer = f2.read(BLOCKSIZE)
                    while len(file_buffer) > 0:
                        md5.update(file_buffer)
                        sha1.update(file_buffer)
                        sha256.update(file_buffer)
                        file_buffer = f2.read(BLOCKSIZE)

                if hash_type == 'md5':
                    hash_sum = md5.hexdigest()
                elif hash_type == 'sha1':
                    hash_sum = sha1.hexdigest()
                elif hash_type == 'sha256':
                    hash_sum = sha256.hexdigest()
                else:
                    raise Exception("An error occured: incorrect hashing algorithm specified!")

                if hash_sum == hash_value:
                    print(file_name, 'OK')
                else:
                    print(file_name, 'FAIL')