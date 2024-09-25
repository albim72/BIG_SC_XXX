import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],[0,0,0]])
train_outputs = np.array([[1,0,1,1,0,1,1]]).T
train_iters = 50_000

network.train(train_inputs,train_outputs,train_iters)
print("wektor wag po wytrenowaniu sieci...")
print(network.weights)

print("ocena modelu...")
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0],])

for data in test_data:
    print(f"wynik predykcji dla {data} wynosi: {network.propagation(data)}")
