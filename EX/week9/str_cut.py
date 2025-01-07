def cut_str(word):
    back=[]
    no_point=word.replace(".","!")

    data_list=no_point.split("!")

    for i in range(len(data_list)-1):
        no_space=data_list[i].lstrip()
        back.append(len(no_space))
    return back

print(cut_str("   12 .23 !!! 455 5.3453"))