st = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

number = len(st)
invers = st[::-1]
big = st.title()
bigup = st.upper()
nd =st.count('нд')
am = st.count('ам')
o = st.count('о')
change = st.replace('Лондоне','Минске')
section = st.split()

print(f'Шаг1 - Количество символов - {number}\nШаг2 - Развернутая строка - {invers}\n\
Шаг3 - Заглавные буквы - {big}\nШаг4 - Прописные буквы - {bigup}\nШаг5 - Число вхождений нд - {nd}\n\
Шаг5 - Число вхождений ам - {am}\nШаг5 - Число вхождений о - {o}\nШаг6 - Изменить город - {change}\n\
Шаг7 - Разбить строку - {section}\n')
