import xml.etree.ElementTree as ET
from string import Template
import sys, os
import shutil
import subprocess
import numpy
from multiprocessing import Pool


# ROOT_PATH = '/home/npm-geant/PycharmProjects/AntiDwyer/Global_Project/geant_simulations/'
# GDML_PATH = ROOT_PATH + 'default.gdml'
# GPS_PATH = ROOT_PATH + 'gps.mac'
# INIT_PATH = ROOT_PATH + 'init.mac'
# PROGRAM_GEANT4_PATH = ROOT_PATH
# files = [GDML_PATH, GPS_PATH]


def createFile(particle=None,
               electric=None,
               cell_length=None,
               energy=None,
               momentum=None,
               zcoord=None,
               air_density=None,
               ROOT_PATH=None,
               GDML_PATH=None,
               GPS_PATH=None,
               INIT_PATH=None,
               simulation_particles_number=None):
    # runPath = []
    dictTemp = {'particle': None, 'cell_length': None, 'ElectricField': None, 'primary': None, 'energy': None, 'momentum': None, 'momentum_y': None, 'zcoord': None, 'air_density': None}
    # materialScreen = ["G4_Fe", "G4_C"]
    fgdml = open(GDML_PATH)
    fgps = open(GPS_PATH)
    finit = open(INIT_PATH)
    init = finit.read()
    gdml = fgdml.read()
    gps = fgps.read()
    finit.close()
    fgdml.close()
    fgps.close()
    os.chdir(ROOT_PATH)
    os.mkdir(particle)
    path = ROOT_PATH + particle + '/'
    dictTemp['ElectricField'] = electric
    dictTemp['cell_length'] = cell_length
    dictTemp['particle'] = particle
    # dictTemp['energy'] = energy
    # dictTemp['momentum'] = momentum
    # dictTemp['zcoord'] = zcoord
    dictTemp['air_density'] = air_density
    # if particle == 'e-':
    #     if float(electric) >= 0.4e-4 and float(electric) < 1e-4:
    #         primary = '10000'
    #     elif float(electric) >= 1e-4 and float(electric) < 1.2e-4:
    #         primary = '5000'
    #     elif float(electric) >= 1.2e-4 and float(electric) < 1.6e-4:
    #         primary = '1000'
    #     elif float(electric) >= 1.6e-4 and float(electric) < 1.8e-4:
    #         primary = '500'
    #     elif float(electric) >= 1.8e-4 and float(electric) < 2.2e-4:
    #         primary = '200'
    #     else:
    #         primary = '100'
    # elif particle == 'e+':
    #     primary = '100'
    dictTemp['primary'] = simulation_particles_number
    # runPath.append(path)
    os.mkdir(path + 'gdml')
    os.mkdir(path + 'gps')
    os.mkdir(path + 'mac')
    with open(path + 'gdml/default.gdml', 'w') as fgdml, open(path + 'mac/init.mac', 'w') as finit:
        tempGDML = Template(gdml)
        tempINIT = Template(init)
        fgdml.write(tempGDML.safe_substitute(dictTemp))
        finit.write(tempINIT.safe_substitute(dictTemp))
    with open(path + 'gps/gps.mac', 'w') as fgps:
        for i in range(len(energy)):
            dictTemp['energy'] = energy[i]
            dictTemp['momentum'] = momentum[i]
            dictTemp['momentum_y'] = str(numpy.sqrt(1 - numpy.square(float(momentum[i]))))
            dictTemp['zcoord'] = zcoord[i]
            tempGPS = Template(gps)
            fgps.write(tempGPS.safe_substitute(dictTemp))
            fgps.write('/run/beamOn ' + str(simulation_particles_number) + '\n')
    # os.mkdir(path + 'output')

    # with open('path.txt', 'w') as fout:
    #     for path in runPath:
    #         fout.write(path+'\n')
    return path


def runSimulations(runPath, PROGRAM_GEANT4_PATH, exe_name):
    print(runPath)
    os.chdir(PROGRAM_GEANT4_PATH)
    shutil.copy(exe_name, runPath)
    os.chdir(runPath)
    p = subprocess.Popen(runPath + exe_name + ' -d -g ./gdml/default.gdml -i ./mac/init.mac -gps ./gps/gps.mac', shell=True)
    p.wait()
    return 0


# def countPositrons(runPath):
#    print(runPath)
#    os.chdir(runPath + '/output')
#    i = 0
#    with open('PositronZCoord.txt') as fin:
#        for line in enumerate(fin.readlines()):
#            i = i + 1
#    i = i - 1


def readPath():
    with open('path.txt') as fin:
        paths = fin.read()
    return paths.splitlines()


def main(physics='G4EmStandartPhysics_option4',
         ROOT_PATH=None,
         particle=None,
         electric=None,
         cell_length=None,
         energy=None,
         momentum=None,
         zcoord=None,
         air_density=None,
         simulation_particles_number=None):
    # currPath = os.getcwd()
    # print(currPath)
    # subprocess.call('rm -rf *', shell=True)
    GDML_PATH = ROOT_PATH + '../default.gdml'
    GPS_PATH = ROOT_PATH + '../gps.mac'
    INIT_PATH = ROOT_PATH + '../init.mac'
    # PROGRAM_GEANT4_PATH = ROOT_PATH
    # files = [GDML_PATH, GPS_PATH]
    if particle == 'e-' or particle == 'electron':
        exe_name = 'positron_gamma_birth.exe'
    else:
        exe_name = 'electron_birth.exe'
    path = createFile(particle,
                      electric,
                      cell_length,
                      energy,
                      momentum,
                      zcoord,
                      air_density,
                      ROOT_PATH,
                      GDML_PATH,
                      GPS_PATH,
                      INIT_PATH,
                      simulation_particles_number)
    print(runSimulations(path, ROOT_PATH + '../' + physics + '/', exe_name))
    # for i in range(len(paths)):
    #     paths[i] = ROOT_PATH + paths[i][:-1]
    # for i in range(1):
    # with Pool(os.cpu_count()) as p:
    #     for i in range(len(paths)):
    #         print(p.runSimulations(paths[i], PROGRAM_GEANT4_PATH, exe_name))
        # print(p.map(countPositrons, paths))
    os.chdir(ROOT_PATH)
    return 0


# 1) описание метода моделирования, основные особенности, зашитые
# возможности, описание используемой физической модели (1 — 1 1⁄2
# страница).
# 2) Моделирование изображений нескольких облучаемых объектов: шарик
# (железо, кальций, стекло) и цилиндр (отношение радиуса к высоте 1/8, те же
# материалы) за плоской преградой (железо, графит) в воздухе и в воде для 3-4
# значений энергий в диапазоне 100 — 500 кэВ. Источник излучения плоский
# монохроматический. Значение интенсивности подбирается из соображений
# различимости конечного изображения (порядка Е7).
# 3) Аналитический пересчет размеров изображения из случая шарика с
# диаметром 10 см на диаметр 200 мк.

# dictTemp['ElectricField'] = field
#         if field == '1e-4':
#             dictTemp['Primary'] = '50000'
#         elif field == '1.2e-4' or field == '1.4e-4':
#             dictTemp['Primary'] = '10000'
#         elif field == '1.6e-4' or field == '1.8e-4':
#             dictTemp['Primary'] = '500'
#         elif field == '2e-4':
#             dictTemp['Primary'] = '200'
#         # os.mkdir('/home/npm-geant/CLionProjects/AntiDwyer/PositronsFromElectricField/Scripts/' + dictTemp['Primary'] + 'primary')
#         os.mkdir('/home/npm-geant/CLionProjects/AntiDwyer/PositronsFromElectricField/Scripts/' + dictTemp['Primary'] + 'primary/' + field)
#         pathM = '/home/npm-geant/CLionProjects/AntiDwyer/PositronsFromElectricField/Scripts/' + dictTemp['Primary'] + 'primary/' + field
