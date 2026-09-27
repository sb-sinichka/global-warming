from model import detect, init_model


init_model('model/keras_model.h5','model/labels.txt')
print(detect('dataset/plastic/plastic1.jpg'))