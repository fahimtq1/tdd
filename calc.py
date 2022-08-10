class SimpleCalc:

    def add(self, val1, val2):
        return val1 + val2


    def subtract(self, val1, val2):
        return val1 - val2


    def multiply(self, val1, val2):
        return val1 * val2


    def divide(self, val1, val2):
        return val1 / val2


    def percentage(self, val1, val2):
        return (val1/val2) * 100


    def cm_m(self, cm_value):
        return cm_value * 0.01


    def year_of_birth(self, age):
        year = 2022
        return year - age