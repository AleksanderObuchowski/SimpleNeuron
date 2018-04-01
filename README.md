# Simple Neuron

Simple Neuron is my project of simple python neural network library. It's easy to use and illustrates how neural networks works.

[TOC]

## Requirements

```python
import numpy
```

Simple neuron uses numpy python library so you need to have it installed before using it.

## How it works?


#### Neurons

------------


Neuraln network consists, as the name indicates, of neurons. Each neuron takes an input form neurons connected to it. All inputs have their **weights** . Neuron sums inputs multiplied by their weights, and applies activation function to this sum.
[![Neuron](https://i.imgur.com/PqtErEy.png "Neuron")](https://i.imgur.com/PqtErEy.png "Neuron")

All **inputs** typically have a range 0.00 to 1.00 . Zero means that there is little to no chance of something and one meaning we are almost sure that there is something

**Weights** have a range -1.00 to 1.00. -1 means that the inputs work against of the the thing we are trying to predict and 1 means it acts in favour of it.

The goal of neral network is to adjust its weights so that it, with some certainty, can predict soulution form the inputs. If some input is  more important and it acts in favour of some action it should have positive weight close to 1. If it is not that important the weight should be around 0. and if the input works against an action it should have negative weight close to -1.

###### Example

Let's consider an example below. We are trying to predict if there is a cat on a given picture. Previous layer of neurons have stated there is 67% probability that there is a tale on the image, 83% probalility that there are four paws on the picture, 91% probalility that there is a horn and 48 % chance there are two eyes on the picture.

[![cat](https://i.imgur.com/AkMXLMg.png "cat")](https://i.imgur.com/AkMXLMg.png "cat")

Of course we know that cats have tails, four paws and two eyes, but they don't have horns. That's why inputs  **1**, **2** and **4** should have **positive** weights. If we know there is a tail, this should increase the chance that there is a cat. On the other hand input 3 should have negative weight, because if we know there is a horn, we can be sceptical about image presenting a cat. If we have shown our neural network thousand of images of cats we can hope that it will learn that cats don't have horns and put negative weight in the input whose role was to deduce if there is a horn. However we can't know for sure what neural network picked as important and what it didn't, all inputs and outputs are just numers that somehow lead to the solution

#### Activation Function

------------
The sum of inputs multiplied by their weights can often be larger than 1 or less than 0, that's why we need something called **activation function**. Activation fuction applied to the output limits it to the range (0.00,1.00). An example of such funtion is **sigmoid **.

[![sigmoid function](https://i.imgur.com/FHlAJ2r.png "sigmoid function")](https://i.imgur.com/FHlAJ2r.png "sigmoid function")

As the argumenst approch infinity the function aproches 1, as they approach minus nfinity it approches 0 with the value of 0.5 at when the argument is equal to 0.

#### Layers
------------

Full neural network consists of not one but many neurons arragned in **layers**, each layer takes the  output of the previous one and threats it as input 

[![layers](https://i.imgur.com/njeYOhI.png "layers")](https://i.imgur.com/njeYOhI.png "layers")


#### Weights
------------
Let's consider an neural network with 2 layers, firs one has 3 neurons and the second one has 2 neurons.
![weights](https://i.imgur.com/YHD5ROU.png)

In this layer inputs to layer B should look like this:

![b1](https://i.imgur.com/v9xTCPN.png)

- - -
![b2](https://i.imgur.com/ESwR61r.png)

We can use **Matrix multiplication** to simplify this process
![matrix](https://i.imgur.com/j272ldD.png)