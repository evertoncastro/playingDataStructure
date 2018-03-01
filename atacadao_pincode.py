
def calculate_total(part, start):
    total = 0
    for p in part:
        if start > 9:
            start = 2
        total += int(p) * start
        start += 1
    return total 

def check_dv(total, dv):
    if (total % 11) != int(dv):
        raise Exception('InvalidPincode')

pincode = '048703000054323400345692113'

part = pincode[:15]
dv = pincode[15:16]
check_dv(calculate_total(part, 3), dv)

part = pincode[:25]
dv = pincode[25:26]
check_dv(calculate_total(part, 4), dv)

part = pincode[:26]
dv = pincode[26:27]
check_dv(calculate_total(part, 5), dv)


   