""" Assignment 2: fuzzy sets bla bla bla """


class Bcolors:
    """ Fancy colors y'all!"""
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'

    def disable(self):
        """ Turn that shit off! """
        self.header = ''
        self.okblue = ''
        self.okgreen = ''
        self.warning = ''
        self.fail = ''
        self.endc = ''

    @staticmethod
    def color(coloree, color):
        """ Color a given string using built-in predefined colors"""
        return color + coloree + Bcolors.endc

def get_list_from_input(defining_string=None):
    """ Function to convert input to a string. Empty list on failure """

    if defining_string:
        print(defining_string)
    _input = input("Enter a list as numbers seperated by a space('q' to quit): ")
    while not _input == "q":
        try:
            raw = [float(x) for x in _input.split()]
            print(Bcolors.color("{0}".format(raw), Bcolors.okgreen))
            return raw
        except TypeError as err:
            print(Bcolors.color("Error: ", Bcolors.fail) + "{0}, enter 'q' to exit".format(err))
            _input = input("Enter next list as numbers seperated by a space('q' to quit): ")
        except ValueError as err:
            print(Bcolors.color("Error: ", Bcolors.fail) + "{0}, enter 'q' to exit".format(err))
            _input = input("Enter next list as numbers seperated by a space('q' to quit): ")

    return []

def capture_fazzy_sets(defining_set):
    """Loop to capture fuzzy sets from a given input and stop if there's one that isn't a list."""
    sets = []
    print(Bcolors.color(defining_set, Bcolors.header))
    input_set = get_list_from_input()

    while input_set:
        sets.append(input_set)
        input_set = get_list_from_input()

    print("Input sets:")
    for each_set in sets:
        print(each_set)
    return sets

def calc_solution(y_set, v_set):
    """ Calculates biggest solution for a given fuzzy set Yi and Vi """
    greatest_solution = []


    for y_i in y_set:
        current_row = []
        for v_i in v_set:
            current_row.append(1 if y_i <= v_i else v_i)
        greatest_solution.append(current_row)

    return greatest_solution

def calc_solution_for_all(y_sets, v_sets):
    """ Applies calc_solution to all input sets """

    all_the_solutions = []

    for y_set, v_set in zip(y_sets, v_sets):
        all_the_solutions.append(calc_solution(y_set, v_set))

    return all_the_solutions

def print_fuzzy_rhos(rho_set):
    """ Output of a set as matrix """
    print(Bcolors.color("Optimal solutions:", Bcolors.okblue))

    i = 0
    for each_set in rho_set:
        print("{0}-------------".format(i))
        for each_line in each_set:
            print(each_line)
        print("-------------{0}".format(i))
        i = i + 1

def get_combined_solution(all_solutions):
    """ Combines all solutions to one """
    w = len(all_solutions[1])
    h = len(all_solutions[1][1])
    solution = [[0 for x in range(w)] for y in range(h)]
    for each_matrix in all_solutions:
        for x, each_line in enumerate(each_matrix):
            for y, each_item in enumerate(each_line):
                if not solution[x][y] or each_item < solution[x][y]:
                    solution[x][y] = each_item

    return solution

def print_solution(solution):
    """ Prints one solution """
    print(Bcolors.color("Optimal solution:", Bcolors.okblue))
    for each_line in solution:
        print(each_line)

def main():
    """Fucking main function. God I hate pylint sometimes."""

    # crisp_x = input("Crisp Set X as Python list")
    # crisp_y = input("Crisp Y as Python List")

    fuzzy_x = capture_fazzy_sets("Fuzzy Set X")
    fuzzy_y = capture_fazzy_sets("Fuzzy Set Y")

    all_solutions = calc_solution_for_all(fuzzy_x, fuzzy_y)

    solution = get_combined_solution(all_solutions)

    print_solution(solution)

    #print_fuzzy_rhos(solution)

    #solutions = calc_solution_for_all(fuzzy_x, fuzzy_y)

if __name__ == "__main__":
    main()
