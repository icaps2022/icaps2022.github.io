import csv, pprint

# load the data.csv with csv library
data = {}
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in list(reader)[3:]:
        data[row[0]] = {
            'authors': row[1],
            'title': row[2],
            'pid': row[0]
        }


TEMPLATE = """
      <section id="demo-{pid}" class="demo">
        <div class="row">
          <div class="12u 12u(mobile)">
            <h1>{title}</h1>
            <img src="{pid}.png" alt="{title}" />
            <h2>{authors}</h2>
            <a class="button float-right-button"
                href="ICAPS_2022_paper_{pid}.pdf">Paper</a>
          </div>
        </div>
      </section>
"""

print('<div class="row"><div id="demo-list-1" class="6u 12u(mobile)">')

ul = ""

count = 0
for pid in data:
    ul += f'<li><a href="#demo-{pid}">{data[pid]["title"]}</a></li>\n'
    print(TEMPLATE.format(**data[pid]))
    count += 1
    if count == 5:
        print('</div><div id="demo-list-2" class="6u 12u(mobile)">')
print('</div></div>')

# print(ul)
