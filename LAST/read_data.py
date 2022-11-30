import pickle
import matplotlib.pyplot as plt
import numpy as np

# for nn in range(0, 4):
#     file_name ='/home/pranjali/Documents/2022-Monsoon/DataDrivenDrugDiscovery/Project2/LAST/LAST/final_result/final_res/results/1ake_r' + str(nn) + '_latents.pkl'
#     with open(file_name, 'rb') as f:
#         data = pickle.load(f)
#     data = np.array(data)
#     print(data.shape)
#     plt.scatter(data[:, 0], data[:, 1], s = 10)
#     plt.show()

file_name ='/home/pranjali/Documents/2022-Monsoon/DataDrivenDrugDiscovery/Project2/LAST/LAST/final_result/final_res/results/1ake_' + 'structure.pkl'
with open(file_name, 'rb') as f:
    data = pickle.load(f)
print(data)
print(len(data))
data = np.array(data)
print(data.shape)
plt.scatter(data[0][:, 0], data[0][:, 1], s = 10)
plt.show()