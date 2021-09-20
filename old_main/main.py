import gain_coefficient

import numpy as np
import matplotlib.pyplot as plt
import os
from multiprocessing import Pool


# ROOT_PATH = '/home/npm-geant/PycharmProjects/AntiDwyer/Global_Project/geant_simulations/'
ROOT_PATH = os.getcwd() + '/geant_simulations/'
feedback = gain_coefficient.Feedback()


def main():
    # cell_length = [200, 400, 600, 800, 1000]  # m
    # cell_length = [1000]
    # with Pool(os.cpu_count()) as p:
    #     print(p.map(run_positron, cell_length))
    cell = 1000
    air_density = 0.000526  # g/cm^3
    simulation_feedback_particle_number = 1  # number of simulations for every feedback particle (positrons, gamma). Use > 1 for more statistics
    electron_energy_cut = 0.1  # MeV
    part_of_cell = 0.25  # in which part of cell electron birth is considered to be feedback
    simulation_primary_electron_number = 100
    electric = 1.8e-4
    # physics = 'G4EmLivermorePhysics'
    # physics = 'G4PenelopePhysics'
    # physics = 'G4EmLowEPPhysics'
    physics = 'G4EmStandartPhysics_option4'
    print(feedback.positron_feedback(physics=physics, part_of_cell=part_of_cell, electric_field=electric, air_density=air_density, cell_length=cell, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut))
    # with Pool(os.cpu_count()) as p:
    #     print(p.map(run_gamma, cell_length))
    # run_gamma(400)
    # air_density = 0.000526  # g/cm^3
    # simulation_feedback_particle_number = 1  # number of simulations for every feedback particle (positrons, gamma). Use > 1 for more statistics
    # electron_energy_cut = 0.1  # MeV
    # part_of_cell = 0.25  # in which part of cell electron birth is considered to be feedback
    # simulation_primary_electron_number = 10
    # cell = 500
    # electric = 10e-4
    # print(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric, air_density=air_density, cell_length=cell, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut))
    # file = open(ROOT_PATH + '../results/addition.txt', 'w')
    # cell_length = [400, 1000]
    # electric_field = [3e-4, 1.6e-4]
    # for i in range(2):
    #     electric = electric_field[i]
    #     cell = cell_length[i]
    #     file.write(str(cell) + ' ' + str(electric) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric, air_density=air_density, cell_length=cell, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
    # file.close()


def run_positron(cell_length):
    air_density = 0.000526  # g/cm^3
    simulation_feedback_particle_number = 1  # number of simulations for every feedback particle (positrons, gamma). Use > 1 for more statistics
    electron_energy_cut = 0.1  # MeV
    part_of_cell = 0.25  # in which part of cell electron birth is considered to be feedback
    if cell_length == 100:
        electric_field = [1e-4, 2e-4, 3e-4, 4e-4, 5e-4, 6e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 200:
        electric_field = [1e-4, 1.8e-4, 2.6e-4, 3.4e-4, 4.2e-4, 5e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 300:
        electric_field = [1e-4, 1.6e-4, 2.2e-4, 2.8e-4, 3.4e-4, 4e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 400:
        electric_field = [2e-4, 2.2e-4, 2.4e-4, 2.6e-4, 2.8e-4, 3e-4]
        file = open(ROOT_PATH + '../results/GAV_positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 500
            elif j == 1:
                simulation_primary_electron_number = 300
            elif j == 2:
                simulation_primary_electron_number = 200
            elif j == 3:
                simulation_primary_electron_number = 200
            elif j == 4:
                simulation_primary_electron_number = 200
            else:
                simulation_primary_electron_number = 200
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 500:
        electric_field = [1e-4, 1.3e-4, 1.6e-4, 1.9e-4, 2.2e-4, 2.5e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 600:
        electric_field = [1e-4, 1.2e-4, 1.4e-4, 1.6e-4, 1.8e-4, 2e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 700:
        electric_field = [1e-4, 1.2e-4, 1.4e-4, 1.6e-4, 1.8e-4, 2e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 800:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 900:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 1000:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/positron_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 5000
            elif j == 1:
                simulation_primary_electron_number = 3000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 1000
            else:
                simulation_primary_electron_number = 1000
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.positron_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()


def run_gamma(cell_length):
    air_density = 0.000526  # g/cm^3
    # simulation_primary_electron_number = 1000  # number of primary electrons
    simulation_feedback_particle_number = 1  # number of simulations for every feedback particle (positrons, gamma). Use > 1 for more statistics
    electron_energy_cut = 0.1  # MeV
    part_of_cell = 0.25  # in which part of cell electron birth is considered to be feedback
    if cell_length == 100:
        electric_field = [1e-4, 2e-4, 3e-4, 4e-4, 5e-4, 6e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 200:
        electric_field = [1e-4, 1.8e-4, 2.6e-4, 3.4e-4, 4.2e-4, 5e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 300:
        electric_field = [1e-4, 1.6e-4, 2.2e-4, 2.8e-4, 3.4e-4, 4e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 400:
        electric_field = [1e-4, 1.4e-4, 1.8e-4, 2.2e-4, 2.6e-4, 3e-4]
        file = open(ROOT_PATH + '../results/GAVgamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 1000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 500:
        electric_field = [1e-4, 1.3e-4, 1.6e-4, 1.9e-4, 2.2e-4, 2.5e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 600:
        electric_field = [1e-4, 1.2e-4, 1.4e-4, 1.6e-4, 1.8e-4, 2e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 700:
        electric_field = [1e-4, 1.2e-4, 1.4e-4, 1.6e-4, 1.8e-4, 2e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 800:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 900:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()
    elif cell_length == 1000:
        electric_field = [1.1e-4, 1.2e-4, 1.3e-4, 1.4e-4, 1.5e-4, 1.6e-4]
        file = open(ROOT_PATH + '../results/gamma_results_cell_length_' + str(cell_length) + '.txt', 'w')
        for j in range(len(electric_field)):
            if j == 0:
                simulation_primary_electron_number = 10000
            elif j == 1:
                simulation_primary_electron_number = 5000
            elif j == 2:
                simulation_primary_electron_number = 2000
            elif j == 3:
                simulation_primary_electron_number = 1000
            elif j == 4:
                simulation_primary_electron_number = 500
            else:
                simulation_primary_electron_number = 500
            file.write(str(electric_field[j] * 1e6) + ' ' + str(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field[j], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)) + '\n')
        file.close()


if __name__ == "__main__":
    main()


    # air_density = 0.000526  # g/cm^3
    # simulation_feedback_particle_number = 1  # number of simulations for every feedback particle (positrons, gamma). Use > 1 for more statistics
    # electron_energy_cut = 0.1  # MeV
    # part_of_cell = 0.25  # in which part of cell electron birth is considered to be feedback
    # cell_length = 400
    # electric_field = 2e-4
    # simulation_primary_electron_number = 100
    # print(feedback.gamma_feedback(part_of_cell=part_of_cell, electric_field=electric_field, air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut))
