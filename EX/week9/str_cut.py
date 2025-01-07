def cut_str(word):
    back=[]
    no_point=word.replace(".","!")

    data_list=no_point.split("!")

    for x in data_list:
        no_space=x.lstrip()
        back.append(len(no_space))
    return back

print(cut_str("   12 .23 ! 455 5.3453."))