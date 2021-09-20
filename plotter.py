import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 15
import numpy as np

# filename = 'secondary_avalanches_zcoord.txt'
# f = open('results/' + filename)
#
# x = []
# # y = []
#
# for line in f.readlines():
#     list = line.split()
#     for i in range(len(list)):
#         x.append(float(list[0]))
#         # y.append(float(list[1]))
#
# # size = int(np.sqrt(len(x)))
# size = 10
# amount = np.zeros(size)
# z_coordinate = np.zeros(size)
#
# for i in range(size):
#     z_coordinate[i] = -250 + i * 500 / (size - 1)
#
# for i in range(size - 1):
#     for j in range(len(x)):
#         if z_coordinate[i] < x[j] and x[j] <= z_coordinate[i + 1]:
#             amount[i] = amount[i] + 1
#         amount[i] = amount[i] / 500 * (size - 1)
#
# plt.plot(z_coordinate, amount)
# plt.show()
# f.close()


# def diagram(file='', data='', particle='', xaxis=''):
#     f = open(file, 'r')
#     # data =[]
#     # for line in f.readlines():
#     #     list = line.split()
#     #     for i in range(len(list)):
#     #         data.append(float(list[0]))
#     data = np.loadtxt(file)
#     # data2 = np.loadtxt('./results/gammaEnergyDistribution.txt')
#     k = 0
#     for i in range(len(data)):
#         if data[i] > 0.5:
#             k = k + 1
#     rangge = int(np.sqrt(k) / 5)
#     # print(rangge)
#     min = 0.1
#     max = 10
#     # for i in range(len(data)):
#     #     data[i] = float(data[i])
#     #     # if data[i] < min:
#     #     #     min = data[i]
#     #     if data[i] > max:
#     #         max = data[i]
#
#     x = np.zeros(rangge - 1)
#     y = np.zeros(rangge - 1)
#     for i in range(rangge - 1):
#         x[i] = min + i * (max - min) / rangge
#         for j in range(len(data)):
#             if data[j] > 0.5:
#                 if x[i] < data[j] <= x[i] + (max - min) / rangge:
#                     y[i] = y[i] + 1
#         y[i] = y[i] / 100000
#         x[i] = x[i]
#     # print(x)
#     # for i in range(int(len(x) / 2)):
#     #     a = y[i]
#     #     y[i] = y[len(x) - i - 1]
#     #     y[len(x) - i - 1] = a
#     # print(y)
#     # x[rangge - 1] = max
#     # print(x)
#     directory = '/home/npm-geant/PycharmProjects/AntiDwyer/Global_Project/results/'
#     plt.xlabel(xaxis)
#     plt.ylabel('Number of ' + particle + 's')
#     plt.title('Diagram')
#     plt.plot(x, y)
#     plt.savefig(directory + particle + '_' + xaxis + '.pdf')
#     plt.close()
#     print(k)
#
# file = './results/ElectronEnergyOutput.txt'
# diagram(file=file, particle='electron', xaxis='Energy, MeV')
# directory = '/home/npm-geant/PycharmProjects/AntiDwyer/Global_Project/server_results/'
#
# cell_length = [200, 400]
# particles = ['positron', 'gamma']
#
# for particle in particles:
#     legen = []
#     plt.xlabel('Electric Field, kV/m')
#     plt.ylabel('Feedback Coefficient')
#     if particle == 'positron':
#         plt.title('Positron Feedback Coefficient')
#     else:
#         plt.title('Gamma Feedback Coefficient')
#     for cell_len in cell_length:
#         # file = open(directory + particle + '_' + str(cell_len) + '.txt')
#         # electric_field = []
#         # feedback = []
#         # mistake = []
#         # kok = 0
#         # for line in file.readlines():
#         #     list = line.split()
#         #     for i in range(len(list)):
#         #         electric_field.append(float(list[0]))
#         #         feedback.append(float(list[1]))
#         #         mistake.append(1 / np.sqrt(feedback[kok] * 10000) * feedback[kok])
#         #         kok = kok + 1
#         # file.close()
#         data = np.loadtxt(directory + particle + '_' + str(cell_len) + '.txt')
#         electric_field = np.zeros(len(data[:, 0]))
#         feedback = np.zeros(len(data[:, 0]))
#         mistake = np.zeros(len(data[:, 0]))
#         for ii in range(len(data[:, 0])):
#             electric_field[ii] = data[ii, 0]
#             feedback[ii] = data[ii, 1]
#             mistake[ii] = 1 / np.sqrt(feedback[ii] * 10000) * feedback[ii]
#         # print(feedback)
#         # print(mistake)
#         mew = range(100, 201, 1)
#         gav = np.interp(mew, electric_field, np.log10(feedback))
#         gavv = np.zeros(len(gav))
#         for ii in range(len(gav)):
#             gavv[ii] = 10 ** gav[ii]
#         mustache = np.interp(mew, electric_field, mistake)
#         if cell_len ==200:
#             plt.fill_between(mew, gavv + (-1) * mustache, gavv + mustache, linewidth=2, color='r')
#         elif cell_len == 400:
#             plt.fill_between(mew, gavv + (-1) * mustache, gavv + mustache, linewidth=2, color='b')
#         else:
#             plt.fill_between(mew, gavv + (-1) * mustache, gavv + mustache, linewidth=2, color='w', edgecolor='k')
#         legen.append('Cell length = '+str(cell_len))
#         # plt.legend('Cell length = ' + str(cell_len), loc='best')
#         plt.yscale('log')
#     plt.grid(True)  # lines of supportive grid
#     plt.legend(legen, loc='upper left')
#     plt.savefig(directory + particle + '_feedback.png')
#     plt.close()
#
# # particle = 'positron'
# # legen = []
# plt.xlabel('Electric Field, kV/m')
# plt.ylabel('Feedback Coefficient')
# if particle == 'positron':
#     plt.title('Positron angle distribution')
# else:
#     plt.title('Gamma Feedback Coefficient')
# for cell_len in cell_length:
    # file = open(directory + particle + '_' + str(cell_len) + '.txt')
    # electric_field = []
    # feedback = []
    # mistake = []
    # kok = 0
    # for line in file.readlines():
    #     list = line.split()
    #     for i in range(len(list)):
    #         electric_field.append(float(list[0]))
    #         feedback.append(float(list[1]))
    #         mistake.append(1 / np.sqrt(feedback[kok] * 10000) * feedback[kok])
    #         kok = kok + 1
    # file.close()
# data = np.loadtxt('results/PositronMomentumOutput.txt')
# bins = int(np.sqrt(len(data)))
# x = np.zeros(bins)
# y = np.zeros(bins)
# for i in range(bins):
#     x[i] = 0 + i * 180 / bins
# for i in range(bins - 1):
#     for j in range(len(data)):
#         if x[i] <= np.arccos(-data[j]) < x[i + 1]:
#             y[i] = y[i] + 1
# for i in range(bins):
#     y[i] = y[i] / 10000 / 180 * bins
#
# # plt.legend('Cell length = ' + str(cell_len), loc='best')
# # plt.grid(True)  # lines of supportive grid
# plt.savefig(directory + particle + '_angle.png')
# plt.close()



# gain = np.zeros(len(electric_field))
    # there are two functions for different feedback in gain_coefficient: positron_feedback and gamma_feedback. they calculate feedback coefficient for used parameters
    # for i in range(len(electric_field)):
    #     gain[i] = gain_coefficient.positron_feedback(electric_field=electric_field[i], air_density=air_density, cell_length=cell_length, ROOT_PATH=ROOT_PATH, simulation_primary_electron_number=simulation_primary_electron_number, simulation_positron_number=simulation_feedback_particle_number, electron_energy_cut=electron_energy_cut)
    # # f = open(ROOT_PATH + '../results/results.txt', 'w')
    # # f.close()
    # plt.title('Positron Feedback Coefficient')
    # plt.xlabel('Electric Field, kV/m')
    # plt.ylabel('Feedback coefficient')
    # plt.plot(electric_field, gain)
    # plt.legend('Density = 0.526 kg/m**3', loc='upper right')
    # plt.grid(True)  # lines of supportive grid
    # directory_export = ROOT_PATH + '../results/positron.jpeg'
    # plt.savefig(directory_export)
    # plt.close()
