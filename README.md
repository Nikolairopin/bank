# Задание 1
Было решено создать 3 таблицы в agent_data хранится вся информация которая может попасть под действие закона о персональных данных, из-за чего считаю логичным объединить все данные о клиенте и присвоить каждой записи id который станет внешним ключом. В таблице setting_serv представлена информация, касательно продуктов приобретаемых клиентом, важно заметить что в  таблице есть бинарные атрибуты serv_a и serv_b они отражают дополнительные услуги которые клиент приобретает по желанию, по умолчанию False(бинарные потому что клиент ставит флажок и не может настроить из  условия задачи).  Внешним ключом является id_sevreses. Третья таблица переставляет из себя записи с id заявки id клиента даты начала  долговых обязательств и id пакета услуг. Для обозначения времени используется data и datatime для числовых значений int для смешанных и строковых используется varchar для хранения телефонных номеров используется bigint. Сегмент бд находится в 3-й нормальной форме. 
![image](https://github.com/Nikolairopin/bank/assets/126417867/d34bba90-bd86-4633-860c-1091835fdab2)
# Задание 2: Код на sql
```sql 
SELECT
  setting_serv.type,
  COUNT(applications.id_appl) AS num_applications
FROM
  application_storege.applications
JOIN
  application_storege.setting_serv ON applications.id_sevreses = setting_serv.id_sevreses
WHERE
  EXTRACT(YEAR FROM applications.date_start) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY
  setting_serv.type
ORDER BY
  num_applications DESC
LIMIT 1;
```
