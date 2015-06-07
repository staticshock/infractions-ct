#! /usr/bin/env python
import re
import sys
import csv
import json
import argparse


def main():
    args = parse_args()
    infractions = list(parse_infractions(args.input))
    if args.format == 'csv':
        to_csv(infractions)
    else:
        # json
        if args.costs:
            print(to_costs_json(infractions))
        elif args.descriptions:
            print(to_descriptions_json(infractions))
        else:
            print(to_json(infractions))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=('json', 'csv'), default='json')
    parser.add_argument("--costs", action='store_true')
    parser.add_argument("--descriptions", action='store_true')
    parser.add_argument('input', type=argparse.FileType('r'))
    return parser.parse_args()


# take infractions.txt as input
def parse_infractions(input_file):
    cur_category = None
    cur_infraction = None

    for line in input_file:

        # Blank lines == end of category
        if not line.strip():
            cur_category = None

        # First non-blank line == new category name
        elif line and not cur_category:
            cur_category = line.strip()

        # Otherwise it's a data line, which describes one of two possible
        # flavors of record:
        #   1. Single line: <infraction> <description>      <costs>
        #   2. Multi-line:  <infraction> <description>
        #                                <more description> <costs>
        else:
            name = line[:16].strip()
            description = line[16:132].strip()
            costs_string = line[132:]

            if cur_infraction:
                cur_infraction['description'] += ' ' + description
            else:
                if not name:
                    print(line)
                cur_infraction = {
                    'name': name,
                    'category': cur_category,
                    'description': description,
                }

            # Presence of costs signals the end of the entry
            if costs_string:
                costs = list(enumerate_costs(costs_string))
                # costs[0] may be a string, such as "See Note" or "See Appx A"
                cur_infraction['variable'] = not isinstance(costs[0], float)
                if cur_infraction['variable']:
                    cur_infraction['cost'] = ""
                    cur_infraction['breakdown'] = [""] * 9
                else:
                    cur_infraction['cost'] = costs[0]
                    cur_infraction['breakdown'] = costs[1:]

                yield cur_infraction
                cur_infraction = None


def enumerate_costs(costs_line):
    for i in range(0, 120, 12):
        cost = costs_line[i:i+12].strip()
        if not cost:
            yield 0.0
        elif re.match(r"[0-9.,]+$", cost):
            yield float(cost.replace(",", ""))
        else:
            yield cost


def to_json(infractions):
    return json.dumps(infractions, sort_keys=True)


def to_costs_json(infractions):
    costs = {}
    for infraction in infractions:
        if infraction.get('variable', False):
            costs[infraction['name']] = {'variable': True}
        else:
            costs[infraction['name']] = {
                'cost': infraction['cost'],
                'breakdown': infraction['breakdown'],
            }
    return json.dumps(costs, sort_keys=True)


def to_descriptions_json(infractions):
    descriptions = []
    for infraction in infractions:
        descriptions.append({
            'name': infraction['name'],
            'category': infraction['category'],
            'description': infraction['description'],
        })
    return json.dumps(descriptions, sort_keys=True)


def to_csv(infractions):
    writer = csv.writer(sys.stdout)
    for infraction in infractions:
        writer.writerow([
            infraction['name'],
            'variable' if infraction['variable'] else infraction['cost'],
        ]+ infraction['breakdown'] + [
            infraction['description'],
        ])

main()
