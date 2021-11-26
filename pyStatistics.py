from statistics import median

class stats:
    def __init__(self, lst):
        self.lst = lst
        self.sortedList = sorted(lst)
    def average(self):
        return (sum(self.lst) / len(self.lst))
    def median(self):
        return median(self.lst)
    def firstQuartile(self):
        upToMedian = []
        for element in self.sortedList:
            if element < self.median():
                upToMedian.append(element)
        return stats(upToMedian).median()
    def thirdQuartile(self):
        fromMedian = []
        for element in self.sortedList:
            if element > self.median():
                fromMedian.append(element)
        return stats(fromMedian).median()
    def mode(self):
        modes = []
        occurrences = {}
        maximumOccurrence = 0
        for element in self.lst:
            if element not in occurrences:
                occurrences.update({element: 1})
            else:
                occurrences[element] += 1
        for number, occurrence in occurrences.items():
            if occurrence > maximumOccurrence:
                maximumOccurrence = occurrence
        for number, occurrence in occurrences.items():
            if occurrence == maximumOccurrence:
                modes.append(number)
        if len(modes) == 1:
            return modes[0]
        else:
            return modes
    def max(self):
        return self.sortedList[len(self.sortedList)-1]
        # or we can just do self.sortedList[-1]
    def min(self):
        return self.sortedList[0]
