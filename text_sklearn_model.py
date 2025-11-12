import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_TOL: float = 1e-6

def read_file(path: str) -> str:
    with open(path) as f:
        return f.read()

class TextModel:
    def __init__(self, text: str, tolerance: float = BASE_TOL):
        self.tol = tolerance
        self.__vectorizer = TfidfVectorizer()
        self.__build_model(text)

    def __build_model(self, text: str) -> None:
        self.__sentences = [s.strip() for s in text.split('.')]
        self.__model = self.__vectorizer.fit_transform(self.__sentences)

    def getAnswers(self, question: str, nAnswers: int = 1) -> list[str]:
        question_vector = self.__vectorizer.transform([question])
        similarities = cosine_similarity(self.__model, question_vector).ravel()
        print(similarities)
        ind_sort = np.argsort(-similarities)
        print(ind_sort)
        print(ind_sort.shape)
        
        reply = [self.__sentences[ind_sort[j]]
                for j in range(nAnswers) if similarities[ind_sort[j]] > self.tol]
        print(reply)
        return reply
    

if __name__ == "__main__":
    text = read_file("tortoise_and_a_hare.txt")
    model = TextModel(text)
    for x in model.getAnswers("Why did the hare agree to the proposal", 2):
        print(x)