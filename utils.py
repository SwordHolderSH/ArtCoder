import torch
from PIL import Image
import os
import numpy as np
import math
import pandas as pd
from torchvision import transforms
import shutil

unloader = transforms.ToPILImage()
load = transforms.ToTensor()


def load_image(filename, size=None, scale=None):
    img = Image.open(filename)
    if size is not None:
        img = img.resize((size, size), Image.ANTIALIAS)
    elif scale is not None:
        img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)), Image.ANTIALIAS)
    return img


def add_pattern(target_PIL, code_PIL, module_number=37, module_size=16):
    target_img = np.asarray(target_PIL)
    code_img = np.array(code_PIL)
    output = target_img
    output = np.require(output, dtype='uint8', requirements=['O', 'W'])
    ms = module_size  # module size
    mn = module_number  # module_number
    output[0 * ms:(8 * ms) - 1, 0 * ms:(8 * ms) - 1, :] = code_img[0 * ms:(8 * ms) - 1, 0 * ms:(8 * ms) - 1, :]
    output[((mn - 8) * ms) + 1:(mn * ms), 0 * ms:(8 * ms) - 1, :] = code_img[((mn - 8) * ms) + 1:(mn * ms),
                                                                    0 * ms:(8 * ms) - 1,
                                                                    :]
    output[0 * ms: (8 * ms) - 1, ((mn - 8) * ms) + 1:(mn * ms), :] = code_img[0 * ms: (8 * ms) - 1,
                                                                     ((mn - 8) * ms) + 1:(mn * ms), :]
    output[28 * ms: (33 * ms) - 1, 28 * ms:(33 * ms) - 1, :] = code_img[28 * ms: (33 * ms) - 1, 28 * ms:(33 * ms) - 1,
                                                               :]

    output = Image.fromarray(output.astype('uint8'))
    print('Added finder and alignment patterns.')
    return output


def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def gram_matrix(y):
    (b, ch, h, w) = y.size()
    features = y.view(b, ch, w * h)
    features_t = features.transpose(1, 2)
    gram = features.bmm(features_t) / (ch * h * w)
    return gram


def get_action_matrix(img_target, img_code, module_size=16, IMG_SIZE=592, Dis_b=50, Dis_w=200):
    img_code = np.require(np.asarray(img_code.convert('L')), dtype='uint8', requirements=['O', 'W'])
    img_target = np.require(np.array(img_target.convert('L')), dtype='uint8', requirements=['O', 'W'])

    ideal_result = get_binary_result(img_code, module_size)
    center_mat = get_center_pixel(img_target, module_size)
    error_module = get_error_module(center_mat, code_result=ideal_result,
                                    threshold_b=Dis_b,
                                    threshold_w=Dis_w)
    return error_module, ideal_result


def get_binary_result(img_code, module_size, module_number=37):
    binary_result = np.zeros((module_number, module_number))
    for j in range(module_number):
        for i in range(module_number):
            module = img_code[i * module_size:(i + 1) * module_size, j * module_size:(j + 1) * module_size]
            module_color = np.around(np.mean(module), decimals=2)
            if module_color < 128:
                binary_result[i, j] = 0
            else:
                binary_result[i, j] = 1
    return binary_result


def get_center_pixel(img_target, module_size):
    center_mat = np.zeros((37, 37))
    for j in range(37):
        for i in range(37):
            module = img_target[i * module_size:(i + 1) * module_size, j * module_size:(j + 1) * module_size]
            module_color = np.mean(module[5:12, 5:12])
            center_mat[i, j] = module_color
    return center_mat


def get_error_module(center_mat, code_result, threshold_b, threshold_w):
    error_module = np.ones((37, 37))  # 0 means correct,1 means error
    for j in range(37):
        for i in range(37):
            center_pixel = center_mat[i, j]
            right_result = code_result[i, j]
            if right_result == 0 and center_pixel < threshold_b:
                error_module[i, j] = 0
            elif right_result == 1 and center_pixel > threshold_w:
                error_module[i, j] = 0
            else:
                error_module[i, j] = 1
    return error_module


def get_target(binary_result, b_robust, w_robust, module_num=37, module_size=16):
    img_size = module_size * module_num
    target = np.require(np.ones((img_size, img_size)), dtype='uint8', requirements=['O', 'W'])

    for i in range(module_num):
        for j in range(module_num):
            # print(str(i) + ' == ' + str(j))
            one_binary_result = binary_result[i, j]
            if one_binary_result == 0:
                target[i * module_size:(i + 1) * module_size, j * module_size:(j + 1) * module_size] = b_robust
            else:
                target[i * module_size:(i + 1) * module_size, j * module_size:(j + 1) * module_size] = w_robust

    target = load(Image.fromarray(target.astype('uint8')).convert('RGB')).unsqueeze(0).cuda()
    return target


def save_image_epoch(tensor, path, name, code_pil, addpattern=True):
    """Save a single image."""
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)
    if addpattern == True:
        image = add_pattern(image, code_pil, module_number=37, module_size=16)
    image.save(os.path.join(path, "epoch_" + str(name)))


def tensor_to_PIL(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)
    return image


def get_3DGauss(s=0, e=15, sigma=1.5, mu=7.5):
    x, y = np.mgrid[s:e:16j, s:e:16j]
    z = (1 / (2 * math.pi * sigma ** 2)) * np.exp(-((x - mu) ** 2 + (y - mu) ** 2) / (2 * sigma ** 2))
    z = torch.from_numpy(MaxMinNormalization(z.astype(np.float32)))
    for j in range(16):
        for i in range(16):
            if z[i, j] < 0.1:
                z[i, j] = 0
    return z


def MaxMinNormalization(loss_img):
    maxvalue = np.max(loss_img)
    minvalue = np.min(loss_img)
    img = (loss_img - minvalue) / (maxvalue - minvalue)
    img = np.around(img, decimals=2)
    return img


def print_options(opt):
    """Print and save options
    It will print both current options and default values(if different).
    It will save options into a text file / [checkpoints_dir] / opt.txt
    """
    message = ''
    message += '----------------- Options ---------------\n'
    for k, v in sorted(vars(opt).items()):
        comment = ''
        message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
    message += '----------------- End -------------------'
    print(message)
