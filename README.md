# A simple neural network with Numpy
Develop and run a basic neural network with Numpy for simplicity and performance. The network is a simple perceptron with 1 input layer and 1 output neuron.


## Logic

If the first input is 1, the output neuron should be activated.


## The maths

Implementing a Sigmoid activation function to normalize the sum of the weights.

![alt text](https://github.com/adrienfunel/neural-network/blob/main/images/activation.jpg?raw=true)
Nb: the bias is intentionally overlooked in the code.

The network then uses the derivative of the sigmoid to calculate the gradient of the Sigmoid curve and make adjustments to the neurons.

![alt text](https://github.com/adrienfunel/neural-network/blob/main/images/layers.jpg?raw=true)


## Docs and credits

Helpful documentation:
https://iamtrask.github.io/2015/07/12/basic-python-network/

[Image credits](https://medium.com/coinmonks/the-mathematics-of-neural-network-60a112dd3e05)