class IIRFilter:
    def __init__(self, b, a):
        """
        Tworzy obiekt filtra IIR
        :param b: współczynniki dla licznika
        :param a: współczynniki dla mianownika
        """

        self._b = b
        self._a = a

        self._x_history = [0.0] * len(b)
        self._y_history = [0.0] * len(a)

    def process(self, x):
        """
        Przetwarza jedną póbkę przez filtr
        :param x: aktualna próbka wejściowa
        :return: przefiltrowana próbka wyjściowa
        """
        self._x_history = [x] + self._x_history[:-1]

        y = 0.0

        # część feedforward
        for i in range(len(self._b)):
            y += self._b[i] * self._x_history[i]

        for i in range(1, len(self._a)):
            y -= self._a[i] * self._y_history[i]

        # normalizacja przez a[0]
        y = y / self._a[0]

        # Przesuń historię wyjścia
        self._y_history = [y] + self._y_history[:-1]

        return y

if __name__ == "__main__":
    b = [0.25, 0.25, 0.25, 0.25]
    a = [1.0]

    filt = IIRFilter(b, a)

    input_signal = [1, 0,0,0,0,0,0,0,0,0,0,0]
    output_signal = []

    print("Test filtra IIR: ")
    for sample in input_signal:
        y = filt.process(sample)
        output_signal.append(y)
        print(f"Input: {sample} -> Output: {y:.4f}")

    print("Wyjście:" , output_signal)




