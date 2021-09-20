import numpy as np
import matplotlib.pyplot as plt
import os


def distribution():
    event = '/140/'
    name_data = 'Output.txt'
    name_plot = '.png'
    particle = ['Electron', 'Positron', 'Gamma']
    path = ['output/', 'positron_output/', 'gamma_output/']
    value = ['Energy', 'Momentum', 'ZCoord']
    value_units = [', Mev', '', ', m']
    range_min = [1, -1, -500]
    range_max = [5, 1, 500]
    rotate = [1, 1, -1]
    add = [0, 0, 500]
    # for i in range(len(particle)):
    i = 2
    for j in range(len(value)):
        file = open(os.getcwd() + '/geant_simulations' + event + path[i] + particle[i] + value[j] + name_data)
        data = np.loadtxt(file)
        file.close()
        y_axis, x_axis = np.histogram(data, range=(range_min[j], range_max[j]), density=True)
        for k in range(len(x_axis)):
            x_axis[k] = add[j] + rotate[j] * x_axis[k]
        plt.title(particle[i] + ' ' + value[j])
        plt.xlabel(value[j] + value_units[j])
        plt.ylabel(particle[i] + ' number density')
        plt.plot(x_axis[0: len(x_axis) - 1], y_axis)
        plt.savefig(os.getcwd() + '/geant_simulations' + event + particle[i] + value[j] + name_plot)
        plt.close()
    file = open(os.getcwd() + '/geant_simulations' + event + path[i] + particle[i] + value[0] + name_data)
    data_0 = np.loadtxt(file)
    file.close()
    file = open(os.getcwd() + '/geant_simulations' + event + path[i] + particle[i] + value[2] + name_data)
    data_2 = np.loadtxt(file)
    for k in range(len(data_2)):
        data_2[k] = data_2[k] * rotate[2] + add[2]
    file.close()
    plt.title(particle[i] + ' ' + value[0] + ' ' + value[2])
    plt.xlabel(value[0] + value_units[0])
    plt.ylabel(value[2] + value_units[2])
    plt.plot(data_0, data_2, '*')
    plt.savefig(os.getcwd() + '/geant_simulations' + event + particle[i] + value[0] + value[2] + name_plot)
    plt.close()


if __name__ == '__main__':
    distribution()
