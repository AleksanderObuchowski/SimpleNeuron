<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [HOW IT WORKS - THEORY](#how-it-works---theory)
  - [Neurons](#neurons)
    - [Example](#example)
  - [Activation Function](#activation-function)
  - [Layers](#layers)
  - [Weights](#weights)
  - [HOW DOES NEURAL NETWORK LEARN?](#how-does-neural-network-learn)
    - [Errors](#errors)
    - [Errors on layers](#errors-on-layers)
    - [Learning](#learning)
- [HOW IT WORKS  - PYTHON](#how-it-works----python)
- [INSTALATION](#instalation)
  - [Requirements](#requirements)
  - [Installing SimpleNueron](#installing-simplenueron)
- [USAGE](#usage)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->






# HOW IT WORKS - THEORY


## Neurons

------------


Neuraln network consists, as the name indicates, of neurons. Each neuron takes an input from neurons connected to it. All inputs have their **weights** . Neuron sums inputs multiplied by their weights, and applies activation function to this sum.
[![Neuron](https://i.imgur.com/PqtErEy.png "Neuron")](https://i.imgur.com/PqtErEy.png "Neuron")

All **inputs** typically have a range from 0.00 to 1.00 . Zero means that there is little to no chance of something and one means we are almost sure that there is some likelihood.

**Weights** have a range -1.00 to 1.00. -1 means that the inputs dereases the probability of the the thing we are trying to predict and 1 means it acts in increases the probability.

The goal of a neural network is to adjust its weights so that it, with some certaint probability, can predict solution from the inputs. If some input is more important and acts increases the probability of some action, it should have positive weight close to 1. If it is not that important, the weight should be around 0. And if the input decreases the probability of an action it should have negative weight close to -1.

### Example

Let's consider the example below. We are trying to predict if there is a cat in a given picture. Previous layer of neurons has stated there is 67% probability that there is a tail in the image, 83% probalility that there are four paws in the picture, 91% probalility that there is a horn and 48 % chance there are two eyes on the picture.

[![cat](https://i.imgur.com/AkMXLMg.png "cat")](https://i.imgur.com/AkMXLMg.png "cat")

Of course we know that cats have tails, four paws and two eyes, but they don't have horns. That's why inputs  **1**, **2** and **4** should have **positive** weights. If we know there is a tail, this should increase the chance that there is a cat. On the other hand input 3 should have negative weight, because if we know there is a horn, we can be sceptical about the image presenting a cat. If we have shown our neural network thousand of images of cats we can hope that it has learnt that cats don't have horns and put negative weight in the input, which role was to deduce if there is a horn. However we can't know for sure what neural network picked as important and what it didn't, all inputs and outputs are just numbers that somehow lead to the solution.

## Activation Function

------------
The sum of the inputs multiplied by their weights can often be larger than 1 or less than 0, that's why we need something called **activation function**. Activation fuction applied to the output limits it to the range (0.00,1.00). An example of such a function is **sigmoid **.

[![sigmoid function](https://i.imgur.com/FHlAJ2r.png "sigmoid function")](https://i.imgur.com/FHlAJ2r.png "sigmoid function")

As the arguments approch infinity, the function aproches 1. As they approach minus infinity, it approches 0, with the value of 0.5 when the argument is equal to 0.

## Layers
------------

Full neural network consists of not one but many neurons arranged in **layers**, each layer takes the  output of the previous one and treats it as an input.

[![layers](https://i.imgur.com/njeYOhI.png "layers")](https://i.imgur.com/njeYOhI.png "layers")


## Weights
------------
Let's consider a neural network with 2 layers, first one has 3 neurons and the second one has 2 neurons.
![weights](https://i.imgur.com/YHD5ROU.png)

In this layer inputs to layer B should look like this:

![b1](https://i.imgur.com/v9xTCPN.png)

- - -
![b2](https://i.imgur.com/ESwR61r.png)

We can use **Matrix multiplication** to simplify this process,
![matrix](https://i.imgur.com/j272ldD.png)


## HOW DOES A NEURAL NETWORK LEARN?



_ _ _

### Errors
- - -
In order for a neural network to learn, it first has to know what mistakes it's making. Let's consider the following example:
![erroer](https://i.imgur.com/0897Cjp.png)

Let's say we guessed the value of Y1 but it's wrong and we know the value of an error. Let's call this error EY1. What should be the error of X1 or X2? One might say we should split the error of Y1 evenly because there are two nodes connected to Y1, so error of X1 should be 1/2 of error of Y1 and error of X2 should be 1/2 of error of Y1. Well it's generally not a good way of doing this, because we can see that weight coming from X2 is 3 times larger than the one of X1. Because of that X2 contributes to the mistake of Y1 3 times as much as X1. Therefore it would be better to describe the error of X1 as 1/4 of the error of Y1 and error of X2 as 3/4 of the error of Y1. This can lead to a general principle:
<br/>



![](https://i.imgur.com/NV1ZNFR.png)  
<br/>

![](https://i.imgur.com/G88y0W7.png)  

### Errors on layers





- - -



![](https://i.imgur.com/NfLZ1Bi.png)  

If we consider the following example then we see that X1 and X2 contribute not only to the error of Y1 but also Y2. Therefore their error should come for both Y1 and Y2. If we write it in an equation, it looks like this:
<br/>
![](https://i.imgur.com/meU10hK.png)  
<br/>
![](https://i.imgur.com/ktDUcdk.png)  
If we again write it in marices, we get something like this:

![](https://i.imgur.com/T8alM7z.png)  

We can then ommit the values in the denominator. If we do this, we only lose the information about the normalization of the errors, not the information about how much each weight contributs to it.

![](https://i.imgur.com/xpZOn4h.png)  

Now we can see that the weight of the matrix is the same as the one we were using to feed forward values between the layers, except now it's transposed, which means it is flipped along the diagonal line. And if you think about it, it makes a perfect sence, we are now going backwards, instead of forwards, which means we need to invert the matrix:

![](https://i.imgur.com/CutKCIe.png)  

Now we can write the general priciple:  

![](https://i.imgur.com/HX7j6p7.png)  

With this alghoritm we can desribe the errors from the end to the beggining of the neural network

### Learning
- - -
Ok now know the errors but how can we adjust the weight to correct them?

Firstly we will have to define the error function **E**:
<br/>
![](https://i.imgur.com/8PjnGMo.png)
<br/>
Where **C** is the correct value of the output and **O** is the output of the nueral network
We are calculationg the square of the difference in order to make the value of it be always positive and also to have a function that has only one minimum.

Secondly we are going to calculate the **derivative** of the error function to know how it changes and which way to go to reach the minimum of the error function.


![](https://i.imgur.com/QRU9veo.png)

If we calculate the derivative, we can show it like that:
<br/>
![](https://i.imgur.com/aqe5Z2p.png)
<br/>
Then we can use the **chain rule** to expand the derivative:
<br/>
![](https://i.imgur.com/H8zAwhk.png)
<br/>
Then we can calculate the derivative of the error function over the output
<br/>
![](https://i.imgur.com/CfWclM9.png)
<br/>
Then we can can write the output **O** as an activation function applied over weighted output of the previous layer:
<br/>
![](https://i.imgur.com/NUdDiUn.png)
<br/>
Then we can calculate the derivtive of the activation fuction using a  **chain rule** 
<br/>
![](https://i.imgur.com/MWc94GV.png)
<br/>
Then, in order to calculate the new value of weight, we need to **subtract** the derivative from the previous value. That is because the derivative tells us where the function increases and, as you remeber we want to go downhill.
<br/>
![](https://i.imgur.com/2VGbWq8.png)
<br/>
Then we can write the equation in a slightly cleaner way:
<br/>
![](https://i.imgur.com/KP91T81.png)
<br/>
Now we need to remember we are going backwards once again, so our weights matrix needs to be transposed 
<br/>
![](https://i.imgur.com/PRSyZ3L.png)
<br/>
Now we need to introduce variable called **learning rate** .
This variable, ranged form 0 to 1, will tell us how much we want theweights to change.
Generally we don't want to go with the difference of weights because we might miss the minimum. 
<br/>
![](https://i.imgur.com/V5aeZ0u.png)
<br/>
The steps we are taking are proportional to the derivative, so you can see, if the function is steeper, we take bigger steps, when we get closer to the minimum, we take smaller and smaller steps, making our calculations more accurate.
Too small learning rate however can lead to very slow updates as well as getting stuck in local minimum, which is not the global one.
<br/>
If we take into consideration the learning rate, our general equation looks like this
<br/>
![](https://i.imgur.com/NYfoLYp.png)
<br/>
That's whole theory behind a simple neural network!



# HOW IT WORKS  - PYTHON

works in progress

# INSTALATION
## Requirements
Simple neuron requires libraries :
Numpy
Scipy

to install them you can simply do it with pip:
```
pip install numpy

```
```
pip install scipy

```
## Installing SimpleNueron
To install SimpleNeuron you all you have to do is copy the SimpleNeuron.py file to your directory



# USAGE

First you need to imporst NeuralNetwork object
```
from SimpleNeuron import NeuralNetwork
```
then you need to initialize neural network object, it takes 2 parameters as input table consisting of numbers of neurons in each layer and learning rate, for example:

```
nn = NeuralNetwork([3,6,8],0.3)
```
will create a neural network with 3 layears consisting, as follows 3,6,8 neurons with learning rate of 0.3
Then you will have to train your network on some data for this you use:
```
nn.learn(input,output)
```
finally when your network is trained you can use predict function to predict output based on input:

```
nn.predict(input)
```
