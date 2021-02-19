import texttable
import numpy as np


class YaakobiAndZaydel:
    mat_flag = False
    index = 0
    flag = False
    equations = []
    temp = []
    answer = []
    rows = 0
    cols = 0
    col_swaper_index = 0
    max_iter = 114
    counter = 0
    index = 0

    def insertFunc(self, lnl):
        self.equations = lnl.copy()
        print(f'inserted list is: {self.equations}')

    def MatrixPrint(self):
        string_eq = ''

        if self.flag == False:

            if self.mat_flag == False:
                print('\n\n** Matrix Representation: **\n')

                eq = self.equations.copy()
                eq.insert(0, [f'x{i + 1}' for i in range(len(eq[0]) - 1)])
                eq[0].append('B')
                table_mat = texttable.Texttable()
                table_mat.set_precision(3)
                table_mat.add_rows(eq)

                print(table_mat.draw())
                # self.mat_flag = True
                print()
            print('\nyour equations are:\n')

            for x in self.equations:
                for i in range(len(x)):
                    if x[i] >= 0:
                        if i == len(x) - 2:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('+ {:.4f} = '.format(x[i]), end='')
                        else:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('+ {:.4f} '.format(x[i]), end='')

                    else:
                        if i == len(x) - 2:
                            string_eq += '{:.4f} = '.format(x[i])
                            print('{:.4f} = '.format(x[i]), end='')
                        else:
                            string_eq += '{:.4f} = '.format(x[i])
                            print('{:.4f} '.format(x[i]), end='')
                string_eq += '\n'
                print()
        else:
            string_eq += '\nyour self.equations are:\n'
            print('\nyour self.equations are:\n')

            for x in self.equations:
                for i in range(len(x)):
                    if x[i] >= 0:
                        if i == 0:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('+ {:.4f} = '.format(x[i]), end='')
                        else:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('+ {:.4f} '.format(x[i]), end='')

                    else:
                        if i == 0:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('{:.4f} = '.format(x[i]), end='')
                        else:
                            string_eq += '+ {:.4f} = '.format(x[i])
                            print('{:.4f} '.format(x[i]), end='')
                string_eq += '\n'
                print()

    def findDominantRow(self, index):
        for i in range(index, len(self.equations)):
            if abs(self.equations[i][index - 1]) > sum(map(abs, self.equations[i][:index - 1])) + sum(map(abs, self.equations[i][index - 1 + 1:len(self.equations[i]) - 1])):
                return i

    def isValid(self):
        string_eq = ''
        self.MatrixPrint()

        for i in range(self.index, len(self.equations)):
            j = None

            if abs(self.equations[i][i]) < sum(map(abs, self.equations[i][:i])) + sum(map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])):
                self.col_swaper_index += 1

                sumA = sum(map(abs, self.equations[i][:i])) + sum(map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1]))
                temp = '\n(*) pivot: {0:}  (*) sum: {1:}  - need to be changed!\n'.format(str(self.equations[i][i]), str(sumA))
                string_eq += temp

                print('\npivot: ', self.equations[i][i], ' sum: ',
                      sum(map(abs, self.equations[i][:i])) + sum(map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])),
                      ' - need to be changed!\n')

                j = self.findDominantRow(i + 1)
                if j is None:
                    if self.col_swaper_index < len(self.equations[0]) - 1:

                        np_eq = np.array(self.equations)
                        np_eq[:, [i, self.col_swaper_index]] = np_eq[:, [self.col_swaper_index, i]]

                        self.equations = np_eq.copy()
                        for i in range(len(np_eq)):
                            self.equations[i] = np_eq[i].copy()

                        self.equations = self.equations.tolist()
                        self.MatrixPrint()
                        self.isValid()

                    elif self.col_swaper_index == len(self.equations[0]) - 1:
                        if self.max_iter > self.counter:
                            self.col_swaper_index = 0
                            self.counter += 1
                            self.isValid()
                        else:
                            string_eq += 'cannot find dominant diagonal for this matrix - thus, there is no answer.'

                            print('cannot find dominant diagonal for this matrix - thus, there is no answer.')
                            exit(1)


                else:
                    self.changeRow(i, j)
            else:
                self.index += 1

    def changeRow(self, row_index1, row_index2):
        self.equations[row_index1], self.equations[row_index2] = self.equations[row_index2], self.equations[row_index1]

    def Yaakobi(self):
        variables = []
        temp = [0 for i in range(len(self.equations))]
        changes = []
        variables.append(temp.copy())
        self.isValid()

        self.flag = True
        i = 0
        table_ans = texttable.Texttable()
        table_ans.set_precision(5)

        for x in self.equations:  ## x = 5 + y + z
            x[0], x[i] = x[i], x[0]
            changes.append(tuple([0, i]))
            i += 1
            print()

        for x in self.equations:  ## 2x = - 10y - 3z
            for i in range(1, len(x) - 1):
                x[i] *= -1

        j = 0
        for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
            c1, c2 = changes[j][0], changes[j][1]
            temp1 = variables[len(variables) - 1].copy()
            temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

            sum_temp = 0
            k = 1
            for i in range(1, len(x) - 1):
                sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                k += 1

            sum_temp = x[len(x) - 1] / x[0] + sum_temp

            temp[j] = sum_temp

            j += 1

        self.MatrixPrint()
        variables.append(temp.copy())

        while (abs(variables[len(variables) - 1][0] - variables[len(variables) - 2][0]) > 0.000001 and self.max_iter > self.counter):
            j = 0
            for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
                c1, c2 = changes[j][0], changes[j][1]
                temp1 = variables[len(variables) - 1].copy()
                temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

                sum_temp = 0
                k = 1
                for i in range(1, len(x) - 1):
                    sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                    k += 1
                sum_temp = x[len(x) - 1] / x[0] + sum_temp

                temp[j] = sum_temp

                j += 1
                self.counter += 1
            variables.append(temp.copy())
        print()
        j = 0
        for i in range(len(variables)):
            variables[i].insert(0, j)
            j += 1
        variables.insert(0, ['Index', 'Xr+1', 'Yr+1', 'Zr+1'])
        self.answer = variables[len(variables) - 1][1:].copy()
        table_ans.add_rows(variables)

        print(table_ans.draw())
        # for i in range(len(variables)):
        #     print(i, '  ', end=' ')
        #     for j in range(len(variables[i])):
        #         print(format(variables[i][j], ".4f"), '             ', end='')
        #     print()

    def Zaydel(self):
        variables = []
        temp = [0 for i in range(3)]
        changes = []
        variables.append(temp.copy())
        self.isValid()
        table_ans = texttable.Texttable()
        table_ans.set_precision(5)

        self.flag = True
        print('the fun part starts here:')
        i = 0
        for x in self.equations:  ## x = 5 + y + z
            x[0], x[i] = x[i], x[0]
            changes.append(tuple([0, i]))
            i += 1
            print()

        for x in self.equations:
            for i in range(1, len(x) - 1):
                x[i] *= -1

        j = 0
        for x in self.equations:
            c1, c2 = changes[j][0], changes[j][1]
            temp1 = temp.copy()
            temp[c1], temp[c2] = temp[c2], temp[c1]

            sum_temp = 0
            k = 1
            for i in range(1, len(x) - 1):
                sum_temp = sum_temp + (x[i] * temp[k]) / x[0]
                k += 1

            sum_temp = x[len(x) - 1] / x[0] + sum_temp

            temp[j] = sum_temp

            j += 1
        temp[0] = temp[1]
        self.MatrixPrint()
        variables.append(temp.copy())

        while (abs(variables[len(variables) - 1][0] - variables[len(variables) - 2][0]) > 0.000001 and self.max_iter > self.counter):
            j = 0
            self.counter += 1
            for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
                c1, c2 = changes[j][0], changes[j][1]
                temp1 = variables[len(variables) - 1].copy()
                temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

                sum_temp = 0
                k = 1
                for i in range(1, len(x) - 1):
                    sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                    k += 1
                sum_temp = x[len(x) - 1] / x[0] + sum_temp

                temp[j] = sum_temp

                j += 1
            variables.append(temp.copy())
        print()

        for i in range(len(variables)):
            variables[i].insert(0, j)
            j += 1
        variables.insert(0, ['Index', 'Xr+1', 'Yr+1', 'Zr+1'])
        table_ans.add_rows(variables)

        self.answer = variables[len(variables) - 1][1:].copy()

        print(table_ans.draw())

    def getAnswer(self):
        if self.answer != []:
            return self.answer


zaydel = YaakobiAndZaydel()
# # zaydel.insertFunc([[1, 2, 4, 8, 0], [1, 2.25, 5.0625, 11.390625, 0.112463], [1, 2.3, 5.289999999999999, 12.166999999999998, 0.167996], [1, 2.7, 7.290000000000001, 19.683000000000003, 0.222709]])
zaydel.insertFunc([[-1, -2, 5, 2], [4, -1, 1, 4], [1, 6, 2, 9]])
# zaydel.insertFunc([[10,8,1,-7],[4,10,-5,2],[5,1,10,1.5]])
# #
zaydel.Zaydel()
print("the answer is: ", zaydel.getAnswer())


def neville(list, x):
    dict={}
    tempdict ={}
    n = len(list)
    iters = 1
    while len(dict) != 1:
        for i in range(n - iters):
            temp = ((x - list[i][0]) * list[i + iters][1] - (x - list[i + iters][0]) * list[i][1]) / (list[i + iters][0] - list[i][0])
            tempdict['p' + str(i) + ',' + str(i + iters)] = temp
            #print('p' + str(i) + ',' + str(i + iters))
        dict = tempdict
        tempdict = {}
        print('Iteration Number: ',iters,dict)
        iters += 1


    return dict