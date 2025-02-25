# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    for i in range(start, stop-1, -1):
        print(message,str(i))
    print(completion_message)

    return None


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    return (base ** 2 + height ** 2) ** (1 / 2)


def calculate_area(base, height):
    return (base * height) / 2


def calculate_perimeter(base, height):
    return calculate_hypotenuse(base, height) + base + height


def calculate_aspect(base, height):
    aspect = ""
    if height > base:
        aspect = "tall"
    elif height < base:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "aspect": calculate_aspect(base, height),
        "base": base,
        "height": height,
        "hypotenuse": calculate_hypotenuse(base, height),
        "perimeter": calculate_perimeter(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    else:
        diagram = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return diagram + "\n" + facts


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    facts = get_triangle_facts(base,height,units ="mm")
    diagram = tell_me_about_this_right_triangle(facts)
    if return_diagram and return_dictionary:
        return {
            "diagram": diagram,
            "facts": facts
        }
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    lengthList = []
    for i in range(3,21,2):
        lengthList.append(i)
    for j in range(20,3,-2):
        lengthList.append(j)
    wordList = list_of_words_with_lengths(lengthList)
    for i in range(len(wordList)):
        print(wordList[i])
    return wordList

    # baseURL = (
    #     "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
    #     "wordlength={length}"
    # )

    # for i in range(3, 21, 2):
    #     url = baseURL.format(length=i)
    #     r = requests.get(url)
    #     if r.status_code is 200:
    #         message = r.text
    #         pyramid_list.append(message)
    #     else:
    #         print("failed a request", r.status_code, i)
    # for i in range(20, 3, -2):
    #     url = baseURL.format(length=i)
    #     r = requests.get(url)
    #     if r.status_code is 200:
    #         message = r.text
    #         pyramid_list.append(message)
    #     else:
    #         print("failed a request", r.status_code, i)


def get_a_word_of_length_n(length):
    import requests
    if type(length) is int:
        if length >= 3:
            baseURL = (
                "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
                "wordlength={length}"
            )
            url = baseURL.format(length=length)
            r = requests.get(url)
            if r.status_code is 200:
                message = r.text
            else:
                message = "failed a request " + str(r.status_code) + " " + str(length)
            return message
        else:
            message = "Length must be above 3 characters"
            return None
    else:
        message = "Length must be an integer and above 3"
        return None


def list_of_words_with_lengths(list_of_lengths):
    list_of_words = []
    for length in list_of_lengths:
        word = get_a_word_of_length_n(length)
        while word is None:
            word = get_a_word_of_length_n(length)
        list_of_words.append(word)
    return list_of_words

if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid()
