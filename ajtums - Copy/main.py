import urllib.request
import bs4 as bs
import ssl

url = 'https://akademik.ums.ac.id/kuliah.php?category=FProgdi&keyword=%25_&cetak=layar&submitted=yes&mod=Jadwal_Kuliah'

# url = 'https://www.google.com'

context = ssl._create_unverified_context()
source = bs.BeautifulSoup(urllib.request.urlopen(url, context=context).read(), 'lxml')

div = source.body.find_all(['span', 'tr'])[1:]

day = ['SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT', 'SABTU']

master = []

temp = []

for d in div:
    if d.text in day:
        if d.text == 'SENIN':
            pass
        else:
            master.append(temp)
            temp = []
    else:
        temp.append([td.text for td in d.find_all(['td','th'])])
master.append(temp)
print(master)
ruang = []
for day in master:
    for schedule in day[1:]:
        if schedule[0] not in ruang:
            (ruang.append(schedule[0]))

print(len(ruang))
print(ruang)
for r in ruang:
    print(r)