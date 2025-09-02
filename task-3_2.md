# Deep Learning: Understanding Basic Neural Networks [[link]](https://medium.com/@sumbatilinda/deep-learning-part-1-understanding-basic-neural-networks-c9ccdb17a343)
### Blog Review ([docs](https://docs.google.com/document/d/1fIOPxG2oayxLDc2CusvOJ2YGP7R6LkLvmVnpPVi2Xno/edit?tab=t.nmla5a3d5kw9))

Back in the day, some scientist looked at the birds and went, *“damn, flying is cool, we should do it too,”* and that’s how planes were born. Similarly, neural networks came into existence when someone went, *“Why not copy the best pattern recognizer in existence? The human brain.”*  

The way I see it, **neural networks** are kind of like fake neurons passing numbers around (as in sending signals). The main goal is to spot **patterns**, whether in emails, face recognition, or the Instagram algorithm.  



### The timeline:
- **1943** – McCulloch & Pitts make the first math brain model, *“threshold logic”*, i.e., the neuron goes yes/no.  
- **1958** – Rosenblatt drops the **perceptron** (OG neural network), baby version of pattern recognition  
- **1980s** – Fukushima invents **Neocognitron** (handwriting recognition)  
- **1990s** – People try deeper networks but they take forever to train.  
- **2000s** – Hinton & co pre-trains deep networks layer by layer  
- **2009** – Speech recognition hits with big data → error rates drop  
- **2012** – Google’s neural net now recognises cats  
- **2014-16** – Neural nets are now mainstream. Google buys DeepMind, Facebook tags faces in posts (*DeepFace*), AlphaGo beats a professional Go player.  



But, **Deep Learning ≠ computers thinking like humans.** It’s more like, with enough data + power, they can do human-ish stuff like translate languages, recognise images, recommend you shows at 2am.  



This article then jumps into the **technical definitions** of Deep Learning and its components. Starting with **Deep Learning**, also called *‘Artificial Neural Networks’*, which is similar to a real brain neuron and has many layers.  

A **Deep Learning Model** is trained by:  
`set a learning objective -> adjust its parameters -> improve performance`  

It differs from **traditional ML**, which takes forever since you have to manually decide what features matter and build them yourself, which is not really efficient.  



### The perceptron
The perceptron is the simplest form of a neural network:  
- takes several **inputs**  
- performs **weighted calculation**  
- produces **single output**  

- **Single-Layer Perceptron** – only input and output layers, straightforward but limited.  
- **Multi-Layer Perceptron** – has hidden layers between input and output, allows network to capture more complex patterns.  

In general, **neurons work like**:  
`Receives input signals -> perform calculations -> send output signals to deeper neurons through synapse.`  



### Terminologies:
- **Neuron (node)** – lies at core; receives inputs, processes them and produces an output.  
- **Weights** – values assigned to connections between neurons. Network learns patterns and improves predictions by adjusting these weights. *(primary way to train DL models)*  
- **Bias** – acts as an additional parameter; allows network to account for variations.  
- **Activation function** – introduces non-linearity; helps network learn complex relationships (*sigmoid, tanh, ReLU*)  

Process:  
`neuron collects inputs -> adds each signal & multiplies them by respective weights -> adds a bias -> applies activation function -> passes result to next layer through synapse.`  
(repeats until final output is produced.)  



### Activation Functions
**Activation Functions** introduce non-linearity, allowing the network to learn complex patterns and decide whether a neuron should be activated based on input.  

- **Threshold Function (unit step function)**  
  - Neuron activates only if weighted input ≥ threshold, else stays inactive.  
  - Binary output → [0 (False) or 1 (True)]  
  - The graph is too rigid + not differentiable at all points, hence can’t be used in modern training.  

- **Sigmoid Function**  
  - Smooth curve mapping, input → range (0,1)  
  - Good for probability and binary  
  - Differentiable at all points hence works with backpropagation  

- **Rectifier Functions (ReLUs)**  
  - Piecewise linear nature  
  - *(it's graph takes a sharp turn at 0, where the function transitions from outputting 0 to outputting the input value itself.)*  

- **Hyperbolic Tangent Function (tanh)**  
  - Output values: range (-1, 1)  
  - *(it's graph is similar to sigmoid, but output values are shifted downwards)*  



### Conclusion
When I was just stating out, deep learning felt pretty intimidating with all its jargon and math, but this article broke it down really simply, and now I get how neurons, weights, bias, and activation functions all fit together, and I feel more familiar with the basics of how neural networks work, and I’m looking forward to explore more!
