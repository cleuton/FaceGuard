from flask import Flask, request
from flask_restful import Resource, Api    
import sys
from align import align_dataset_mtcnn
import classifier

def process():
    retorno = True
    args = {
        'input_dir' : './serverutil/uploads',
        'output_dir' : './serverutil/processadas',
        'image_size' : 160,
        'margin': 32,
        'random_order': True,
        'gpu_memory_fraction': 0.25,
        'detect_multiple_faces': False
    }
    align_dataset_mtcnn.align(args)
    #python classifier.py CLASSIFY ./serverutil/processadas /Users/cleuton/localprojs/FaceNet/20170512-110547/20170512-110547.pb /Users/cleuton/localprojs/FaceNet/20170512-110547/my_classifier.pkl --batch_size 1000
    argsClassif = {
        'mode': 'CLASSIFY',
        'data_dir': './serverutil/processadas',
        'model' : '/Users/cleuton/localprojs/FaceNet/20170512-110547/20170512-110547.pb',
        'use_split_dataset': False,
        'test_data_dir': '',
        'batch_size': 1000,
        'image_size': 160,
        'seed': 666,
        'min_nrof_images_per_class': 1,
        'nrof_train_images_per_class': 1,
        'classifier_filename': '/Users/cleuton/localprojs/FaceNet/20170512-110547/my_classifier.pkl'
    }
    retorno = classifier.process_image(argsClassif)
    print('Retorno do classifier: ', retorno)
    return retorno
