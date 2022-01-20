class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = []

    def collectPackage(self, pk):
        if (self.location == pk.office) and (len(self.packages) < self.size):
            for i in self.packages:
                if i.id == pk.id:
                    pk.collected = True
            if pk.collected == False:
                self.packages.append(pk)
                pk.collected = True

    def deliverOnePackage(self, pk):
        if self.location == pk.address:
            for i in range(len(self.packages)):
                if self.packages[i].id == pk.id:
                    self.packages.pop(i)
                    pk.delivered = True

    def deliverPackages(self):
        for pk in self.packages:
            if pk.address == self.location:
                pk.delivered = True
                self.packages.pop(self.packages.index(pk))

    def removePackage(self, pk):
        i = 0
        while i < len(self.packages):
            if self.packages[i].id == pk.id:
                pk.office = self.location
                self.packages.pop(i)
                pk.collected = False
            i += 1

    def driveTo(self, loc):
        self.location = loc

    def getPackagesIds(self):
        packageList = []
        for package in self.packages:
            packageList.append(package.id)
        return packageList



