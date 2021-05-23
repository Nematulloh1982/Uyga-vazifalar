# Muallif: Azamkhanov Nematilla 
#    AMALIYOT N8 27.02.2021 



davlatlar=['Qozog\'iston', 'Azarbayjon', 'O\'zbekiston', 'Arabiston', 'Yaponiya']

print('Davlatlarning soni:',len(davlatlar), 'ga teng\n')
print('sorted() funksiyasida Alifbo bo\'yicha:',(sorted(davlatlar)))
print('\nsorted() funksiyasida Ters alifbo bo\'yicha:\n',(sorted(davlatlar, reverse=True)))
print('\nAsl ro\'yxat: \n',(davlatlar))
davlatlar.reverse()
print('\nAsl ro\'yxat reverse() metodi yordamida: ',davlatlar)
davlatlar.sort()
print('\nsort() metodida Alifbo bo\'yicha:',davlatlar)
davlatlar.sort(reverse=True)
print('\nsort() metodida Ters Alifbo bo\'yicha:',davlatlar)


sonlar=list( range(120, 1201, 2))
print(('120 - dan 1200 - gacha bo\'lgan sonlar:\n\n'),sonlar)
print()
print('Ushbu sonlarning yi\'g\'indisi:',sum(sonlar), "- ga teng\n")
print('Ro\'yxatdagi eng katta sondan eng kichik sonni ayirganda',max(sonlar)-min(sonlar), 'chiqadi\n')
print("Ro\'yxatdagi elementlar soni",len(sonlar), "- ga teng\n")

print("Boshidan 5 ta son:",sonlar[:5])
print("Oxiridan 5 ta son:",sonlar[-5:])




taomlar=['Jarkop', 'Palov', 'Chuchvara', 'lagmon', 'Sho\'rva']
print("Taomlar ro'yxati:",taomlar)
print()
nonushta = taomlar[:]
print("Taomlardan Nonushtaga nusxa olingan ro'yxat:\n",nonushta)
print()
nonushta.remove('Jarkop')
nonushta.remove("lagmon")
nonushta.remove('Chuchvara')
nonushta.insert(0, "Salat")
nonushta.insert(2, "Kasha")
print("Taomlar ro'yxati:\n",taomlar)
print("\nNonushtaga o'zgarishlar kiritgandan so'ng:\n",nonushta)