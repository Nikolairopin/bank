# Задание 1
Было решено создать 3 таблицы: 
* 1) В agent_data хранится вся информация, которая может попасть под действие закона о персональных данных, из-за чего считаю логичным объединить все данные о клиенте и присвоить каждой записи id который станет внешним ключом.
* 2) В таблице setting_serv представлена информация касательно продуктов приобретаемых клиентом, важно отметить, что в  таблице есть бинарные атрибуты serv_a и serv_b - они отражают дополнительные услуги, которые клиент приобретает по желанию, по умолчанию False (бинарные, потому что клиент или сотрудник ставит флажок).  Внешним ключом является id_sevreses.
* 3) Третья таблица переставляет из себя записи с id заявки, id клиента, даты начала долговых обязательств и id пакета услуг.

Для обозначения времени используется data и datatime, для числовых значений - int, для смешанных и строковых - varchar, для хранения телефонных номеров - bigint. 

Сегмент бд находится в 3-й нормальной форме. 

![image](https://github.com/Nikolairopin/bank/assets/126417867/d34bba90-bd86-4633-860c-1091835fdab2)
# Задание 2: Напишите SQL-запрос, который бы возвращал самый популярный вид продукта за текущий год
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
# Задание 3:

![image](https://github.com/Nikolairopin/bank/assets/126417867/c91b08c1-83fc-44fe-afa0-9b638c9198d6)


Где:

* (A) – ежемесячный платеж,
* (P) – сумма кредита (body),
* (r) – месячная процентная ставка (interest/12),
* (n) – срок кредита в месяцах (length_loan).
Основной долг - часть каждого аннуитетного платежа, идущая на погашение основного долга. Рассчитывается как разница между ежемесячным платежом и долгом по процентам в соответствующем месяце.

Долг по процентам - рассчитывается на основе остатка основного долга и месячной процентной ставки.

Остаток основного долга - рассчитывается как разница между остатком долга на начало месяца и основной долгом, погашаемым в данном месяце.


```python
class LoanCalculator:
    def __init__(self, body, interest, length_loan):
        self.body = body
        self.interest = interest
        self.length_loan = length_loan

    def calculate_annuity_payment(self):
        monthly_interest = self.interest / 12 / 100
        annuity_payment = self.body * (monthly_interest * (1 + monthly_interest) ** self.length_loan) / (
                    (1 + monthly_interest) ** self.length_loan - 1)

        remaining_principal = self.body
        payments_schedule = []

        for month in range(1, self.length_loan + 1):
            interest_payment = remaining_principal * monthly_interest
            principal_payment = annuity_payment - interest_payment
            remaining_principal -= principal_payment

            payments_schedule.append({
                "Месяц": month,
                "Ежемесячный платеж": round(annuity_payment, 2),
                "Основной долг": round(principal_payment, 2),
                "Долг по процентам": round(interest_payment, 2),
                "Остаток основного долга": round(remaining_principal, 2)
            })

        return payments_schedule


# Тест 1
calculator1 = LoanCalculator(100000, 10, 12)  # Сумма кредита 100000, годовая процентная ставка 10%, срок 12 месяцев
schedule1 = calculator1.calculate_annuity_payment()
print("Тестовый набор данных 1:")
for payment in schedule1:
    print(payment)

# Тест 2
calculator2 = LoanCalculator(500000, 8, 24)  # Сумма кредита 500000, процент 8%, срок 24 месяца
schedule2 = calculator2.calculate_annuity_payment()
print("\nТестовый набор данных 2:")
for payment in schedule2:
    print(payment)

# Тест 3
calculator3 = LoanCalculator(50000, 15, 6)
schedule3 = calculator3.calculate_annuity_payment()
print("\nТестовый набор данных 3:")
for payment in schedule3:
    print(payment)
```
 # Выход
```python
Тестовый набор данных 1:
{'Месяц': 1, 'Ежемесячный платеж': 8791.59, 'Основной долг': 7958.26, 'Долг по процентам': 833.33, 'Остаток основного долга': 92041.74}
{'Месяц': 2, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8024.57, 'Долг по процентам': 767.01, 'Остаток основного долга': 84017.17}
{'Месяц': 3, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8091.45, 'Долг по процентам': 700.14, 'Остаток основного долга': 75925.72}
{'Месяц': 4, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8158.87, 'Долг по процентам': 632.71, 'Остаток основного долга': 67766.85}
{'Месяц': 5, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8226.86, 'Долг по процентам': 564.72, 'Остаток основного долга': 59539.99}
{'Месяц': 6, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8295.42, 'Долг по процентам': 496.17, 'Остаток основного долга': 51244.56}
{'Месяц': 7, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8364.55, 'Долг по процентам': 427.04, 'Остаток основного долга': 42880.01}
{'Месяц': 8, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8434.26, 'Долг по процентам': 357.33, 'Остаток основного долга': 34445.76}
{'Месяц': 9, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8504.54, 'Долг по процентам': 287.05, 'Остаток основного долга': 25941.22}
{'Месяц': 10, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8575.41, 'Долг по процентам': 216.18, 'Остаток основного долга': 17365.8}
{'Месяц': 11, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8646.87, 'Долг по процентам': 144.72, 'Остаток основного долга': 8718.93}
{'Месяц': 12, 'Ежемесячный платеж': 8791.59, 'Основной долг': 8718.93, 'Долг по процентам': 72.66, 'Остаток основного долга': -0.0}

Тестовый набор данных 2:
{'Месяц': 1, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19280.31, 'Долг по процентам': 3333.33, 'Остаток основного долга': 480719.69}
{'Месяц': 2, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19408.85, 'Долг по процентам': 3204.8, 'Остаток основного долга': 461310.84}
{'Месяц': 3, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19538.24, 'Долг по процентам': 3075.41, 'Остаток основного долга': 441772.6}
{'Месяц': 4, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19668.5, 'Долг по процентам': 2945.15, 'Остаток основного долга': 422104.1}
{'Месяц': 5, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19799.62, 'Долг по процентам': 2814.03, 'Остаток основного долга': 402304.49}
{'Месяц': 6, 'Ежемесячный платеж': 22613.65, 'Основной долг': 19931.62, 'Долг по процентам': 2682.03, 'Остаток основного долга': 382372.87}
{'Месяц': 7, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20064.49, 'Долг по процентам': 2549.15, 'Остаток основного долга': 362308.38}
{'Месяц': 8, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20198.26, 'Долг по процентам': 2415.39, 'Остаток основного долга': 342110.12}
{'Месяц': 9, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20332.91, 'Долг по процентам': 2280.73, 'Остаток основного долга': 321777.21}
{'Месяц': 10, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20468.46, 'Долг по процентам': 2145.18, 'Остаток основного долга': 301308.74}
{'Месяц': 11, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20604.92, 'Долг по процентам': 2008.72, 'Остаток основного долга': 280703.82}
{'Месяц': 12, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20742.29, 'Долг по процентам': 1871.36, 'Остаток основного долга': 259961.54}
{'Месяц': 13, 'Ежемесячный платеж': 22613.65, 'Основной долг': 20880.57, 'Долг по процентам': 1733.08, 'Остаток основного долга': 239080.97}
{'Месяц': 14, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21019.77, 'Долг по процентам': 1593.87, 'Остаток основного долга': 218061.2}
{'Месяц': 15, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21159.9, 'Долг по процентам': 1453.74, 'Остаток основного долга': 196901.29}
{'Месяц': 16, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21300.97, 'Долг по процентам': 1312.68, 'Остаток основного долга': 175600.32}
{'Месяц': 17, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21442.98, 'Долг по процентам': 1170.67, 'Остаток основного долга': 154157.34}
{'Месяц': 18, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21585.93, 'Долг по процентам': 1027.72, 'Остаток основного долга': 132571.41}
{'Месяц': 19, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21729.84, 'Долг по процентам': 883.81, 'Остаток основного долга': 110841.58}
{'Месяц': 20, 'Ежемесячный платеж': 22613.65, 'Основной долг': 21874.7, 'Долг по процентам': 738.94, 'Остаток основного долга': 88966.88}
{'Месяц': 21, 'Ежемесячный платеж': 22613.65, 'Основной долг': 22020.53, 'Долг по процентам': 593.11, 'Остаток основного долга': 66946.34}
{'Месяц': 22, 'Ежемесячный платеж': 22613.65, 'Основной долг': 22167.34, 'Долг по процентам': 446.31, 'Остаток основного долга': 44779.01}
{'Месяц': 23, 'Ежемесячный платеж': 22613.65, 'Основной долг': 22315.12, 'Долг по процентам': 298.53, 'Остаток основного долга': 22463.89}
{'Месяц': 24, 'Ежемесячный платеж': 22613.65, 'Основной долг': 22463.89, 'Долг по процентам': 149.76, 'Остаток основного долга': -0.0}

Тестовый набор данных 3:
{'Месяц': 1, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8076.69, 'Долг по процентам': 625.0, 'Остаток основного долга': 41923.31}
{'Месяц': 2, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8177.65, 'Долг по процентам': 524.04, 'Остаток основного долга': 33745.66}
{'Месяц': 3, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8279.87, 'Долг по процентам': 421.82, 'Остаток основного долга': 25465.79}
{'Месяц': 4, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8383.37, 'Долг по процентам': 318.32, 'Остаток основного долга': 17082.42}
{'Месяц': 5, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8488.16, 'Долг по процентам': 213.53, 'Остаток основного долга': 8594.26}
{'Месяц': 6, 'Ежемесячный платеж': 8701.69, 'Основной долг': 8594.26, 'Долг по процентам': 107.43, 'Остаток основного долга': -0.0}
```
 # код на java script 
```js
function calculateAnnuityPayment(body, interest, lengthLoan) {
    let monthlyInterest = interest / 12 / 100;
    let annuityPayment = body * (monthlyInterest * Math.pow((1 + monthlyInterest), lengthLoan)) / (Math.pow((1 + monthlyInterest), lengthLoan) - 1);
    
    let remainingPrincipal = body;
    let paymentsSchedule = [];
    
    for (let month = 1; month <= lengthLoan; month++) {
        let interestPayment = remainingPrincipal * monthlyInterest;
        let principalPayment = annuityPayment - interestPayment;
        remainingPrincipal -= principalPayment;
        
        paymentsSchedule.push({
            "Месяц": month,
            "Ежемесячный платеж": annuityPayment.toFixed(2),
            "Основной долг": principalPayment.toFixed(2),
            "Долг по процентам": interestPayment.toFixed(2),
            "Остаток основного долга": remainingPrincipal.toFixed(2)
        });
    }
    
    return paymentsSchedule;
}

// Тестовые данные
let body = 100000; // Сумма кредита
let interest = 10; // Годовая процентная ставка
let lengthLoan = 12; // Срок кредита в месяцах

let schedule = calculateAnnuityPayment(body, interest, lengthLoan);
schedule.forEach(payment => {
    console.log(payment);
});
```

