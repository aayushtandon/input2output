with open('C:\New folder\input.txt','r') as f:
    whole_text = f.read()
    main_list = whole_text.split('\n* ')

def list_formatter(list1):
    dot_count = list1[-1].count('.')
    list1_str_rep = ' ' + ' ' * dot_count + '- ' + list1[-1][(dot_count + 1):] + '\n'
    chunk_str = ''
    star_flag = 1
    double_star_flag = 1
    triple_star_flag = 1
    star_count = list1[0].count('*')
    if star_count == 0:
        chunk_str = chunk_str + str(chunk_line_num) + ' ' + list1[0][(star_count):] + '\n'
    elif star_count == 1:
        chunk_str = chunk_str + str(chunk_line_num) + '.' + str(star_flag) + ' ' + list1[0][(star_count):] + '\n'
        star_flag = star_flag + 1
    elif star_count == 2:
        chunk_str = chunk_str + str(chunk_line_num) + '.' + str(star_flag) + '.' + str(double_star_flag) + ' ' + list1[
                                                                                                                     0][
                                                                                                                 (
                                                                                                                     star_count):] + '\n'

        double_star_flag = double_star_flag + 1
    elif star_count == 3:
        chunk_str = chunk_str + str(chunk_line_num) + '.' + str(star_flag) + '.' + str(double_star_flag) + '.' + str(
            triple_star_flag) + ' ' + list1[0][(star_count):] + '\n'
        triple_star_flag = triple_star_flag + 1

    for element in range(len(list1) - 2, 0, -1):
        ele_dot_count = list1[element].count('.')
        if ele_dot_count == 0:
            list1_str_rep = list1_str_rep + '    ' + list1[element] + '\n'
        elif ele_dot_count < dot_count:
            list1_str_rep = list1_str_rep + ' ' + ' ' * ele_dot_count + '+ ' + list1[element][ele_dot_count + 1:] + '\n'
            dot_count = dot_count - 1
        elif ele_dot_count == dot_count:
            list1_str_rep = list1_str_rep + ' ' + ' ' * ele_dot_count + '- ' + list1[element][ele_dot_count + 1:] + '\n'
    the_main_list = list1_str_rep.split('\n')
    if '' in the_main_list:
        the_main_list.remove('')
    for i in the_main_list[::-1]:
        chunk_str = chunk_str + i + '\n'
    print chunk_str

for chunk_line_num in range(1,len(main_list)):
    if chunk_line_num!=3:
        list1 = [s for s in main_list[chunk_line_num].splitlines() if s != ' ' and s != '']
        list_formatter(list1)
    else:
        list0 = (' '+main_list[chunk_line_num]).split('\n*')
        for chunk2 in list0:
            lvl3_chunk_list = [s for s in chunk2.splitlines() if s != ' ' and s != '']
            list_formatter(lvl3_chunk_list)


