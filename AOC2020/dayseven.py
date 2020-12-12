from typing import List, NamedTuple, Dict, Tuple
import re
from collections import defaultdict

def input(path:str)-> List[str]:
    with open(path) as f:
        raw = f.read()
        bags = make_bags(raw)
        print(len(can_eventually_contain(bags, "shiny gold")))
        print(num_bags_inside(bags, "shiny gold"))

class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]

def parse_line(line: str) -> Bag:
    part1, part2 = line.split(" contain ")
    color = part1[:-5]

    part2 = part2.rstrip(".")
    if part2 == "no other bags":
        return Bag(color, {})

    contains = {}

    contained = part2.split(", ")
    for subbag in contained:
        subbag = re.sub(r"bags?$", "", subbag)
        first_space = subbag.find(" ")
        count = int(subbag[:first_space].strip())
        color2 = subbag[first_space:].strip()
        contains[color2] = count
    return Bag(color, contains)

def make_bags(raw: str) -> List[Bag]:
    return [parse_line(line) for line in raw.split("\n")]

def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    ic = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.color)
    return ic

def can_eventually_contain(bags: List[Bag], color: str) -> List[str]:
    parent_map = parents(bags)

    check_me = [color]
    can_contain = set()

    while check_me:
        child = check_me.pop()
        for parent in parent_map.get(child, []):
            if parent not in can_contain:
                can_contain.add(parent)
                check_me.append(parent)
    return list(can_contain)
    
def num_bags_inside(bags: List[Bag], color: str) -> int:
    by_color = {bag.color: bag for bag in bags}

    num_bags = 0
    stack: List[Tuple[str,int]] = [(color, 1)]
    while stack:
        next_color, multiplier = stack.pop()
        bag = by_color[next_color]
        for child, count in bag.contains.items():
            num_bags += multiplier * count
            stack.append((child, count * multiplier))
    return num_bags

if __name__ == "__main__":

    # Test
    print("test:")
    test_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayseventest.txt')

    print("\n")
    # real
    print("real:")
    real_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayseven.txt')

    
