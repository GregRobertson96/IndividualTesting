import csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class ReadSmoothieFile:
    def attributesFile(self, menuName):
        readCSVFile = ReadCSVFile()
        smoothieMenu = readCSVFile.getConfig(entitiesFolder, menuName + ".csv")
        return smoothieMenu