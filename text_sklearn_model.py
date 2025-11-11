import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class TextModel:
    def __init__(self, text: str):
        self.__build_model()

    def __build_model(self) -> None:
        pass

    def getAnswers(self, question: str, nAnswers: int = 1) -> list[str]:
        return []