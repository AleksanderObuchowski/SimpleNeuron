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
        self.weights_ih = np.random.rand(self.hidden_neurons,self.input_neurons) #is <0;1> should be <-1;1>
        self.weights_ho = np.random.rand(self.output_neurons,self.hidden_neurons) #is <0;1> should be <-1;1>
        self.bias_h= np.random.rand(self.hidden_neurons)
        self.bias_o= np.random.rand(self.output_neurons)
    def feedforward(self,input):
        #print("weights")
        #print(self.weights_ih)
        #print("input")
        #print(input)
        self.hidden = np.matmul(self.weights_ih,input)
        #print("input x weights")
        #print(self.hidden)
        self.hidden = np.add(self.bias_h,self.hidden)
        #print("bias")
        #print(self.bias_h)
        #print("input x weights + bias")
        #print(self.hidden)
        self.hidden = np.array(map(sigmoid, self.hidden))
        #print("map")
        #print(self.hidden)
        #print("weights h --> o")
        #print(self.weights_ho)
        self.hidden = np.resize(self.hidden,(self.hidden_neurons,1))
        #print("resize")
        #print(self.hidden)
        self.output = np.matmul(self.weights_ho,self.hidden)
        #print("output")
        #print(self.output)
        self.output = np.add(self.bias_o,self.output)
        #print("output")
        #print(self.output)
        self.output = np.array(map(sigmoid,self.output))
        return self.output

    def train(self,inputs,targets):
        self.outputs = self.feedforward(inputs)
        print("outputs")
        print(self.outputs)
        print("targets")
        print(targets)
        self.output_errors = np.subtract(targets,self.outputs)
        print("error")
        print(self.output_errors)
        print(self.weights_ho)
        self.weights_ho2 = self.weights_ho.copy()
        self.weights_ho2= self.weights_ho2.transpose()
        self.hidden_errors = np.matmul(self.weights_ho2,self.output_errors)
        print(self.weights_ho2)
        print(self.hidden_errors)
        #self.hidden_errors = _______
nn = NeuralNetwork(2,2,1)

input = [2,2]
target = [0]
output = nn.feedforward(input);
#print("final output")
print(output)
nn.train(input,target)
