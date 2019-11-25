def convert(number):
    is_factor_dict = {"Pling": number % 3 == 0, "Plang": number % 5 == 0, "Plong": number % 7 == 0}
    raindrops = "".join([k for k, v in is_factor_dict.items() if v])
    if raindrops != "":
        return raindrops
    else:
        return str(number)
