window.onload = function() {
    var annualFund = document.getElementsByName("annualFunding")[0],
        finCurPer = document.getElementsByName("finCurPeriod")[0],
        finEnd = document.getElementsByName("finEndYear")[0];
    annualFund.addEventListener('input', function() {
        finCurPer.value = annualFund.value;
        finEnd.value = annualFund.value;
    });
};
