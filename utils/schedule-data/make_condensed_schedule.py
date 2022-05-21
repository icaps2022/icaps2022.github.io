
with open('icaps_schedule_details.csv', 'r') as f:
    lines = f.readlines()

data = {i: {} for i in range(19)}

for line in lines[1:]:
    line = line.split(',')
    data[int(line[0])][line[2]] = line

print('<table class="schedule-overview">')
for slot in range(19):
    print('<tr>', end='')
    print(f'<td>{slot+6}</td>', end='')
    for day in range(1,5):
        if f'{day}' not in data[slot]:
            print(f'<td></td>', end='')
        else:
            line = data[slot][f'{day}']
            if line[4] == 'Joint':
                print(f'<td colspan="2">{line[5]}</td>', end='')
            elif line[4] == 'Single':
                print(f'<td><a href="#{line[5]}">{line[7]}</a></td><td><a href="#{line[6]}">{line[8]}</a></td>', end='')
            else:
                print('<td></td><td></td>', end='')
    print('</tr>')
print('</table>')
