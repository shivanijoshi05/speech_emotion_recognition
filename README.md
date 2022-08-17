Speech Emotion Recognition -

SER basically recognizes the emotional aspects of human speech. Emotion detection and its analysis have vital importance in today's digital world of remote communication. This system will predict various human emotions from their speech. Here we will be using Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) dataset containing audio files that would help in training the model.

Tools and Software used:
Librosa, 
HTML, 
Keras, 
VGG-19, 
Flask

We trained our model using VGG16 and VGG19 out of which, VGG19 gave higher accuracy for which 70 epochs were given for training. The training accuracy of this model was 92.14% and the validation accuracy was 85.62%. The overall accuracy obtained was 86%. 


In this system, the model that we built is deployed on web application that we created with the help of Flask and HTML. The user can upload an audio file as an input to the website to which the model applies the algorithm and predicts the emotion of the input audio file as an output.
Hence, this way our web application produces the output which recognizes the emotion from speech.

Authors : 
Dhruvi Dhapre, Khushi Kamat, Shivani Joshi, Khushbu Modi
