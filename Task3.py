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