import random
import numpy as np

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class NeuralNetwork:
    def __init__(self,a,b,c):
        self.input_neurons = a
        self.hidden_neurons = b
        self.output_neurons = c
        self.weights_ih = np.random.rand(self.hidden_neurons,self.input_neurons) #is <0;1> should be <-1;1> or just change weights to be <-1;1>
        self.weights_ho = np.random.rand(self.output_neurons,self.hidden_neurons) #is <0;1> should be <-1;1> or just change weights to be <-1;1>
        self.bias_h= np.random.rand(self.hidden_neurons)
        self.bias_o= np.random.rand(self.output_neurons)
    def feedforward(self,input):
        print("weights")
        print(self.weights_ih)
        print("input")
        print(input)
        self.hidden = np.matmul(self.weights_ih,input)
        print("input x weights")
        print(self.hidden)
        self.hidden = np.add(self.bias_h,self.hidden)
        print("bias")
        print(self.bias_h)
        print("input x weights + bias")
        print(self.hidden)
        self.hidden = np.array(map(sigmoid, self.hidden))
        print("map")
        print(self.hidden)
        self.output = np.matmul(self.weights_ho,self.hidden)
        self.output = np.add(self.bias_h,self.output)
        print("output")
        print(self.output)
        self.output = np.array(map(sigmoid,self.hidden))
        return self.output
nn = NeuralNetwork(3,2,1)

input = [1,2,3]

output = nn.feedforward(input);
print("final output")
print(output[1])
