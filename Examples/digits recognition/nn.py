

import numpy
import scipy.special



class NeuralNetwork:
    def __init__(self,nodes,learningrate):
        

        self.nodes = nodes
        self.lr = learningrate
        
        
        #initializing weights
        self.weights = []
        for i in range(0,len(self.nodes)-1):
            self.weights.append(numpy.random.rand(self.nodes[i+1],self.nodes[i])-0.5)
        
        self.activation_function = lambda x:scipy.special.expit(x)
     
        pass
        
    def train(self,inputs_list,targets_list):
        
        self.outputs = []
        
        # convert inputs list to 2d array 
        
        self.outputs.append(numpy.array(inputs_list, ndmin=2).T)
        
        for i in range(1,len(self.weights)+1):
            self.outputs.append(self.activation_function(numpy.dot(self.weights[i-1],self.outputs[i-1])))
            
        
        
        targets = numpy.array(targets_list,ndmin=2).T
        self.errors = []
        self.errors.append(targets - self.outputs[-1])  
        for i in range(1,len(self.weights)):
            self.errors.append(numpy.dot(self.weights[-i].T, self.errors[i-1]))
        for i in range(1,len(self.weights)+1):
            self.weights[-i] += self.lr*numpy.dot((self.errors[i-1]*self.outputs[-i]*(1.0 - self.outputs[-i])),numpy.transpose(self.outputs[-i-1]))
        
        
        
        pass
        
    def query(self,inputs_list):
        
        #converting inputs to 2D vertical array
        self.inputs = []
        self.inputs.append(numpy.array(inputs_list, ndmin=2).T)
        
        for i in range(1,len(self.weights)+1):
            self.inputs.append(self.activation_function(numpy.dot(self.weights[i-1],self.inputs[i-1])))
            
        
        return self.inputs[-1]
        
        

