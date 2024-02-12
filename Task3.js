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