import os
import os.path
import random

def main():
    IMAGE_ROOT = 'MY/'

    # ===== write training txt =====
    TRAIN_TXT_FILE = 'train.txt'
    ftrain = open(TRAIN_TXT_FILE, 'w')
    train_all = []

    train_fire = os.listdir(IMAGE_ROOT+'train/Fire')
    for file_name in train_fire:
        train_all.append(file_name+' 1')

    train_safe = os.listdir(IMAGE_ROOT+'train/Safe')
    for file_name in train_safe:
        train_all.append(file_name+' 0')

    shuff_ind = [x for x in range(0, len(train_all))]
    random.shuffle(shuff_ind)
    for i in shuff_ind:
        ftrain.write(train_all[i] + '\n')

    ftrain.close()

    # ===== write validation txt =====
    VAL_TXT_FILE = 'val.txt'
    fval = open(VAL_TXT_FILE, 'w')
    val_all = []

    val_fire = os.listdir(IMAGE_ROOT + 'valid/Fire')
    for file_name in val_fire:
        val_all.append(file_name+' 1')

    val_safe = os.listdir(IMAGE_ROOT + 'valid/Safe')
    for file_name in val_safe:
        val_all.append(file_name+' 0')

    shuff_ind = [x for x in range(0, len(val_all))]
    random.shuffle(shuff_ind)
    for i in shuff_ind:
        fval.write(val_all[i] + '\n')

    fval.close()

    # ===== write testing txt =====
    TEST_TXT_FILE = 'test.txt'
    ftest = open(TEST_TXT_FILE, 'w')
    test_all = []

    test_fire = os.listdir(IMAGE_ROOT + 'test/Fire')
    for file_name in test_fire:
        test_all.append(file_name + ' 1')

    test_safe = os.listdir(IMAGE_ROOT + 'test/Safe')
    for file_name in test_safe:
        test_all.append(file_name + ' 0')

    shuff_ind = [x for x in range(0, len(test_all))]
    random.shuffle(shuff_ind)
    for i in shuff_ind:
        ftest.write(test_all[i] + '\n')

    ftest.close()

if __name__ == '__main__':
    main()
