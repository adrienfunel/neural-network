import numpy as np
from app import NeuralNetwork
from time import perf_counter


def main():
    # Initialize the single neuron neural network
    neural_network = NeuralNetwork()

    print(f"Random starting synaptic weights: {neural_network.synaptic_weights}")

    # The training set, with 4 examples consisting of 3
    # input values and 1 output value
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 10000)

    print(f"Synaptic weights after training: {neural_network.synaptic_weights}")

    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))

    print("New situation: input data = ", A, B, C)
    print(f"Output data: {neural_network.test(np.array([A, B, C]))}")


if __name__ == "__main__":
    start = perf_counter()

    main()

    end = perf_counter()
    elapsed = end - start
    print(f"Elapsed time in seconds {elapsed:0.2f}")
