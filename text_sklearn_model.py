import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy.typing import NDArray

BASE_TOL: float = 1e-6

def read_file(path: str) -> str:
    with open(path) as f:
        return f.read()

class TextModel:
    def __init__(self, text: str, tolerance: float = BASE_TOL):
        self.tol = tolerance
        self.__build_model(text)

    def __build_model(self, text: str) -> None:
        self.__vectorizer = TfidfVectorizer()
        self.__sentences = [s for s in text.split('.')]
        self.__model = self.__vectorizer.fit_transform(self.__sentences)
    
    def get_feature_names_out(self) -> NDArray:
        return self.__vectorizer.get_feature_names_out()

    def getAnswers(self, question: str, nAnswers: int = 1) -> list[str]:
        question_vector = self.__vectorizer.transform([question])
        similarities = cosine_similarity(self.__model, question_vector).ravel()
        ind_sort = np.argsort(similarities)
        
        return [self.__sentences[ind_sort[-j]]
                for j in range(1, nAnswers + 1) if similarities[ind_sort[-j]] > self.tol]
        
    

if __name__ == "__main__":
    text = read_file("tortoise_and_a_hare.txt")
    model = TextModel(text)
    print(model.get_feature_names_out())
    for x in model.getAnswers("Why did the hare agree to the proposal", 3):
        print(x)