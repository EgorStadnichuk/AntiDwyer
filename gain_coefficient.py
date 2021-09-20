import generator
import gain_calculator

import numpy as np
import os
import shutil

electron_zcoord_file = 'ElectronZCoordOutput.txt'
electron_energy_file = 'ElectronEnergyOutput.txt'
electron_momentum_file = 'ElectronMomentumOutput.txt'
secondary_electron_zcoord_file = 'ElectronZCoordOutput.txt'
secondary_electron_energy_file = 'ElectronEnergyOutput.txt'
secondary_electron_momentum_file = 'ElectronMomentumOutput.txt'


class Feedback:
    def __init__(self):
        self.folder = 0

    def positron_feedback(self,
                          ROOT_PATH,
                          physics='G4EmStandartPhysics_option4',
                          part_of_cell=0.5,
                          electric_field=1e-4,
                          cell_length=400,
                          primary_electron_energy=10,
                          air_density=0.000526,
                          simulation_primary_electron_number=1000,
                          simulation_positron_number=1,
                          electron_energy_cut=0.1,
                          zcoord=200):
        bool = True
        while bool:
            ROOT_PATH1 = ROOT_PATH + str(self.folder) + '/'
            self.folder = self.folder + 1
            bool = os.path.exists(ROOT_PATH1)
        ROOT_PATH = ROOT_PATH1
        os.mkdir(ROOT_PATH)

        log_file = open(ROOT_PATH + 'log.txt', 'w')
        log_file.write('feedback particle: positron' + '\n' + 'physics: ' + physics + '\n' + 'electric field (MV per mm): ' + str(
            electric_field) + '\n' + 'cell length (m): ' + str(cell_length) + '\n' + 'air density (g per cm3): ' + str(
            air_density) + '\n' + 'primary electron energy (MeV):' + str(
            primary_electron_energy) + '\n' + 'part of cell for feedback: ' + str(
            part_of_cell) + '\n' + 'electron energy cut (MeV): ' + str(electron_energy_cut) + '\n' + 'electron start coordinate z: ' + str(cell_length / 2 - zcoord) + '\n' + 'number of primary electrons: ' + str(
            simulation_primary_electron_number) + '\n')

        if os.path.exists('e-'):
            shutil.rmtree('e-')
        if os.path.exists('positron_output'):
            shutil.rmtree('positron_output')
        if os.path.exists('output'):
            shutil.rmtree('output')
        if os.path.exists('e+'):
            shutil.rmtree('e+')

        positron_zcoord_file = 'PositronZCoordOutput.txt'
        positron_energy_file = 'PositronEnergyOutput.txt'
        positron_momentum_file = 'PositronMomentumOutput.txt'
        electric_field = str(electric_field)
        primary_electron_energy = [str(primary_electron_energy)]
        cell_length = str(cell_length)
        air_density = str(air_density)
        simulation_positron_number = str(simulation_positron_number)
        simulation_primary_electron_number = str(simulation_primary_electron_number)

        os.chdir(ROOT_PATH)
        os.mkdir('output')
        generator.main(physics=physics, ROOT_PATH=ROOT_PATH, particle='e-', electric=electric_field,
                       cell_length=cell_length, energy=primary_electron_energy, momentum=['-1'],
                       zcoord=[str(zcoord)], air_density=air_density,
                       simulation_particles_number=simulation_primary_electron_number)

        os.chdir(ROOT_PATH)
        os.renames('output', 'positron_output')
        # shutil.rmtree('output')
        positron_path = ROOT_PATH + 'positron_output/'

        if os.path.exists(positron_path + positron_zcoord_file) and os.stat(
                        positron_path + positron_zcoord_file).st_size != 0:
            positron_zcoord_first = np.loadtxt(positron_path + positron_zcoord_file)
            positron_energy_first = np.loadtxt(positron_path + positron_energy_file)
            positron_momentum_first = np.loadtxt(positron_path + positron_momentum_file)
        else:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('positron_output'):
                shutil.rmtree('positron_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('e+'):
                shutil.rmtree('e+')
            print('NO POSITRONS!!!')
            return 0

        number_of_positrons = 0
        # print(positron_zcoord_first)

        try:
            if len(positron_zcoord_first) != 0:
                for i in range(len(positron_energy_first)):
                    # if positron_zcoord_first[i] > -1 * float(cell_length) / 2:
                    number_of_positrons = number_of_positrons + 1
            else:
                number_of_positrons = 0
        except TypeError:
            number_of_positrons = 0

        if number_of_positrons == 0:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('positron_output'):
                shutil.rmtree('positron_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('e+'):
                shutil.rmtree('e+')
            print('NO POSITRONS!!!')
            return 0

        # print(number_of_positrons)
        positron_zcoord = []
        positron_energy = []
        positron_momentum = []

        # plotter.diagram(positron_path + positron_energy_file, 'positron', 'Energy, MeV')
        # plotter.diagram(positron_path + positron_momentum_file, 'positron', 'Momentum Direction')

        for i in range(len(positron_energy_first)):
            # if positron_zcoord_first[i] > -1 * float(cell_length) / 2:
            positron_zcoord.append(str(positron_zcoord_first[i]))
            positron_energy.append(str(positron_energy_first[i]))
            positron_momentum.append(str(positron_momentum_first[i]))

        os.chdir(ROOT_PATH)

        log_file.write('number of positrons: ' + str(len(positron_zcoord)) + '\n')

        os.mkdir('output')
        # for i in range(number_of_positrons):
        generator.main(physics='G4EmStandartPhysics_option4',
                       ROOT_PATH=ROOT_PATH,
                       particle='e+',
                       electric=str(electric_field),
                       cell_length=cell_length,
                       energy=positron_energy,
                       momentum=positron_momentum,
                       zcoord=positron_zcoord,
                       air_density=air_density,
                       simulation_particles_number=simulation_positron_number)
        os.chdir(ROOT_PATH)
        # shutil.rmtree('e+')

        # plotter.diagram(ROOT_PATH + 'output/' + electron_energy_file, 'electron', 'Energy, MeV')
        # plotter.diagram(ROOT_PATH + 'output/' + electron_momentum_file, 'electron', 'Momentum Direction')

        os.renames('output', 'secondary_electron_output')
        # shutil.rmtree('output')
        secondary_electron_path = ROOT_PATH + 'secondary_electron_output/'

        if os.path.exists(secondary_electron_path + secondary_electron_zcoord_file) and os.stat(
                        secondary_electron_path + secondary_electron_zcoord_file).st_size != 0:
            secondary_electron_zcoord_first = np.loadtxt(secondary_electron_path + secondary_electron_zcoord_file)
            secondary_electron_energy_first = np.loadtxt(secondary_electron_path + secondary_electron_energy_file)
            secondary_electron_momentum_first = np.loadtxt(secondary_electron_path + secondary_electron_momentum_file)
        else:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('positron_output'):
                shutil.rmtree('positron_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('e+'):
                shutil.rmtree('e+')
            print('NO POSITRONS!!!')
            return 0

        number_of_secondary_electrons = 0
        # print(positron_zcoord_first)

        try:
            if len(secondary_electron_zcoord_first) != 0:
                for i in range(len(secondary_electron_energy_first)):
                    # if positron_zcoord_first[i] > -1 * float(cell_length) / 2:
                    number_of_secondary_electrons = number_of_secondary_electrons + 1
            else:
                number_of_secondary_electrons = 0
        except TypeError:
            number_of_secondary_electrons = 0

        if number_of_secondary_electrons == 0:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('positron_output'):
                shutil.rmtree('positron_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('e+'):
                shutil.rmtree('e+')
            print('NO POSITRONS!!!')
            return 0

        # print(number_of_positrons)
        secondary_electron_zcoord = []
        secondary_electron_energy = []
        secondary_electron_momentum = []

        # plotter.diagram(positron_path + positron_energy_file, 'positron', 'Energy, MeV')
        # plotter.diagram(positron_path + positron_momentum_file, 'positron', 'Momentum Direction')

        for i in range(len(secondary_electron_energy_first)):
            # if secondary_electron_zcoord_first[i] > -1 * float(cell_length) / 2:
            secondary_electron_zcoord.append(str(secondary_electron_zcoord_first[i]))
            secondary_electron_energy.append(str(secondary_electron_energy_first[i]))
            secondary_electron_momentum.append(str(secondary_electron_momentum_first[i]))

        os.chdir(ROOT_PATH)

        log_file.write('number of secondary electrons: ' + str(len(secondary_electron_zcoord)) + '\n')

        shutil.rmtree('e-')
        os.mkdir('output')
        # for i in range(number_of_positrons):
        generator.main(physics='G4EmStandartPhysics_option4',
                       ROOT_PATH=ROOT_PATH,
                       particle='e-',
                       electric=str(electric_field),
                       cell_length=cell_length,
                       energy=secondary_electron_energy,
                       momentum=secondary_electron_momentum,
                       zcoord=secondary_electron_zcoord,
                       air_density=air_density,
                       simulation_particles_number=1)

        os.chdir(ROOT_PATH)

        gamma_zcoord_file = 'GammaZCoordOutput.txt'
        # gamma_energy_file = 'GammaEnergyOutput.txt'
        gamma_momentum_file = 'GammaMomentumOutput.txt'

        secondary_gamma_path = ROOT_PATH + 'output/'

        if os.path.exists(secondary_gamma_path + gamma_zcoord_file) and os.stat(secondary_gamma_path + gamma_zcoord_file).st_size != 0:
            secondary_gamma_zcoord_first = np.loadtxt(secondary_gamma_path + gamma_zcoord_file)
            secondary_gamma_momentum_first = np.loadtxt(secondary_gamma_path + gamma_momentum_file)
        else:
            # if os.path.exists('e-'):
            #     shutil.rmtree('e-')
            # if os.path.exists('gamma_output'):
            #     shutil.rmtree('gamma_output')
            # if os.path.exists('output'):
            #     shutil.rmtree('output')
            # if os.path.exists('gamma'):
            #     shutil.rmtree('gamma')
            print('NO GAMMA!!!')
            return 0

        primary_gamma_path = ROOT_PATH + 'positron_output/'

        if os.path.exists(primary_gamma_path + gamma_zcoord_file) and os.stat(primary_gamma_path + gamma_zcoord_file).st_size != 0:
            primary_gamma_zcoord_first = np.loadtxt(primary_gamma_path + gamma_zcoord_file)
            primary_gamma_momentum_first = np.loadtxt(primary_gamma_path + gamma_momentum_file)
        else:
            # if os.path.exists('e-'):
            #     shutil.rmtree('e-')
            # if os.path.exists('gamma_output'):
            #     shutil.rmtree('gamma_output')
            # if os.path.exists('output'):
            #     shutil.rmtree('output')
            # if os.path.exists('gamma'):
            #     shutil.rmtree('gamma')
            print('NO GAMMA!!!')
            return 0

        # positron_gain_coefficient = gain_calculator.gain(part_of_cell=part_of_cell,
        #                                                          ROOT_PATH=ROOT_PATH,
        #                                                          electric=electric_field,
        #                                                          number_of_positrons=number_of_positrons,
        #                                                          cell_length=cell_length,
        #                                                          air_density=air_density,
        #                                                          simulation_positron_number=simulation_positron_number,
        #                                                          simulation_primary_electron_number=simulation_primary_electron_number,
        #                                                          electron_energy_cut=electron_energy_cut)



        # if os.path.exists('e-'):
        #    shutil.rmtree('e-')
        # if os.path.exists('positron_output'):
        #    shutil.rmtree('positron_output')
        # if os.path.exists('output'):
        #    shutil.rmtree('output')
        # if os.path.exists('e+'):
        #    shutil.rmtree('e+')
        # if os.path.exists(ROOT_PATH):
        #    shutil.rmtree(ROOT_PATH)
        number_of_secondary_gamma = 0
        for i in range(len(secondary_gamma_momentum_first)):
            if secondary_gamma_momentum_first[i] < 0:
                number_of_secondary_gamma = number_of_secondary_gamma + 1
        number_of_primary_gamma = 0
        for i in range(len(primary_gamma_momentum_first)):
            if primary_gamma_momentum_first[i] < 0:
                number_of_primary_gamma = number_of_primary_gamma + 1

        print(number_of_primary_gamma)
        print(number_of_secondary_gamma)

        positron_feedback_coefficient = float(number_of_secondary_gamma) / float(number_of_primary_gamma)

        log_file.write('number of primary gamma: ' + str(len(primary_gamma_zcoord_first)))
        log_file.write('feedback coefficient: ' + str(positron_feedback_coefficient))
        log_file.close()

        return positron_feedback_coefficient

    def gamma_feedback(self,
                       ROOT_PATH,
                       physics='G4EmStandartPhysics_option4',
                       part_of_cell=0.5,
                       electric_field=1e-4,
                       cell_length=400,
                       primary_electron_energy=3,
                       air_density=0.000526,
                       simulation_primary_electron_number=1000,
                       simulation_positron_number=100,
                       electron_energy_cut=0.1,
                       zcoord=200):
        bool = True
        while bool:
            ROOT_PATH1 = ROOT_PATH + str(self.folder) + '/'
            self.folder = self.folder + 1
            bool = os.path.exists(ROOT_PATH1)
        ROOT_PATH = ROOT_PATH1
        os.mkdir(ROOT_PATH)

        log_file = open(ROOT_PATH + 'log.txt', 'w')
        log_file.write('feedback particle: gamma' + '\n' + 'physics: ' + physics + '\n' + 'electric field (MV per mm): ' + str(
            electric_field) + '\n' + 'cell length (m): ' + str(cell_length) + '\n' + 'air density (g per cm3): ' + str(
            air_density) + '\n' + 'primary electron energy (MeV):' + str(
            primary_electron_energy) + '\n' + 'part of cell for feedback: ' + str(
            part_of_cell) + '\n' + 'electron energy cut (MeV): ' + str(electron_energy_cut) + '\n' + 'electron start coordinate z: ' + str(cell_length / 2 - zcoord) + '\n' + 'number of primary electrons: ' + str(
            simulation_primary_electron_number) + '\n')

        os.chdir(ROOT_PATH)
        if os.path.exists('e-'):
            shutil.rmtree('e-')
        if os.path.exists('gamma_output'):
            shutil.rmtree('gamma_output')
        if os.path.exists('output'):
            shutil.rmtree('output')
        if os.path.exists('gamma'):
            shutil.rmtree('gamma')

        gamma_zcoord_file = 'GammaZCoordOutput.txt'
        gamma_energy_file = 'GammaEnergyOutput.txt'
        gamma_momentum_file = 'GammaMomentumOutput.txt'
        electric_field = str(electric_field)
        primary_electron_energy = [str(primary_electron_energy)]
        cell_length = str(cell_length)
        air_density = str(air_density)
        simulation_positron_number = str(simulation_positron_number)
        simulation_primary_electron_number = str(simulation_primary_electron_number)

        os.chdir(ROOT_PATH)
        os.mkdir('output')
        generator.main(physics=physics,
                       ROOT_PATH=ROOT_PATH,
                       particle='e-',
                       electric=electric_field,
                       cell_length=cell_length,
                       energy=primary_electron_energy,
                       momentum=['-1'],
                       zcoord=[str(zcoord)],
                       air_density=air_density,
                       simulation_particles_number=simulation_primary_electron_number)

        os.chdir(ROOT_PATH)
        os.renames('output', 'gamma_output')
        # shutil.rmtree('output')
        gamma_path = ROOT_PATH + 'gamma_output/'

        if os.path.exists(gamma_path + gamma_zcoord_file) and os.stat(gamma_path + gamma_zcoord_file).st_size != 0:
            gamma_zcoord_first = np.loadtxt(gamma_path + gamma_zcoord_file)
            gamma_energy_first = np.loadtxt(gamma_path + gamma_energy_file)
            gamma_momentum_first = np.loadtxt(gamma_path + gamma_momentum_file)
        else:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('gamma_output'):
                shutil.rmtree('gamma_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('gamma'):
                shutil.rmtree('gamma')
            print('NO GAMMA!!!')
            return 0

        number_of_gamma = 0
        # print(gamma_zcoord_first)
        try:
            if len(gamma_zcoord_first) != 0:
                for i in range(len(gamma_energy_first)):
                    if gamma_zcoord_first[i] < float(cell_length) * (part_of_cell - 0.5) and gamma_energy_first[i] >= electron_energy_cut:
                        number_of_gamma = number_of_gamma + 1
            else:
                number_of_gamma = 0
        except TypeError:
            number_of_gamma = 0

        if number_of_gamma == 0:
            if os.path.exists('e-'):
                shutil.rmtree('e-')
            if os.path.exists('gamma_output'):
                shutil.rmtree('gamma_output')
            if os.path.exists('output'):
                shutil.rmtree('output')
            if os.path.exists('gamma'):
                shutil.rmtree('gamma')
            print('NO GAMMA!!!')
            return 0

        # print(number_of_gamma)
        gamma_zcoord = []
        gamma_energy = []
        gamma_momentum = []
        j = 0
        for i in range(len(gamma_energy_first)):
            if gamma_zcoord_first[i] < float(cell_length) * (part_of_cell - 0.5) and gamma_energy_first[i] >= electron_energy_cut:
                gamma_zcoord.append(str(gamma_zcoord_first[i]))
                gamma_energy.append(str(gamma_energy_first[i]))
                gamma_momentum.append(str(gamma_momentum_first[i]))

        # plotter.diagram(file=gamma_path + gamma_energy_file, data=gamma_energy, particle='gamma', xaxis='Energy, MeV')
        # plotter.diagram(file=gamma_path + gamma_momentum_file, data=gamma_momentum, particle='gamma', xaxis='Momentum Direction')

        os.chdir(ROOT_PATH)

        log_file.write('number of gamma: ' + str(len(gamma_zcoord)) + '\n')

        os.mkdir('output')
        # for i in range(number_of_gamma):
        generator.main(physics='G4EmStandartPhysics_option4',
                       ROOT_PATH=ROOT_PATH,
                       particle='gamma',
                       electric=str(electric_field),
                       cell_length=cell_length,
                       energy=gamma_energy,
                       momentum=gamma_momentum,
                       zcoord=gamma_zcoord,
                       air_density=air_density,
                       simulation_particles_number=simulation_positron_number)
        os.chdir(ROOT_PATH)
        # shutil.rmtree('gamma')

        # plotter.diagram(file=ROOT_PATH + 'output/' + electron_energy_file, data=np.loadtxt(ROOT_PATH + 'output/' + electron_energy_file),particle='electron', xaxis='Energy, MeV')
        # plotter.diagram(file=ROOT_PATH + 'output/' + electron_momentum_file, particle='electron', xaxis='Momentum Direction', data=np.loadtxt(ROOT_PATH + 'output/' + electron_momentum_file))

        os.chdir(ROOT_PATH)
        gamma_gain_coefficient = gain_calculator.gain(part_of_cell=part_of_cell,
                                                              ROOT_PATH=ROOT_PATH,
                                                              electric=electric_field,
                                                              number_of_positrons=number_of_gamma,
                                                              cell_length=cell_length,
                                                              air_density=air_density,
                                                              simulation_positron_number=simulation_positron_number,
                                                              simulation_primary_electron_number=simulation_primary_electron_number,
                                                              electron_energy_cut=electron_energy_cut)
        # if os.path.exists('e-'):
        #     shutil.rmtree('e-')
        # if os.path.exists('gamma_output'):
        #     shutil.rmtree('gamma_output')
        # if os.path.exists('output'):
        #     shutil.rmtree('output')
        # if os.path.exists('gamma'):
        #     shutil.rmtree('gamma')
        # os.chdir(ROOT_PATH + '../')
        # if os.path.exists(ROOT_PATH):
        #     shutil.rmtree(ROOT_PATH)

        log_file.write('feedback coefficient: ' + str(gamma_gain_coefficient))
        log_file.close()

        return gamma_gain_coefficient
