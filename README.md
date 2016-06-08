# Experiments-in-Music
An exploration in machine-assisted musical composition.

# Installation
See using Character RNN model implemented in Tensor Flow from https://github.com/sherjilozair/char-rnn-tensorflow


# Dataset
All jigs in D minor (in 6/8 time) from The Nottingham Collection, with some preliminary data cleaning. Songs begin with a %.

Raw data: http://abc.sourceforge.net/NMD/nmd/jigs.txt


# Sampling
I modified the character generation step in two ways:
- Forcing the model to continue writing a song without the new song character '%'
- Iterating back and forth between two models (128 nodes & 256 nodes respectively), the smaller one which is "creative" and the bigger one potentially overfit (hence it is not allowed to write too many characters in a row, but it is really good at injecting parts from other tunes coherently)
