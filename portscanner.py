from prettytable import PrettyTable

from service.NetworkService import NetworkService
from util.Logger import Logger

if __name__ == "__main__":


    devices = NetworkService.getAllDevices()
    devices.sort(key=lambda x: int(x.ipAddress.split(".")[-1]))

    table = PrettyTable(["IP Address", "Open Ports"])
    for device in devices:
        table.add_row([device.ipAddress, ", ".join(sorted(device.openPorts, key=lambda x: int(x)))])

    Logger.logGrey("\n")
    Logger.logYellow(table)
