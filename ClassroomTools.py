import random


class SeatingChartMaker:
    def __init__(self, file=None):
        self.original_list = []
        self.randomized_list = []
        self.names_list = None
        self.chart = {}
        self.class_size = 21
        self.max_group = 4
        self.gui_output = ""
        self.group_fill_order = [1, 3, 4, 6, 7, 8, 2, 5, 9]
        self.col_width = 0
        # self.min_group = 3
        # self.exceptions = {}

        if file:
            self.import_names(file)

    def get_groups(self):
        return self.chart

    def get_gui_output(self):
        return self.gui_output

    def set_class_size(self, num):
        self.class_size = num

    def set_max_group(self, num):
        self.max_group = num

    def set_group_order(self, order):
        self.group_fill_order = order

    def import_names(self, file=None):
        self.names_list = None
        self.col_width = 0
        f = open(file, "r")
        self.names_list = f.readlines()
        f.close()
        for i in range(len(self.names_list)):
            self.names_list[i] = self.names_list[i].rstrip('\n')
        self.col_width = max(len(word) for row in self.names_list for word in row) + 2

    # def set_min_group(self, num):
    #     self.min_group = num

    def set_original_list(self, names=False):
        self.original_list.clear()
        if names:
            self.original_list = self.names_list.copy()
            self.class_size = len(self.original_list)
        else:
            for i in range(1, self.class_size + 1):
                self.original_list.append(i)

    def set_randomized_list(self, names=False):
        self.randomized_list.clear()
        self.set_original_list(names)
        # group = self.original_list.copy()
        for i in range(self.class_size):
            a = self.original_list.pop(random.randint(0, len(self.original_list) - 1))
            self.randomized_list.append(a)

    def create_groups(self, names=False):
        self.set_randomized_list(names)
        self.chart.clear()
        whole_group = self.randomized_list.copy()
        groups = []
        a = self.class_size // self.max_group
        b = self.class_size % self.max_group
        if b != 0:
            a += 1
        for i in range(a):
            groups.append([])
        i = len(self.randomized_list)
        j = 0
        while i > 0:
            groups[j].append(whole_group.pop(0))
            i -= 1
            j += 1
            if j == a:
                j = 0
        # for i in range(1, len(self.chart)+1):
        #     self.classroom[str(i)] = None
        for index in self.group_fill_order:
            if len(groups) > 0:
                self.chart[str(index)] = groups.pop(0)
            # else:
            #     self.chart[str(index)] = None
        return self.chart

    def create_display(self):
        self.gui_output = ""
        chart = sorted(self.chart.keys())
        while chart:
            i = chart.pop(0)
            self.gui_output += "Table" + i + ":"
            first = self.chart[i].copy()
            if chart:
                j = chart.pop(0)
                self.gui_output += "\t\t\tTable" + j + ":\n"
                second = self.chart[j].copy()
            for k in range(self.max_group):
                try:
                    self.gui_output += first.pop(0)
                except IndexError:
                    self.gui_output += "\t\t"
                try:
                    self.gui_output += "\t\t\t" + second.pop(0) + "\n"
                except IndexError:
                    self.gui_output += "\n"
            self.gui_output += "\n"
        print(self.gui_output)


class Grader:
    def __init__(self, file=None):
        self.rubric = {1: 20, 2: 40, 3: 60, 4: 75, 5: 85, 6: 100}
        self.translated_scores = {}
        if file:
            self.translate_scores(file)
            self.print(True)

    def translate_to_percent(self, score):
        a = score % 1
        b = int(score // 1)
        c = 100
        if b is not len(self.rubric):
            c = self.rubric[b] + a*(self.rubric[b+1]-self.rubric[b])
        return c

    def translate_scores(self, file):
        self.translated_scores.clear()
        f = open(file)
        scores = f.readlines()
        f.close()
        for score in scores:
            score = score.rstrip('\n')
            self.translated_scores[score] = self.translate_to_percent(float(score))

    def print(self, out=False):
        output = ""
        for score in sorted(self.translated_scores):
            output += "{0}: {1}\n".format(score, self.translated_scores[score])
        if out:
            f = open('TranslatedScores.txt', 'w')
            f.write(output)
            f.close()
        print(output)

    def set_rubric(self):
        None
