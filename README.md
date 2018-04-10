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


Neuraln network consists, as the name indicates, of neurons. Each neuron takes an input form neurons connected to it. All inputs have their **weights** . Neuron sums inputs multiplied by their weights, and applies activation function to this sum.
[![Neuron](https://i.imgur.com/PqtErEy.png "Neuron")](https://i.imgur.com/PqtErEy.png "Neuron")

All **inputs** typically have a range 0.00 to 1.00 . Zero means that there is little to no chance of something and one meaning we are almost sure that there is something

**Weights** have a range -1.00 to 1.00. -1 means that the inputs work against of the the thing we are trying to predict and 1 means it acts in favour of it.

The goal of neral network is to adjust its weights so that it, with some certainty, can predict soulution form the inputs. If some input is  more important and it acts in favour of some action it should have positive weight close to 1. If it is not that important the weight should be around 0. and if the input works against an action it should have negative weight close to -1.

### Example

Let's consider an example below. We are trying to predict if there is a cat on a given picture. Previous layer of neurons have stated there is 67% probability that there is a tale on the image, 83% probalility that there are four paws on the picture, 91% probalility that there is a horn and 48 % chance there are two eyes on the picture.

[![cat](https://i.imgur.com/AkMXLMg.png "cat")](https://i.imgur.com/AkMXLMg.png "cat")

Of course we know that cats have tails, four paws and two eyes, but they don't have horns. That's why inputs  **1**, **2** and **4** should have **positive** weights. If we know there is a tail, this should increase the chance that there is a cat. On the other hand input 3 should have negative weight, because if we know there is a horn, we can be sceptical about image presenting a cat. If we have shown our neural network thousand of images of cats we can hope that it will learn that cats don't have horns and put negative weight in the input whose role was to deduce if there is a horn. However we can't know for sure what neural network picked as important and what it didn't, all inputs and outputs are just numers that somehow lead to the solution

## Activation Function

------------
The sum of inputs multiplied by their weights can often be larger than 1 or less than 0, that's why we need something called **activation function**. Activation fuction applied to the output limits it to the range (0.00,1.00). An example of such funtion is **sigmoid **.

[![sigmoid function](https://i.imgur.com/FHlAJ2r.png "sigmoid function")](https://i.imgur.com/FHlAJ2r.png "sigmoid function")

As the argumenst approch infinity the function aproches 1, as they approach minus nfinity it approches 0 with the value of 0.5 at when the argument is equal to 0.

## Layers
------------

Full neural network consists of not one but many neurons arragned in **layers**, each layer takes the  output of the previous one and threats it as input 

[![layers](https://i.imgur.com/njeYOhI.png "layers")](https://i.imgur.com/njeYOhI.png "layers")


## Weights
------------
Let's consider an neural network with 2 layers, firs one has 3 neurons and the second one has 2 neurons.
![weights](https://i.imgur.com/YHD5ROU.png)

In this layer inputs to layer B should look like this:

![b1](https://i.imgur.com/v9xTCPN.png)

- - -
![b2](https://i.imgur.com/ESwR61r.png)

We can use **Matrix multiplication** to simplify this process
![matrix](https://i.imgur.com/j272ldD.png)


## HOW DOES NEURAL NETWORK LEARN?



_ _ _

### Errors
- - -
In order for neural network to learn it first has to know about the mistakes it's making. Let's concider following example:
![erroer](https://i.imgur.com/0897Cjp.png)

Lest's say we guessed the value of Y1 but it's wrong and we know the error. Let's call this error EY1. What should be the error of X1 or X2? One might say we should split the errror of Y1 evenly becouse there are two nodes connected to Y1, so error of X1 should be 1/2 of error of Y1 and error of X2 should be 1/2 of error of Y1. Well it's generaly not a good wey of doung this, beause we can see that weight comming from X2 is 3 times larger than the of of X1. Because of that X2 contributes to the mistake of Y1 3 times as much as X1. Therefore it would be better to describe the error of X1 as 1/4 the error of Y1 and error of X2 as 3/4 the error of Y1. Whis can lead to general principle:
<br/>



![](https://i.imgur.com/NV1ZNFR.png)  
<br/>

![](https://i.imgur.com/G88y0W7.png)  

### Errors on layers





- - -



![](https://i.imgur.com/NfLZ1Bi.png)  

If we consider the following example then we see that X1 and X2 contribute to not only the error of Y1 but also Y2. Therefore their error should come for both Y1 and Y2. If we write it in equation it should look like this:
<br/>
![](https://i.imgur.com/meU10hK.png)  
<br/>
![](https://i.imgur.com/ktDUcdk.png)  
If we again write it in marices we would get something like this:

![](https://i.imgur.com/T8alM7z.png)  

We can then ommint the values in the denominator. If we do this we only loose the information about the normalization of the errors not the information about how much each weight contributs to it.

![](https://i.imgur.com/xpZOn4h.png)  

We can now see then the weight matrix is the same one what we have been using for to feed forward values between the layers, exept now it's transposed what means it is flipped along the diagonal line. And if you think about it, it makes perfect sence, we are now going backawrds instead of forward what means we need to invert the matrix:

![](https://i.imgur.com/CutKCIe.png)  

We can now write the general priciple:  

![](https://i.imgur.com/HX7j6p7.png)  

With this alghoritm we can desribe errors from the end to the beggigng of the neural network

### Learning
- - -
Ok we now know the erros but how can we adjust the weight to correct them?

Firstly we will have to define error function **E**:
<br/>
![](https://i.imgur.com/8PjnGMo.png)
<br/>
Where **C** is the correct value of the ourput and **O** is the output of the nueral network
We are calculationg the squar of the difference in order to make the value of it always possitive and also have a function that has only one minimum

Secondly we are goint to calculate the **derivative** of the error function to know how it changes and which way to go to reach the minimum of the error fucntion.

<br/>
![](https://i.imgur.com/QRU9veo.png)
<br/>
If we calculate the derivative we can show it like that:
<br/>
![](https://i.imgur.com/aqe5Z2p.png)
<br/>
Then we can use the **chain rule ** to expand the derivative:
<br/>
![](https://i.imgur.com/H8zAwhk.png)
<br/>
Then we can calculate the derivative of the error function over output
<br/>
![](https://i.imgur.com/CfWclM9.png)
<br/>
Then we can can write the output **O** as an activation function applied over weighted output of the previous layer:
<br/>
![](https://i.imgur.com/NUdDiUn.png)
<br/>
Then we can calculate the derivtive of activation fuction using **chain rule**
<br/>
![](https://i.imgur.com/MWc94GV.png)
<br/>
Then in order to calculate the new value of weight we need to **subtract** the derivative form the previous value. That is because the derviative tells us in the function increase and, as you remeber we want to go downhill.
<br/>
![](https://i.imgur.com/2VGbWq8.png)
<br/>
Then we can write the equation in a slightly cleaner way:
<br/>
![](https://i.imgur.com/KP91T81.png)
<br/>
Now we need to remember we are going backwards once again so our weights matrix needs to be transposed 
<br/>
![](https://i.imgur.com/PRSyZ3L.png)
<br/>
Now we need to introduce variable called **learning rate** .
This variable, ranged form 0 to 1 will tell us how much we want weights to change
Generally we dont want to go with difference of weights because we might miss the minimum. 
<br/>
![](https://i.imgur.com/V5aeZ0u.png)
<br/>
The steps we are taking ar proportional to the derivative so you can see then when the function is steeper we take bigger steps, when it tends to minimum we take smalller and smaller steps meking our calculations more accurate.
Too small learning rate however can leat to very slow updates as well as stucking in local minimum which is not the lobal one.
<br/>
If we take to concederation the learning rate our general equation would look like this
<br/>
![](https://i.imgur.com/NYfoLYp.png)
<br/>
Theat's the whole theory behind a simple neural network !



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