# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))


def human_years_cat_years_dog_years(h):
    cat = [15, 9, 4]
    dog = [15, 9, 5]
    return [h,
            min(1, h)*cat[0] + clamp(0, h-1, 1)*cat[1] + max(0, h-2)*cat[2],
            min(1, h)*dog[0] + clamp(0, h-1, 1)*dog[1] + max(0, h-2)*dog[2]
            ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(human_years_cat_years_dog_years(1))
    print(human_years_cat_years_dog_years(2))
    print(human_years_cat_years_dog_years(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
