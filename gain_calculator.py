import numpy as np
import os
import json

ROOT_PATH = '/home/npm-geant/PycharmProjects/AntiDwyer/Global_Project/geant_simulations/'
electron_zcoord_file = 'ElectronZCoordOutput.txt'
electron_energy_file = 'ElectronEnergyOutput.txt'
electron_momentum_file = 'ElectronMomentumOutput.txt'


def gain(ROOT_PATH='',
         part_of_cell=0.5,
         electric=None,
         number_of_positrons=1,
         cell_length='400',
         air_density='0.000526',
         simulation_primary_electron_number='1000',
         simulation_positron_number='100',
         electron_energy_cut=0.1):
    # if float(electric) >= 0.4e-4 and float(electric) < 1e-4:
    #     primary = '10000'
    # elif float(electric) >= 1e-4 and float(electric) < 1.2e-4:
    #     primary = '5000'
    # elif float(electric) >= 1.2e-4 and float(electric) < 1.6e-4:
    #     primary = '1000'
    # elif float(electric) >= 1.6e-4 and float(electric) < 1.8e-4:
    #     primary = '500'
    # elif float(electric) >= 1.8e-4 and float(electric) < 2.2e-4:
    #     primary = '200'
    # else:
    #     primary = '100'
    #     electric = '2.8e-4'
    if float(electric) < 0.4e-4:
        electric = '0.4e-4'
    elif float(electric) >= 0.4e-4 and float(electric) < 0.6e-4:
        electric = '0.6e-4'
    elif float(electric) >= 0.6e-4 and float(electric) < 0.8e-4:
        electric = '0.8e-4'
    elif float(electric) >= 0.8e-4 and float(electric) < 1e-4:
        electric = '1e-4'
    elif float(electric) >= 1e-4 and float(electric) < 1.2e-4:
        electric = '1.2e-4'
    elif float(electric) >= 1.2e-4 and float(electric) < 1.4e-4:
        electric = '1.4e-4'
    elif float(electric) >= 1.4e-4 and float(electric) < 1.6e-4:
        electric = '1.6e-4'
    elif float(electric) >= 1.6e-4 and float(electric) < 1.8e-4:
        electric = '1.8e-4'
    elif float(electric) >= 1.8e-4 and float(electric) < 2.0e-4:
        electric = '2e-4'
    elif float(electric) >= 2e-4 and float(electric) < 2.2e-4:
        electric = '2.2e-4'
    elif float(electric) >= 2.2e-4 and float(electric) < 2.4e-4:
        electric = '2.4e-4'
    elif float(electric) >= 2.4e-4 and float(electric) < 2.6e-4:
        electric = '2.6e-4'
    else:
        electric = '2.8e-4'

    if float(air_density) < (0.000526 + 0.000736) / 2:
        air_density = '0.526'
    else:
        air_density = '0.736'

    data = np.zeros(2 * 17).reshape(17, 2)
    with open(ROOT_PATH + '../electron_reversal/ElecRevField' + str(int(float(electric) * 1e6)) + 'Density' + str(float(air_density)) + '.txt') as fim:
        for i, line in enumerate(fim.readlines()):
            data[i] = line.split(' ')
    reverse_energy = np.zeros(17)
    reverse_angle = np.zeros(17)
    for j in range(17):
        reverse_energy[j] = data[j, 0]
        reverse_angle[j] = data[j, 1]

    if os.path.exists(ROOT_PATH + 'output/' + electron_energy_file) and os.stat(ROOT_PATH + 'output/' + electron_energy_file).st_size != 0:
        electron_energy = np.loadtxt(ROOT_PATH + 'output/' + electron_energy_file)
        electron_momentum = np.loadtxt(ROOT_PATH + 'output/' + electron_momentum_file)
        electron_zcoord = np.loadtxt(ROOT_PATH + 'output/' + electron_zcoord_file)
    else:
        return 0

    # print(len(electron_energy))
    # print(len(electron_zcoord))
    # print(number_of_positrons)
    gain_coefficient = 0
    # f = open(ROOT_PATH + '../results/secondary_avalanches_zcoord.txt', 'w')
    for j in range(len(electron_zcoord) - 1):
        if electron_energy[j] >= electron_energy_cut and float(cell_length)* (0.5 - part_of_cell) < electron_zcoord[j] < float(cell_length) / 2:
            cosangle = 1
            for i in range(17 - 1):
                if electron_energy[j] >= reverse_energy[i] and electron_energy[j] < reverse_energy[i + 1]:
                    if abs(electron_energy[j] - reverse_energy[i]) <= abs(electron_energy[j] - reverse_energy[i + 1]):
                        cosangle = np.cos(reverse_angle[i] * 3.1416 / 180)
                    else:
                        cosangle = np.cos(reverse_angle[i + 1] * 3.1416 / 180)
                elif electron_energy[j] < reverse_energy[0]:
                    cosangle = np.cos(reverse_angle[0] * 3.1416 / 180)
                else:
                    cosangle = np.cos(reverse_angle[16] * 3.1416 / 180)
            # if float(cell_length) / 4 < electron_zcoord[j] < float(cell_length) / 2:
            if 0 < electron_momentum[j] < cosangle:
                # print(electron_momentum[j])
                gain_coefficient = gain_coefficient + 1
                # f.write(str(electron_zcoord[j]) + '\n')
    # print(gain_coefficient)
    # f.close()
    gain_coefficient = (number_of_positrons / float(simulation_primary_electron_number)) * (gain_coefficient / 1 / number_of_positrons)
    # gain_coefficient = gain_coefficient / (1 - gain_coefficient)
    
    return gain_coefficient


def zelenyy_gain(ROOT_PATH='',
                 part_of_cell=0.5,
                 electric=None,
                 number_of_positrons=1,
                 cell_length='400',
                 air_density='0.000526',
                 simulation_primary_electron_number='1000',
                 simulation_positron_number='100',
                 electron_energy_cut=0.1):
    file = open(ROOT_PATH + '../electron_reversal/' + str(int(float(air_density) * 1e6)) + '_' + str(int(float(electric) * 1e6)) + '.json', 'r')
    data = json.load(file)
    if os.path.exists(ROOT_PATH + 'output/' + electron_energy_file) and os.stat(ROOT_PATH + 'output/' + electron_energy_file).st_size != 0:
        electron_energy = np.loadtxt(ROOT_PATH + 'output/' + electron_energy_file)
        electron_momentum = np.loadtxt(ROOT_PATH + 'output/' + electron_momentum_file)
        electron_zcoord = np.loadtxt(ROOT_PATH + 'output/' + electron_zcoord_file)
    else:
        return 0
    gain_coefficient = 0
    for j in range(len(electron_zcoord)):
        if electron_energy[j] >= electron_energy_cut and float(cell_length) * (0.5 - part_of_cell) < electron_zcoord[j] < float(cell_length) / 2:
            # print(electron_energy[j], np.arccos(electron_momentum[j]) * 180 / 2 / np.pi)
            for i in range(len(data['energy']) - 1):
                if data['energy'][i] > electron_energy[j] and data['theta'][i] <= np.arccos(electron_momentum[j]) * 180 / 2 / np.pi < data['theta'][i + 1]:
                    # print(data['number'][i])
                    gain_coefficient = gain_coefficient + data['number'][i - 9]
                    break
    gain_coefficient = (number_of_positrons / float(simulation_primary_electron_number)) * (gain_coefficient / 1 / number_of_positrons)
    return gain_coefficient
