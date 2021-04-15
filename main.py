import argparse
import utils as utils
from Artcoder import artcoder

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--style_img_path', help="path to input style target (default: './style/texture1.1.jpg')", type=str,
                        default='./style/texture1.1.jpg')
    parser.add_argument('--content_img_path', help="path to input content target (default: './content/boy.jpg')", type=str,
                        default='./content/boy.jpg')
    parser.add_argument('--code_img_path', help="path to input code target (default: './code/boy.jpg')", type=str,
                        default='./code/boy.jpg')
    parser.add_argument('--output_dir', help='path to save output stylized QR code', type=str,
                        default='./output/')
    parser.add_argument('--learning_rate',
                        help='learning rate (default: 0.01)',
                        type=int, default=0.01)
    parser.add_argument('--style_weight', help='style_weight', type=int, default=1e15)
    parser.add_argument('--content_weight', help='content_weight', type=int, default=1e8)
    parser.add_argument('--code_weight', help='code_weight', type=int, default=1e12)

    parser.add_argument('--module_size',
                        help='the resolution of each square module of a QR code (default: 16)',
                        type=int, default=16)
    parser.add_argument('--module_number',
                        help='Number of QR code modules per side (default: 37)',
                        type=int, default=37)
    parser.add_argument('--epoch', help='epoch number (default: 20000)', type=int,
                        default=50000)
    parser.add_argument('--discriminate_b',
                        help="for black modules, pixels' gray values under discriminate_b will be discriminated to error modules to activate sub-code-losses (discriminate_b in [0-128])",
                        type=int,
                        default=70)
    parser.add_argument('--discriminate_w',
                        help="for white modules, pixels' gray values over discriminate_w will be discriminated to error modules to activate sub-code-losses (discriminate_w in [128-255])",
                        type=int,
                        default=180)
    parser.add_argument('--correct_b',
                        help="for black module, correct error modules' gray value to correct_b (correct_b < discriminate_b)",
                        type=int,
                        default=40)
    parser.add_argument('--correct_w',
                        help="for white module, correct error modules' gray value to correct_w (correct_w > discriminate_w)",
                        type=int,
                        default=220)
    parser.add_argument('--use_activation_mechanism',
                        help="whether to use the activation mechanism (1 means use and other numbers mean not)",
                        type=int,
                        default=1)

    args = parser.parse_args()
    utils.print_options(opt=args)

    artcoder(STYLE_IMG_PATH=args.style_img_path, CONTENT_IMG_PATH=args.content_img_path, CODE_PATH=args.code_img_path,
             OUTPUT_DIR=args.output_dir, LEARNING_RATE=args.learning_rate, CONTENT_WEIGHT=args.content_weight,
             STYLE_WEIGHT=args.style_weight, CODE_WEIGHT=args.code_weight, MODULE_SIZE=args.module_size,
             MODULE_NUM=args.module_number, EPOCHS=args.epoch, Dis_b=args.discriminate_b, Dis_w=args.discriminate_w,
             Correct_b=args.correct_b, Correct_w=args.correct_w, USE_ACTIVATION_MECHANISM=args.use_activation_mechanism)
