# Experiments-in-Music
An exploration in machine-assisted musical composition.

# Installation
See using Character RNN model implemented in Tensor Flow from https://github.com/sherjilozair/char-rnn-tensorflow


# Dataset
All jigs in D minor (in 6/8 time) from The Nottingham Collection, with some preliminary data cleaning. Songs begin with a %.

Raw data: http://abc.sourceforge.net/NMD/nmd/jigs.txt


# Sampling
I modified the character generation step in two ways:

1. Forcing the model to continue writing a song without the new song character '%'

2. Iterating back and forth between two models (128 nodes & 256 nodes respectively)
- The smaller one is "creative" but struggles to write long passages
- The bigger one is overfit to the data and thus is limited from writing too many characters in a row. It is very good at borrowing parts from other tunes coherently.


# Similar Projects

- https://maraoz.com/2016/02/02/abc-rnn/
- http://yoavz.com/music_rnn/

# ABC Notation

- May help to read this: http://www.lesession.co.uk/abc/abc_notation.htm
- To convert ABC to MIDI: use abc2midi for conversion and timidity for playing
install: $ sudo apt-get install abcmidi timidity
convert: $ abc2midi music.abc -o music.mid 
play: $ timidity music.mid
