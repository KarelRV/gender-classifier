import pandas
import pickle
import re
import gzip

def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')


def read_model():
    """
    Reads the classifier model from a pickle file
    :param filename: name of the file
    :return: a model for running gender redictions on
    """

    file = gzip.open("data.tar.gz", 'rb')
    model = pickle.load(file)
    file.close()
    return model


def convert_to_six_digits(name):
    """
    Converts the a name into a six digit representation to run on the predictor
    :param name: a string of a customers name or email prefix
    :return: a 6 digit string representing the nam
    """
    name = name.lower()

    if len(name) == 0:
        return "unkown"
    elif len(name) == 1:
        return name * 6
    elif len(name) == 2:
        return name * 3
    else:
        return name[0:3] + name[-3:]


def one_hot_encode(name):
    """
    One hot encodes a six digit name into a binary vector
    :return: a 1x156 vector, each 26 vectors is one hot encoded to represent that letter
    """
    one_hot_encoded = []
    for ltr in name:
        one_hot_encoded += [1 if i == ord(ltr) else 0 for i in range(97, 123)]
    return one_hot_encoded


def predict(name):
    """
    Converts a name into a one hot encoded 6 character length vector
    :param name: a string of a persons name or email prefix
    :return: a gender prediction for the name as a string "MALE" or "FEMALE"
    """
    genders = ["FEMALE", "MALE"]
    if '@' in name:
        name = name[:name.find("@")]
    name = convert_to_six_digits(name)
    name = one_hot_encode(name)
    return genders[model.predict([name])[0]]