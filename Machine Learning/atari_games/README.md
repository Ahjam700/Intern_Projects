# Welcome to Atari Games
Welcome to my Atari Game AI project. This project explores deep reinforcement learning to train AI agents
that can play classic Atari games like CartPole, Space Invaders, and Pac-Man. Using Deep Q-Networks (DQN)
and neural networks, the AI learns to make real-time decisions and improve gameplay performance.
The goal is to develop intelligent agents that surpass human players and showcase the power of machine
learning in gaming!

## Task
The challenge is to train an AI agent that can autonomously play Atari games using deep reinforcement learning.
 The complexity lies in learning game mechanics through raw pixel data and optimizing actions to maximize
 rewards. Unlike traditional approaches, reinforcement learning requires the agent to explore, make mistakes,
 and improve over time, making it both an exciting and demanding machine learning problem.

## Description
This project utilizes Deep Q-Networks (DQN) to enable AI agents to play Atari games by learning optimal
strategies from experience. Instead of manually programming rules, the agent interacts with the game
environment, observes the consequences of its actions, and adjusts its strategy accordingly.
By leveraging neural networks and reinforcement learning techniques, the AI can progressively refine
its decision-making skills, achieving human-level or even superhuman performance over time.

## Installation
To install the project and its dependencies, follow these steps:
```bash
pip install gym gym[atari] stable-baselines3 torch torchvision
```
Ensure that your environment supports GPU acceleration for faster training. If running on a local machine,
ensure that all required drivers and CUDA libraries are installed for efficient deep learning computations.
Running experiments on cloud-based GPU services like Google Colab or AWS can also significantly speed up
training times.

## Usage
To train and test the AI models, run the following commands:
```bash
python train.py --game CartPole-v1
python train.py --game SpaceInvaders-v4
python train.py --game MsPacman-v4
```
The script initializes the agent, loads the game environment, and begins training using reinforcement learning.
Once training is complete, the model can be tested by observing how well it performs in real-time gameplay.
Adjusting hyperparameters like learning rate,
batch size, and training steps can help improve performance.

### The Core Team

Ahmed Jamil Shehu

<span><i>Made by Ahmed Jamil Shehu<a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>

qwasar