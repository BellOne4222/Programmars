terms = ["Z 3", "D 5"]

terms_dict = {} # 약관 종류와 유효기간을 딕셔너리로 저장
for i in terms:
    term, expiration_date = i.split()
    terms_dict[term] = expiration_date

print(int(terms_dict['Z']) > 2)