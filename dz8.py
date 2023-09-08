import time
import logging

logging.basicConfig(filename="timing.log", level=logging.INFO, filemode="w")


def timer(funct):
    start_time = time.time()
    res = funct()
    end_time = time.time()
    exect_time = end_time - start_time
    logging.info(f"Функція '{funct.__name__}' виконана за {exect_time} секунд")
    return res, exect_time


def sleep():
    time.sleep(2)
    return "<result>"


result, execution_time = timer(sleep)
print(f"Результат: {result}")
print(f"Час виконання: {int(execution_time)} секунд")
