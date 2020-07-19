"""Plot SV data"""

import csv
import matplotlib.pyplot as plt

# Read and parse CSV data
def readcsv(filename):
    """Read and parse Wireshark SV-CSV data"""
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data = []
        for row in spamreader:
            data.append(row[0].replace('"', '').split(','))

    # Unpack data into a dictionary
    parsedata = dict((k, []) for k in data[0])
    values = ['IA', 'IB', 'IC', 'IN', 'VA', 'VB', 'VC', 'VN']
    parsedata['value'] = dict((k, []) for k in values)

    for item in data[1:]:

        parsedata['No.'].append(int(item[0]))
        parsedata['Time'].append(float(item[1]))
        parsedata['Source'].append(item[2])
        parsedata['Destination'].append(item[3])
        parsedata['Protocol'].append(item[4])
        parsedata['Length'].append(item[5])
        parsedata['Time delta from previous displayed frame'].append(
            float(item[6]))
        parsedata['smpCnt'].append(int(item[7]))
        for key, val in zip(values, item[8:16]):
            parsedata['value'][key].append(float(val))
        parsedata['Info'].append(item[9])

    return parsedata

def plot(dictdata):
    """Plot SV data"""
    fig1, ax1 = plt.subplots()

    plt.figure(1)
    ax1.set_ylabel('smpCnt')
    ax1.set_xlabel('Packet No.')

    ax1.plot(dictdata['Time'], dictdata['value']['IA'], '-', color='blue',
             label='IA (A Primary)')

    plt.title(
        'Number Packets x Time delta from previous captured frame',
        fontsize=18,
        fontweight='bold')
    plt.legend(loc='upper right', fontsize=14)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print('Normal_traffic_NIC_COFFEE.csv')
    DATA = readcsv('Normal_traffic_NIC_COFFEE.csv')
    plot(DATA)