from typing import List
import re
import numpy as np

def input(path: str)->List[str]:
    passportinfo = []
    curr = []
    with open(path) as f:
        for line in f.readlines():
            if line == "\n":
                passportinfo.append(curr)
                curr = []
            else:
                line = line.replace("\n", "")
                curr.append(line)
    finalinfo = []
    for _list in passportinfo:
        templist = [string.split(" ") for string in _list]
        finalinfo.append([x for y in templist for x in y])
    return finalinfo

def check_byr(val:str)->bool:
    # four digits; at least 1920 and at most 2002.
    if re.match('[0-9]{4}', val) and (1920 <= int(val)<=2002):
        return True
    else:
        return False

def check_iyr(val:str)->bool:
    # four digits; at least 2010 and at most 2020.
    if re.match('[0-9]{4}', val) and (2010 <= int(val)<=2020):
        return True
    else:
        return False

def check_eyr(val:str)->bool:
    # four digits; at least 2020 and at most 2030.
    if re.match('[0-9]{4}', val) and (2020 <= int(val)<=2030):
        return True
    else:
        return False

def check_hgt(val:str)->bool:
    # a number followed by either cm or in
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if np.isfinite(int(val[:-2])) and re.match('cm', val[-2:], flags=re.I) and (150 <= int(val[:-2])<=193):
        return True
    elif np.isfinite(int(val[:-2])) and re.match('in', val[-2:], flags=re.I) and (59 <= int(val[:-2])<=76):
        return True
    else:
        return False

def check_hcl(val:str)->bool:
    # a # followed by exactly six characters 0-9 or a-f.
    if val[0:1] == '#' and re.match('[A-Za-z0-9]{6}', val[1:], flags=re.I):
        return True
    else:
        return False

def check_ecl(val:str)->bool:
    # exactly one of: amb blu brn gry grn hzl oth.
    if len(val) == 3 and val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True
    else:
        return False

def check_pid(val:str)->bool:
    # a nine-digit number, including leading zeroes.
    if len(val) == 9 and re.match('(?:0*([1-9]\d{1,9}|\w{9}))$', val):
        return True
    else:
        return False

def part_two(passportinfo:List[str], counter:int, valid_count:int)->int:

    passport_dict = dict()
    for id in passportinfo:
        key, val = id.split(':')[0], id.split(':')[1]
        
        assert key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

        assert val and len(val) > 0 

        if key == 'cid':
            continue
    
        if not passport_dict.get(counter):
            passport_dict[counter] = {'byr':None,
                                      'iyr':None,
                                      'eyr':None,
                                      'hgt':None,
                                      'hcl':None,
                                      'ecl':None,
                                      'pid':None}
           
        if not passport_dict[counter].get(key):
            passport_dict[counter][key] = val

    if (passport_dict[counter].get('byr') and check_byr(passport_dict[counter].get('byr')) and
        passport_dict[counter].get('iyr') and check_iyr(passport_dict[counter].get('iyr')) and 
        passport_dict[counter].get('eyr') and check_eyr(passport_dict[counter].get('eyr')) and 
        passport_dict[counter].get('hgt') and check_hgt(passport_dict[counter].get('hgt')) and
        passport_dict[counter].get('hcl') and check_hcl(passport_dict[counter].get('hcl')) and
        passport_dict[counter].get('ecl') and check_ecl(passport_dict[counter].get('ecl')) and 
        passport_dict[counter].get('pid') and check_pid(passport_dict[counter].get('pid'))):
        valid_count +=1

    return valid_count

def part_one(passportinfo:List[str], counter:int, valid_count:int)->int:

    passport_dict = dict()
    for id in passportinfo:
        key, val = id.split(':')[0], id.split(':')[1]
        
        assert key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

        assert val and len(val) > 0 

        if key == 'cid':
            continue
    
        if not passport_dict.get(counter):
            passport_dict[counter] = {'byr':None,
                                      'iyr':None,
                                      'eyr':None,
                                      'hgt':None,
                                      'hcl':None,
                                      'ecl':None,
                                      'pid':None}
           
        if not passport_dict[counter].get(key):
            passport_dict[counter][key] = val

    if (passport_dict[counter].get('byr') and
        passport_dict[counter].get('iyr') and 
        passport_dict[counter].get('eyr') and 
        passport_dict[counter].get('hgt') and
        passport_dict[counter].get('hcl') and
        passport_dict[counter].get('ecl') and 
        passport_dict[counter].get('pid')):
        valid_count +=1

    return valid_count


if __name__ == "__main__":
    passportinfo = input("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayfour.txt")

    
    # test dict
    testinfo = [["ecl:gry", "pid:860033327", "eyr:2020", "hcl:#fffffd",
                'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm'],['iyr:2013',
                'ecl:amb', 'cid:350', 'eyr:2023', 'pid:028048884','hcl:#cfa07d',
                'byr:1929'],['hcl:#ae17e1','iyr:2013','eyr:2024','ecl:brn','pid:760753108',
                'byr:1931','hgt:179cm'],['hcl:#cfa07d','eyr:2025','pid:166559648','iyr:2011',
                'ecl:brn', 'hgt:59in']]
    valid_count = 0
    for i, info in enumerate(testinfo):
        valid_count = part_one(info, i, valid_count)

    # part one
    valid_count = 0
    for i, info in enumerate(passportinfo):
        valid_count = part_one(info, i, valid_count)
    print("part one results:", valid_count)

    # test two
    assert True == check_byr("2000")
    assert False == check_byr("2400")

    assert True == check_pid("000000001")
    assert False == check_pid("0000000001")

    assert False == check_hgt("200cm")
    assert True == check_hgt("150cm")

    # invalid
    invalid_test = [['eyr:1972', 'cid:100', 'hcl:#18171d' 'ecl:amb', 'hgt:170', 'pid:186cm', 'iyr:2018', 'byr:1926'],
                    ['iyr:2019','hcl:#602927', 'eyr:1967', 'hgt:170cm', 'ecl:grn', 'pid:012533040', 'byr:1946'],
                    ['hcl:dab227', 'iyr:2012', 'ecl:brn', 'hgt:182cm', 'pid:021572410', 'eyr:2020' 'byr:1992', 'cid:277'],
                    ['hgt:59cm', 'ecl:zzz', 'eyr:2038', 'hcl:74454a', 'iyr:2023', 'pid:3556412378', 'byr:2007']]

    # valid
    valid_test = [['pid:087499704', 'hgt:74in', 'ecl:grn', 'iyr:2012', 'eyr:2030', 'byr:1980','hcl:#623a2f'],
                  ['eyr:2029', 'ecl:blu', 'cid:129', 'byr:1989', 'iyr:2014', 'pid:896056539', 'hcl:#a97842', 'hgt:165cm'],
                  ['hcl:#888785', 'hgt:164cm', 'byr:2001', 'iyr:2015', 'cid:88', 'pid:545766238', 'ecl:hzl'],
                  ['eyr:2022', 'iyr:2010', 'hgt:158cm', 'hcl:#b6652a', 'ecl:blu', 'byr:1944', 'eyr:2021', 'pid:093154719']
                ]

    # invalid test
    invalid_count = 0
    for i, info in enumerate(invalid_test):
        invalid_count = part_two(info, i, invalid_count)

    assert invalid_count == 0

     # valid test
    validtest_count = 0
    for i, info in enumerate(valid_test):
        validtest_count = part_two(info, i, validtest_count)

    assert validtest_count+1 == 4

    # part two
    valid_count = 0
    for i, info in enumerate(passportinfo):
        valid_count = part_two(info, i, valid_count)
    print("part two results:", valid_count+1)

