month, days = map(int, input().split())
month_to_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

prv, nxt = 'mm.dd', 'mm.dd'

if days + 1 > month_to_days[month]:
    nxt = f"{str(month+1).rjust(2, '0')}.01"
else:
    nxt = f"{str(month).rjust(2, '0')}.{str(days+1).rjust(2, '0')}"

if days - 1 <= 0:
    prv = f"{str(month-1).rjust(2, '0')}.{month_to_days[month-1]}"
else:
    prv = f"{str(month).rjust(2, '0')}.{str(days-1).rjust(2, '0')}"

print(prv, nxt)