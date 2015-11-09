import fourtillsix as f, onetillthree as o, seventillnine as s

def check_input(x):

    if 1<=x<4:
        o.onetofour.btw_one_and_four(x)

    elif 4<=x<7:
        f.fourtoseven.btw_four_and_seven(x)

    elif 7<=x<10:
        s.sevenandten.btw_seven_and_ten(x)
    else:
        print "Number is out of specified range... Quiting the programm..."


