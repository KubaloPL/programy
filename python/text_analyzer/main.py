"""
Stwórz program, który analizuje tekst i zapisuje wyniki do pliku logów.
1. Stwórz moduł text_analysis z funkcjami:
    word_count (zlicza liczbę słów),
    unique_words (zwraca listę unikalnych słów).
Wykorzystaj klasy do obsługi danych wejściowych i logowania wyników.
"""

import text_analysis as analyzer
import logging

LOG_FILE = "text_analyzer.log"

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger("User_Manager")

class TextAnalyzer:
    def __init__(self, string: str):
        self.string = string
        self.word_count = analyzer.word_count(string)
        self.unique_words = analyzer.unique_words(string)

if __name__ == "__main__":
    analyzer = TextAnalyzer("test test test xd")
