from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

import re

def main():
    # List of models to interact
    models = ['store512', 'store256', 'store512', 'store256', 'store512', 'store256']
    # Number of characters each model gets to produce
    voice = [5, 10, 10, 20, 15, 20]    

    # Build music string
    # Initial primer is the new song character
    music = 'D'

    # For x iterations, let different models write music and prime each other
    x = 100
    for i in range(0, x):
	music = sample(directory=models[i%len(models)], prime=music, loop=0, length=voice[i%len(models)])
	print ('Song so far: ' + music)
        print ('')

    music = 'X:1\nM:6/8\nK:D\n' + music
    with open('test/music.abc', 'w') as newfile:
    	newfile.write(music)

    print ('Done')

def sample(directory, prime, loop, length):
    tf.reset_default_graph()
    with open(os.path.join(directory, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(directory, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, infer=True, loop=loop)

    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(directory)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

	    # Limit sample length in hopes of obtaining only enough
            # Force song to continue
            music = model.sample(sess, chars, vocab, length, prime, 1, force=True)
            return music

if __name__ == '__main__':
    main()
