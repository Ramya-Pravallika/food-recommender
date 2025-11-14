from gensim.models import Word2Vec


def train_item2vec(sequences, vector_size=32, window=5, min_count=1, epochs=10):
    # sequences: list of lists of string ids
    model = Word2Vec(sentences=sequences, vector_size=vector_size, window=window, min_count=min_count, sg=1, workers=4)
    model.train(sequences, total_examples=len(sequences), epochs=epochs)
    return model


def save_model(model, path='models/item2vec.model'):
    model.save(path)


def load_model(path='models/item2vec.model'):
    return Word2Vec.load(path)
