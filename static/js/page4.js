document.addEventListener("DOMContentLoaded", function () {
    let totalCashElement = document.getElementById("total-cash");
    let totalVodCashElement = document.getElementById("total-vod-cash");
    let totalExpensesElement = document.getElementById("total-cash-out");

    let cashTotals = {};
    let vodCashTotals = {};
    let expensesTotals = {};

    function calculateTotals(containerId, totalsObj) {
        let container = document.getElementById(containerId);
        let orders = container.querySelectorAll("p");

        orders.forEach((p) => {
            if (p.innerHTML.includes("إجمالي السعر")) {
                let value = parseFloat(p.innerText.replace("إجمالي السعر:", "").trim()) || 0;
                let dateElement = p.nextElementSibling;
                
                if (dateElement && dateElement.innerHTML.includes("التاريخ والوقت")) {
                    let date = dateElement.innerText.replace("التاريخ والوقت:", "").trim().split(",")[0];
                    
                    if (!totalsObj[date]) {
                        totalsObj[date] = 0;
                    }
                    totalsObj[date] += value;
                }
            }
        });
    }

    calculateTotals("first", cashTotals);
    calculateTotals("second", vodCashTotals);
    calculateTotals("third", expensesTotals);

    function createTable(title, data) {
        let table = `<h2>${title}</h2><table border='1' style="width: 100%; border-collapse: collapse;">`;
        table += `<tr><th>التاريخ</th><th>الإجمالي</th></tr>`;
        for (let date in data) {
            table += `<tr><td style="padding: 10px; border: 1px solid black;">${date}</td></tr>`;
            table += `<tr><td colspan="2" style="padding: 10px; border: 1px solid black; text-align: center;">${data[date].toFixed(2)} جنيه</td></tr>`;
        }
        table += "</table>";
        return table;
    }

    totalCashElement.innerHTML = createTable("إجمالي الكاش لكل يوم", cashTotals);
    totalVodCashElement.innerHTML = createTable("إجمالي المحفظة لكل يوم", vodCashTotals);
    totalExpensesElement.innerHTML = createTable("إجمالي المصاريف لكل يوم", expensesTotals);
});