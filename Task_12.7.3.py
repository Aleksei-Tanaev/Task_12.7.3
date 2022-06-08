per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:\n"))
depos = [per_cent['ТКБ']*money/100, per_cent['СКБ']*money/100, per_cent['ВТБ']*money/100, per_cent['СБЕР']*money/100]
depos = list(map(int, depos))
print("deposit =",depos)
print("Максимальная сумма, которую вы можете заработать -", max(depos))