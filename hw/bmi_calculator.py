from enum import IntEnum, unique

@unique
class BMI_CATEGORY(IntEnum): 
    VERY_SEVERELY_UNDERWEIGHT = 0
    SEVERELY_UNDERWEIGHT = 1
    UNDERWEIGHT = 2
    NORMAL = 3
    OVERWEIGHT_SLIGHTLY = 4
    MODERATELY_OBESE = 5
    SEVERELY_OBESE = 6
    VERY_SEVERELY_OBESE = 7
    MORBIDLY_OBESE = 8
    SUPER_OBESE = 9
    HYPER_OBESE = 10


def process_user_input(weight, height):
    w = float(weight)
    h = float(height)
    return w, h


def input_from_user():
    weight = None
    height = None
    ##################################################
    #TODO: input from user
    assert False, "Unimplemented!"
    ##################################################
    return  weight, height


def transform_calc_bmi(weight, height):
    bmi = None
    ##################################################
    #TODO: implement BMI function
    assert False, "Unimplemented!"
    ##################################################
    return bmi


def output_to_user(w, h, bmi, cat):
    ##################################################
    #TODO: output to user
    assert False, "Unimplemented!"
    ##################################################


def classify(bmi):
    category = None
    ##################################################
    #TODO: output to user
    assert False, "Unimplemented!"
    ##################################################
    return category


if __name__ == "__main__":
    w, h = input_from_user()
    bmi = transform_calc_bmi(w, h)
    cat = classify(bmi)
    output_to_user(w, h, bmi, cat)