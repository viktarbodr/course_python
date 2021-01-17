from os import system
import datetime, time

# black
b = '\u25FB\u25FB'
# white
w = '\u00A0''\u00A0'


t_01 = b + b + b
t_02 = b + w + b
t_03 = b + w + b
t_04 = b + w + b
t_05 = b + b + b
    
t_11 = w + b + w
t_12 = b + b + w
t_13 = w + b + w
t_14 = w + b + w
t_15 = w + b + w

t_21 =  b + b + b
t_22 =  w + w + b
t_23 =  w + b + w
t_24 =  b + w + w
t_25 =  b + b + b

t_31 = b + b + b
t_32 = w + w + b
t_33 = b + b + b
t_34 = w + w + b
t_35 = b + b + b

t_41 = b + w + b
t_42 = b + w + b
t_43 = b + b + b
t_44 = w + w + b
t_45 = w + w + b

t_51 = b + b + b
t_52 = b + w + w
t_53 = b + b + b
t_54 = w + w + b
t_55 = b + b + b

t_61 = b + b + b
t_62 = b + w + w
t_63 = b + b + b
t_64 = b + w + b
t_65 = b + b + b

t_71 = b + b + b
t_72 = w + w + b
t_73 = w + b + w
t_74 = b + w + w
t_75 = b + w + w

t_81 =  b + b + b
t_82 =  b + w + b
t_83 =  b + b + b
t_84 =  b + w + b
t_85 =  b + b + b

t_91 = b + b + b
t_92 = b + w + b
t_93 = b + b + b
t_94 = w + w + b
t_95 = w + b + b
# :
zz_1 = w + w + w
zz_2 = w + b + w
zz_3 = w + w + w
zz_4 = w + b + w
zz_5 = w + w + w
#   
z_1 = w + w + w
z_2 = w + w + w
z_3 = w + w + w
z_4 = w + w + w
z_5 = w + w + w


def time_n():
    
    while True:
        t = datetime.datetime.now()
        item = t.strftime('%H%M%S')
        if item[0] == '0':
            hour_01 = t_01
            hour_02 = t_02
            hour_03 = t_03
            hour_04 = t_04
            hour_05 = t_05
        if item[0]== '1':
            hour_01 = t_11
            hour_02 = t_12
            hour_03 = t_13
            hour_04 = t_14
            hour_05 = t_15
        if item[0] == '2':
            hour_01 = t_21
            hour_02 = t_22
            hour_03 = t_23
            hour_04 = t_24
            hour_05 = t_25
        if item[1] == '0':
            hour_11 = t_01
            hour_12 = t_02
            hour_13 = t_03
            hour_14 = t_04
            hour_15 = t_05
        if item[1] == '1':
            hour_11 = t_11
            hour_12 = t_12
            hour_13 = t_13
            hour_14 = t_14
            hour_15 = t_15
        if item[1] == '2':
            hour_11 = t_21
            hour_12 = t_22
            hour_13 = t_23
            hour_14 = t_24
            hour_15 = t_25
        if item[1] == '3':
            hour_11 = t_31
            hour_12 = t_32
            hour_13 = t_33
            hour_14 = t_34
            hour_15 = t_35
        if item[1] == '4':
            hour_11 = t_41
            hour_12 = t_42
            hour_13 = t_43
            hour_14 = t_44
            hour_15 = t_45
        if item[1] == '5':
            hour_11 = t_51
            hour_12 = t_52
            hour_13 = t_53
            hour_14 = t_54
            hour_15 = t_55
        if item[1] == '6':
            hour_11 = t_61
            hour_12 = t_62
            hour_13 = t_63
            hour_14 = t_64
            hour_15 = t_65
        if item[1] == '7':
            hour_11 = t_71
            hour_12 = t_72
            hour_13 = t_73
            hour_14 = t_74
            hour_15 = t_75
        if item[1] == '8':
            hour_11 = t_81
            hour_12 = t_82
            hour_13 = t_83
            hour_14 = t_84
            hour_15 = t_85
        if item[1] == '9':
            hour_11 = t_91
            hour_12 = t_92
            hour_13 = t_93
            hour_14 = t_94
            hour_15 = t_95
        if item[2] == '0':
            min_01 = t_01
            min_02 = t_02
            min_03 = t_03
            min_04 = t_04
            min_05 = t_05
        if item[2] == '1':
            min_01 = t_11
            min_02 = t_12
            min_03 = t_13
            min_04 = t_14
            min_05 = t_15
        if item[2] == '2':
            min_01 = t_21
            min_02 = t_22
            min_03 = t_23
            min_04 = t_24
            min_05 = t_25
        if item[2] == '3':
            min_01 = t_31
            min_02 = t_32
            min_03 = t_33
            min_04 = t_34
            min_05 = t_35
        if item[2] == '4':
            min_01 = t_41
            min_02 = t_42
            min_03 = t_43
            min_04 = t_44
            min_05 = t_45
        if item[2] == '5':
            min_01 = t_51
            min_02 = t_52
            min_03 = t_53
            min_04 = t_54
            min_05 = t_55
        if item[2] == '6':
            min_01 = t_61
            min_02 = t_62
            min_03 = t_63
            min_04 = t_64
            min_05 = t_65
        if item[3] == '0':
            min_11 = t_01
            min_12 = t_02
            min_13 = t_03
            min_14 = t_04
            min_15 = t_05
        if item[3] == '1':
            min_11 = t_11
            min_12 = t_12
            min_13 = t_13
            min_14 = t_14
            min_15 = t_15
        if item[3] == '2':
            min_11 = t_21
            min_12 = t_22
            min_13 = t_23
            min_14 = t_24
            min_15 = t_25
        if item[3] == '3':
            min_11 = t_31
            min_12 = t_32
            min_13 = t_33
            min_14 = t_34
            min_15 = t_35
        if item[3] == '4':
            min_11 = t_41
            min_12 = t_42
            min_13 = t_43
            min_14 = t_44
            min_15 = t_45
        if item[3] == '5':
            min_11 = t_51
            min_12 = t_52
            min_13 = t_53
            min_14 = t_54
            min_15 = t_55
        if item[3] == '6':
            min_11 = t_61
            min_12 = t_62
            min_13 = t_63
            min_14 = t_64
            min_15 = t_65
        if item[3] == '7':
            min_11 = t_71
            min_12 = t_72
            min_13 = t_73
            min_14 = t_74
            min_15 = t_75
        if item[3] == '7':
            min_11 = t_71
            min_12 = t_72
            min_13 = t_73
            min_14 = t_74
            min_15 = t_75
        if item[3] == '8':
            min_11 = t_81
            min_12 = t_82
            min_13 = t_83
            min_14 = t_84
            min_15 = t_85
        if item[3] == '9':
            min_11 = t_91
            min_12 = t_92
            min_13 = t_93
            min_14 = t_94
            min_15 = t_95
        if item[4] == '0':
            sec_01 = t_01
            sec_02 = t_02
            sec_03 = t_03
            sec_04 = t_04
            sec_05 = t_05
        if item[4] == '1':
            sec_01 = t_11
            sec_02 = t_12
            sec_03 = t_13
            sec_04 = t_14
            sec_05 = t_15
        if item[4] == '2':
            sec_01 = t_21
            sec_02 = t_22
            sec_03 = t_23
            sec_04 = t_24
            sec_05 = t_25
        if item[4] == '3':
            sec_01 = t_31
            sec_02 = t_32
            sec_03 = t_33
            sec_04 = t_34
            sec_05 = t_35
        if item[4] == '4':
            sec_01 = t_41
            sec_02 = t_42
            sec_03 = t_43
            sec_04 = t_44
            sec_05 = t_45
        if item[4] == '5':
            sec_01 = t_51
            sec_02 = t_52
            sec_03 = t_53
            sec_04 = t_54
            sec_05 = t_55
        if item[4] == '6':
            sec_01 = t_61
            sec_02 = t_62
            sec_03 = t_63
            sec_04 = t_64
            sec_05 = t_65
        if item[5] == '0':
            sec_11 = t_01
            sec_12 = t_02
            sec_13 = t_03
            sec_14 = t_04
            sec_15 = t_05
        if item[5] == '1':
            sec_11 = t_11
            sec_12 = t_12
            sec_13 = t_13
            sec_14 = t_14
            sec_15 = t_15
        if item[5] == '2':
            sec_11 = t_21
            sec_12 = t_22
            sec_13 = t_23
            sec_14 = t_24
            sec_15 = t_25
        if item[5] == '3':
            sec_11 = t_31
            sec_12 = t_32
            sec_13 = t_33
            sec_14 = t_34
            sec_15 = t_35
        if item[5] == '4':
            sec_11 = t_41
            sec_12 = t_42
            sec_13 = t_43
            sec_14 = t_44
            sec_15 = t_45
        if item[5] == '5':
            sec_11 = t_51
            sec_12 = t_52
            sec_13 = t_53
            sec_14 = t_54
            sec_15 = t_55
        if item[5] == '6':
            sec_11 = t_61
            sec_12 = t_62
            sec_13 = t_63
            sec_14 = t_64
            sec_15 = t_65
        if item[5] == '7':
            sec_11 = t_71
            sec_12 = t_72
            sec_13 = t_73
            sec_14 = t_74
            sec_15 = t_75
        if item[5] == '8':
            sec_11 = t_81
            sec_12 = t_82
            sec_13 = t_83
            sec_14 = t_84
            sec_15 = t_85
        if item[5] == '9':
            sec_11 = t_91
            sec_12 = t_92
            sec_13 = t_93
            sec_14 = t_94
            sec_15 = t_95
        if item[5] == '1' or item[5] == '3' or item[5] == '5' or item[5] == '7' or item[5] == '9':
            sep_1 = zz_1
            sep_2 = zz_2 
            sep_3 = zz_3 
            sep_4 = zz_4
            sep_5 = zz_5
        else:
            sep_1 = z_1
            sep_2 = z_2 
            sep_3 = z_3 
            sep_4 = z_4
            sep_5 = z_5

        time.sleep(1)
        system('clear')
        print(hour_01 + w + hour_11 + sep_1 + min_01 + w + min_11 + sep_1 + sec_01 + w + sec_11)
        print(hour_02 + w + hour_12 + sep_2 + min_02 + w + min_12 + sep_2 + sec_02 + w + sec_12)
        print(hour_03 + w + hour_13 + sep_3 + min_03 + w + min_13 + sep_3 + sec_03 + w + sec_13)
        print(hour_04 + w + hour_14 + sep_4 + min_04 + w + min_14 + sep_4 + sec_04 + w + sec_14)
        print(hour_05 + w + hour_15 + sep_5 + min_05 + w + min_15 + sep_5 + sec_05 + w + sec_15)
     
time_n()
