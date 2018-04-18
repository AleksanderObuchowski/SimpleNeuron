

import numpy
import scipy.special



class NeuralNetwork:
    def __init__(self,nodes,learningrate):

        self.bias = "True"
        self.nodes = nodes
        self.lr = learningrate
        self.activation_function = lambda x:scipy.special.expit(x)


        #if there is a bias we treat it as input with value of 1 so we need to add one neuron to first layer

        if(self.bias):
            nodes[0]+=1

        #initializing weights
        self.weights = []
        for i in range(0,len(self.nodes)-1):
            self.weights.append(numpy.random.rand(self.nodes[i+1],self.nodes[i])-0.5)





    def train(self,inputs_list,targets_list):

        #if there is bias we add input with value "1"

        if (self.bias):
            inputs_list.append(1)



        self.outputs = []

        # convert inputs list to 2d array

        self.outputs.append(numpy.array(inputs_list, ndmin=2).T)

        #feed forward

        for i in range(1,len(self.weights)+1):
            self.outputs.append(self.activation_function(numpy.dot(self.weights[i-1],self.outputs[i-1])))


        # converting targets into 2d array
        targets = numpy.array(targets_list,ndmin=2).T

        #declaring errors table

        self.errors = []

        #adding errors of last layer to the errors table

        self.errors.append(targets - self.outputs[-1])

        #Using backpropagation to fill the errors table

        for i in range(1,len(self.weights)):
            self.errors.append(numpy.dot(self.weights[-i].T, self.errors[i-1]))

        #Updating weights

        for i in range(1,len(self.weights)+1):
            self.weights[-i] += self.lr*numpy.dot((self.errors[i-1]*self.outputs[-i]*(1.0 - self.outputs[-i])),numpy.transpose(self.outputs[-i-1]))





    def predict(self,inputs_list):

        #if there is bias we add input with value "1"

        if (self.bias):
            inputs_list.append(1)

        #converting inputs to 2D vertical array
        self.outputs = []
        self.outputs.append(numpy.array(inputs_list, ndmin=2).T)

        #feed forward
        for i in range(1,len(self.weights)+1):
            self.outputs.append(self.activation_function(numpy.dot(self.weights[i-1],self.outputs[i-1])))

        #returning last layer as output
        return self.outputs[-1]
