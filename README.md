# Experiments-in-Music
An exploration in machine-assisted musical composition.


# Installation and Usage
This project uses the Character RNN model implemented in Tensor Flow by Sherjil Ozair: https://github.com/sherjilozair/char-rnn-tensorflow


# Dataset
The Nottingham Collection: http://abc.sourceforge.net/NMD/nmd/jigs.txt

Please see the ABC Notation section below for more information.

# Pre-processing

I chose to focus only on Jigs that are in D minor to make it easier to train the network. 

The code assumes a new song begins with the character '%', which can be achieved easily from the raw data by replacing "X: #".

# Sampling During Generation
I modified the character generation step in two ways:

1. Forcing the model to continue writing a song without the new song character defined by me to be '%'

2. Iterating back and forth between two models (256 nodes & 512 nodes respectively)
 
The smaller one is "creative" but struggles to write long passages.
The bigger one is very good at borrowing concepts from tunes coherently, thus preserving musical structure.


# Similar Projects

- Equivalent dataset: https://maraoz.com/2016/02/02/abc-rnn/
- Interesting blog on machine-assisted composition: https://highnoongmt.wordpress.com/2015/08/15/deep-learning-for-assisting-the-process-of-music-composition-part-4/
- Another implementation: http://yoavz.com/music_rnn/

# ABC Notation

- It may help to read this tutorial: http://www.lesession.co.uk/abc/abc_notation.htm

- To convert ABC to MIDI: use abc2midi for conversion and timidity for playing

installation (linux): $ sudo apt-get install abcmidi timidity

conversion:           $ abc2midi music.abc -o music.mid 

playing music:        $ timidity music.mid
