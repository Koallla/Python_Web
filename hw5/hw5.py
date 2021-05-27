from time import time, sleep


# def factorize(number):
#     sleep(1)
#     print('Start')
#     result = []
#     for n in range(1, number + 1):
#         if number % n == 0:
#             result.append(n)

#     return result


# start = time()


# # a, b, c, d  = factorize(128, 255, 99999, 10651060)

# a = factorize(128)
# b = factorize(255)
# c = factorize(99999)
# d = factorize(10651060)



# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

# print(time() - start)

# ====================================================================================
# With Pool
from multiprocessing import Pool


def factorize(number):
    # sleep(1)
    print('Start')
    result = []
    for n in range(1, number + 1):
        if number % n == 0:
            result.append(n)
    return result

args = [128, 255, 99999, 10651060]

if __name__ == '__main__':
    start = time()

    with Pool() as pool:
        a, b, c, d = pool.map(factorize, args)

    print(time() - start)


    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]




# =================================================================================================
# With ProcessPoolExecutor

# import concurrent.futures

# start = time()
# def factorize(number):
#     result = []
#     number_list = [num for num in range(1, number + 1)]
#     for n in number_list:
#         if number % n == 0:
#             result.append(n)

#     return result

# args = [128, 255, 99999, 10651060]

# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(factorize, args)


#     # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#     # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#     # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#     # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


# print(time() - start)

# ========================================================================

# from datetime import datetime
# from multiprocessing import Process, Pipe


# def count_divisors(number, pipe):

#     number_result = []
#     for j in range(1, number+1):
#         if not number%j:
#             number_result.append(j)
#     pipe.send(number_result)

# def factorize(*number):

#     print('Start')
#     entered_numbers = number
#     results = []
#     processes = []
#     pipe_receiver = []
#     pipe_sender = []
    
#     for i in entered_numbers:
#         pipe_receiver.append(0)
#         pipe_sender.append(0)
#         pipe_receiver[-1], pipe_sender[-1] = Pipe()
#         processes.append(Process(target = count_divisors, args = (i,pipe_sender[-1])))
#         processes[-1].start()
    
#     for i in range(len(entered_numbers)):
#         results.append(pipe_receiver[i].recv())

#     return results

# if __name__ == '__main__':

#     start = time()
        
#     a, b, c, d  = factorize(128, 255, 99999, 10651060)



#     print(time() - start)
#     assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#     assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#     assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#     assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
