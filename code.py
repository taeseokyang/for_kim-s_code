import random
LENGTH = 20


class GeneticAlgorithm:
    # set parameter
    def __init__(self, populNum, geneNum, selRatio, mutaNum, chromosomes, nowGeneration):
        self.populNum = populNum  # population number
        self.geneNum = geneNum  # generation number
        # set number of chromosome which crossover
        self.selRatio = selRatio
        self.mutaNum = mutaNum  # Number of bit
        self.chromoLists = chromosomes
        self.fScoreLists = {}
        self.parent1 = 0
        self.parent2 = 0
        self.child1 = []
        self.child2 = []
        print(f"Generation {nowGeneration + 1}")

    def CreateChromo(self):
        colsum = 0
        for i in range(self.populNum):
            for k in range(LENGTH):
                self.chromoLists[i][k] = random.randint(0, 1)
                colsum = colsum + self.chromoLists[i][k]
            # Sum fitness dictionary (index:fitness)
            self.fScoreLists[i] = colsum
            colsum = 0

    def printChromo(self):
        for i in range(0, self.populNum):
            print(
                f"0{i+1}: {''.join(map(str, self.chromoLists[i]))} (f:{sum(self.chromoLists[i])})")
            # Update, When Generation is more than 1.
            self.fScoreLists[i] = sum(self.chromoLists[i])

    def Tournament(self):
        sorted_dict = list(sorted(self.fScoreLists.items(),
                                  key=lambda x: x[1], reverse=True))

        number = int(self.populNum*self.selRatio)

        # parent1, 1 Tournament
        if (sorted_dict[0][1] > sorted_dict[1][1]):
            self.parent1 = self.chromoLists[sorted_dict[0][0]]
        else:
            self.parent1 = self.chromoLists[sorted_dict[1][0]]
        # parent2, 2 Tournament
        if (sorted_dict[2][1] > sorted_dict[3][1]):
            self.parent2 = self.chromoLists[sorted_dict[2][0]]
        else:
            self.parent2 = self.chromoLists[sorted_dict[3][0]]

        print(
            f"Best: {''.join(map(str, self.parent1))} (f:{sum(self.parent1)}) \n")
        print("- Tournament Selection")
        print(f"Choose {number} populations for tournament.")
        print(
            f"Parent1: {''.join(map(str, self.parent1))} (f:{sum(self.parent1)})")
        print(
            f"Parent2: {''.join(map(str, self.parent2))} (f:{sum(self.parent2)})\n")

    def Crossover(self):
        cut = random.randint(1, self.populNum - 1)

        for i in range(LENGTH):
            if i < cut:
                self.child1.append(self.parent1[i])
                self.child2.append(self.parent2[i])
            else:
                self.child1.append(self.parent2[i])
                self.child2.append(self.parent1[i])
        print("- One point crossover")
        print(f"Cut point: {cut}")
        print(
            f"Child1: {''.join(map(str, self.child1))} (f:{sum(self.child1)})")
        print(
            f"Child2: {''.join(map(str, self.child2))} (f:{sum(self.child2)}) \n")

    def Mutation(self):
        mutationRate = int(LENGTH*self.mutaNum)
        index = []
        for i in range(mutationRate):
            index.append(random.randint(0, LENGTH))

        for i in range(0, mutationRate):
            if (int(self.child1[index[i]])):
                self.child1[i] = 0
            else:
                self.child1[i] = 1

            if (int(self.child2[index[i]])):
                self.child2[i] = 0
            else:
                self.child2[i] = 1

        print("- Mutation")
        print(f"Number of bit-flip {mutationRate}")
        print(
            f"Child1: {''.join(map(str, self.child1))} (f:{sum(self.child1)})")
        print(
            f"Child2: {''.join(map(str, self.child2))} (f:{sum(self.child2)})\n")

    def Replace(self):
        sorted_dict = list(sorted(self.fScoreLists.items(),
                                  key=lambda x: x[1], reverse=False))
        # Change population with lowest fitness
        self.chromoLists[sorted_dict[0][0]] = self.child1
        self.chromoLists[sorted_dict[1][0]] = self.child2

        print("- Replace")
        print(f"Replace population 0{sorted_dict[0][0] + 1} with child1.")
        print(f"Replace population 0{sorted_dict[1][0] + 1} with child2.\n")

        return self.chromoLists


if __name__ == "__main__":

    userGenerate = int(input("Write a generation number: "))
    userPopulation = int(input("Write a population number: "))
    userTournaRatio = float(
        input("Write a tournament selection ratio number: "))
    userMutaRatio = float(input("Write a mutation ratio number: "))

    result = [
        [0 for col in range(LENGTH)] for row in range(userPopulation)]

    #  __init__(self, populNum, geneNum, selRatio, mutaNum, chromosomes, nowGeneration)
    for i in range(userGenerate):
        if i == 0:
            test = GeneticAlgorithm(
                userPopulation, userGenerate, userTournaRatio, userMutaRatio, result, i)
            test.CreateChromo()
            test.printChromo()
            test.Tournament()
            test.Crossover()
            test.Mutation()
            result = test.Replace()
        else:
            test = GeneticAlgorithm(
                userPopulation, userGenerate, userTournaRatio, userMutaRatio, result, i)
            test.printChromo()
            test.Tournament()
            test.Crossover()
            test.Mutation()
            result = test.Replace()