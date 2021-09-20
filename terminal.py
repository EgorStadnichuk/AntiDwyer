import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gain_calculator
import numpy as np
import os
import json


def terminal():
    ROOT_PATH = os.getcwd()
    # data = np.zeros(2 * 17).reshape(17, 2)
    # electric = '3.5e-4'
    # air_density = '1.2'
    # with open(ROOT_PATH + '/geant_simulations/electron_reversal/ElecRevField' + str(int(float(electric) * 1e6)) + 'Density' + str(float(air_density)) + '.txt') as fim:
    #     for i, line in enumerate(fim.readlines()):
    #         data[i] = line.split(' ')
    # reverse_energy = np.zeros(17)
    # reverse_angle = np.zeros(17)
    # for j in range(17):
    #     reverse_energy[j] = data[j, 0]
    #     reverse_angle[j] = data[j, 1]
    # reverse_value = np.zeros(17)
    # reverse_value[:] = 1
    # file = open(ROOT_PATH + '/geant_simulations/electron_reversal/reversed.json', 'r')
    # data = json.load(file)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(data['energy'], data['theta'], data['number'], c='g', marker='o')
    # ax.scatter(reverse_energy, reverse_angle, reverse_value, c='b', marker='^')
    # ax.set_xlabel('Energy, MeV')
    # ax.set_ylabel('Angle, degrees')
    # ax.set_zlabel('Reversal probability')
    # plt.show()
    # data = np.load(ROOT_PATH + '/results/simulation_output_gain.npy')
    # print(data)
    electron_zcoord_file = 'ElectronZCoordOutput.txt'
    electron_energy_file = 'ElectronEnergyOutput.txt'
    electron_momentum_file = 'ElectronMomentumOutput.txt'
    number = '133'
    particle = 'positron'
    parpar = 'Positron'
    # parpar = 'Gamma'
    # particle = 'gamma'
    if os.path.exists(ROOT_PATH + '/geant_simulations/' + number + '/output/' + electron_energy_file) and os.stat(ROOT_PATH + '/geant_simulations/' + number + '/output/' + electron_energy_file).st_size != 0:
        electron_energy = np.loadtxt(ROOT_PATH + '/geant_simulations/' + number + '/output/' + electron_energy_file)
        electron_momentum = np.loadtxt(ROOT_PATH + '/geant_simulations/' + number + '/output/' + electron_momentum_file)
        electron_zcoord = np.loadtxt(ROOT_PATH + '/geant_simulations/' + number + '/output/' + electron_zcoord_file)
    else:
        return 0
    electron_energy_cut = 0.5
    simulation_primary_electron_number = 10000
    positron = np.loadtxt(ROOT_PATH + '/geant_simulations/' + number + '/' + particle + '_output/' + parpar + 'EnergyOutput.txt')
    number_of_positrons = len(positron)
    cell_length = 1000
    part_of_cell = 0.5
    electric_field = '2e-4'
    number_of_gamma = number_of_positrons
    air_density = '0.0008'
    simulation_positron_number = 1
    ROOT_PATH = ROOT_PATH + '/geant_simulations/' + number + '/'

    # gain_coefficient = gain_calculator.gain(part_of_cell=part_of_cell, ROOT_PATH=ROOT_PATH, electric=electric_field, number_of_positrons=number_of_gamma, cell_length=cell_length, air_density=air_density, simulation_positron_number=simulation_positron_number, simulation_primary_electron_number=simulation_primary_electron_number, electron_energy_cut=electron_energy_cut)
    # print(gain_coefficient)

    ROOT_PATH = os.getcwd()
    file = open(ROOT_PATH + '/geant_simulations/electron_reversal/800_200.json', 'r')
    data = json.load(file)
    # print(data['energy'])

    gain_coefficient = 0
    for j in range(len(electron_zcoord)):
        if electron_energy[j] >= electron_energy_cut and float(cell_length)* (0.5 - part_of_cell) < electron_zcoord[j] < float(cell_length) / 2:
            # print(electron_energy[j], np.arccos(electron_momentum[j]) * 180 / 2 / np.pi)
            for i in range(len(data['energy']) - 1):
                if data['energy'][i] > electron_energy[j] and data['theta'][i] <= np.arccos(electron_momentum[j]) * 180 / 2 / np.pi < data['theta'][i + 1]:
                    # print(data['number'][i])
                    gain_coefficient = gain_coefficient + data['number'][i - 9]
                    break
    gain_coefficient = (number_of_positrons / float(simulation_primary_electron_number)) * (gain_coefficient / 1 / number_of_positrons)
    print(gain_coefficient)


def gotcha():
    primary_energy = [1, 10]
    primary_number = 10000
    for i in range(2):
        file = open('gamma_' + str(primary_energy[i]) + '_mev/GammaEnergyOutput.txt', 'r')
        energy = np.loadtxt(file)
        file.close()
        energ = []  # selection of gamma with energy more than 1 MeV
        for j in range(len(energy)):
            if energy[j] >= 1:
                energ.append(energy[j])
        plot = np.histogram(energ)
        print(plot[0])
        print(plot[1][0: len(plot[1]) - 1])
        for j in range(len(plot[0])):
            plot[0][j] = plot[0][j] / primary_number  # normalization
        plt.title('Primary electron energy ' + str(primary_energy[i]))
        plt.xlabel('Gamma energy, MeV')
        plt.ylabel('Number of gamma')
        y = plot[0]
        x = plot[1][0: len(plot[1]) - 1]
        plt.semilogy(x, y)
    plt.show()

    for i in range(2):
        file = open('gamma_' + str(primary_energy[i]) + '_mev/GammaZCoordOutput.txt', 'r')
        zcoord = np.loadtxt(file)
        file.close()
        file = open('gamma_' + str(primary_energy[i]) + '_mev/GammaEnergyOutput.txt', 'r')
        energy = np.loadtxt(file)
        file.close()
        energ = []
        zcoor = []
        for j in range(len(energy)):
            if energy[j] >= 1:
                energ.append(energy[j])
                zcoor.append(zcoord[j])
        for j in range(len(zcoor)):
            zcoor[j] = 500 - zcoor[j]
        plot = np.histogram(zcoor)
        for j in range(len(plot[0])):
            plot[0][j] = plot[0][j] / primary_number
        plt.title('Primary electron energy ' + str(primary_energy[i]) + ' MeV')
        plt.xlabel('Gamma z coordinate, m')
        plt.ylabel('Number of gamma')
        plt.semilogy(plot[1][0: len(plot[1]) - 1], plot[0])
    plt.show()


if __name__ == '__main__':
    # terminal()
    gotcha()
