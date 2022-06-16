# Before running this, you will have to run make_pathfile.py to create an images.txt list file with all the images.

# Feature Extraction
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty08.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty08/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty09.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty09/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty10.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty10/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty11.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty11/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty12.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty12/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty13.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty13/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty14.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty14/images.txt
#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty15.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/lfw_align_112_png_beauty15/images.txt

#python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/lfw_align_112_png_beauty_random_final.list --inf_list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_random_final/images.txt

# Evaluation
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty08.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty09.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty10.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty11.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty12.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty13.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty14.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy
python3 eval/eval_recognition/eval_1v1.py --feat-list /home/bill/code/face_recognition/magface/features/magface_iresnet100/lfw_align_112_png_beauty15.list --pair-list /mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter/issame.npy

# python3 eval/eval_recognition/eval_1v1.py --feat-list features/magface_iresnet100/lfw_align_112_png_beauty15.list --pair-list /mnt/c/Users/Bill/Desktop/issame.npy

# for gaussian2, gaussia3, pixelation use this
python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/fairfaces_val_gaussian_2_00.list --inf_list /mnt/c/Users/Bill/Desktop/fairfaces_val_gaussian_2/00/images.txt

# for fairfaces and fairbeauty use this because we need resized images 
python3 inference/gen_feat.py --arch iresnet100 --resume models/magface_epoch_00025.pth --feat_list features/magface_iresnet100/fairfaces_val_00.list --inf_list /mnt/c/Users/Bill/Desktop/fairfaces_val_112/00/images.txt