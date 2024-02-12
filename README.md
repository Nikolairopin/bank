# Задание 1
Было решено создать 3 таблицы в agent_data хранится вся информация которая может попасть под действие закона о персональных данных, из-за чего считаю логичным объединить все данные о клиенте и присвоить каждой записи id который станет внешним ключом. В таблице setting_serv представлена информация, касательно продуктов приобретаемых клиентом, важно заметить что в  таблице есть бинарные атрибуты serv_a и serv_b они отражают дополнительные услуги которые клиент приобретает по желанию, по умолчанию False(бинарные потому что клиент ставит флажок и не может настроить из  условия задачи).  Внешним ключом является id_sevreses. Третья таблица переставляет из себя записи с id заявки id клиента даты начала  долговых обязательств и id пакета услуг. Для обозначения времени используется data и datatime для числовых значений int для смешанных и строковых используется varchar для хранения телефонных номеров используется bigint. Сегмент бд находится в 3-й нормальной форме. 
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
Задание 3:
```pyton
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
``` ```
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
``` ```
