


class Delay:
    def __init__(self, max_delay):
        """
        Tworzy obiekt kasy Delay.
        :param max_delay: maksymalna liczba próbek do opóźnienia
        """
        self._buffer = [0.0] * max_delay #prywatny buffor delay
        self._max_delay = max_delay
        self._index = 0

    def process(self, x):
        """
        Dodaje nową próbkę i zwaca próbkę opźnioną.
        :param x: aktualna próbka wejściowa
        :return: próbka wyjściowa opóźniona.
        """
        y = self._buffer[self._index] # zwróć starą wartość
        self._buffer[self._index] = x # wstaw nową próbkę
        self._index = (self._index + 1) % self._max_delay
        return y



if __name__ == "__main__":
    # Testowanie klasy Delay
    delay_samples = 3
    delay = Delay(delay_samples)

    input_signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    output_signal = []

    print("Test opóźnienia sygnału o", delay_samples, "próbki")
    for sample in input_signal:
        y = delay.process(sample)
        output_signal.append(y)
        print(f"Input: {sample} -> Output: {y}")

    print("Ostateczny sygnał wyjściowy: ", output_signal)
    print("testaa")