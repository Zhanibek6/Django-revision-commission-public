from django.db import models
from django.db.models.fields import CharField, EmailField
from django.contrib.auth.models import User
from accounts.models import CustomUser

    
class Organization_GU(models.Model):
    """Ввод данных информации о бюджете."""
    type = models.CharField("Тип организации", default="ГУ", max_length=5)

    name = models.CharField('Наименование организации', max_length=30)

    annualFunding = models.DecimalField('Годовой объем финансирования учреждения', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    finPrePeriod = models.DecimalField('Объем финансирования прошлого периода', help_text='Тыс.тг', max_digits=15,
                                       decimal_places=3, null=True)

    finCurPeriod = models.DecimalField('Объем финансирования текущего периода', help_text='Тыс.тг', max_digits=15,
                                       decimal_places=3, null=True)

    finEndYear = models.DecimalField('Объем финансирования на конец финансового года', help_text='Тыс.тг',
                                     max_digits=15, decimal_places=3, null=True)

    cashExpense = models.DecimalField(
        'Кассовый расход(исполнение плаченных обязательств по бюджетным программам (подпрограммам)', help_text='Тыс.тг',
        max_digits=15, decimal_places=3, null=True)

    dateLastCheck = models.DateField('Дата проведения последней проверки', null=True)

    dateReport = models.DateField('Фактическая дата на конец отчетного периода', null=True)

    finViolations = models.DecimalField('Объем выявленных финансовых нарушений', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    volRecoverFin = models.DecimalField('Объем востановленных/возмещенных средств', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    volReceivableCurrent = models.DecimalField('Объем дебиторской задолженности текущего периода', help_text='Тыс.тг',
                                               max_digits=15, decimal_places=3, null=True)

    volReceivablePrevious = models.DecimalField('Объем дебиторской задолженности прошлого периода', help_text='Тыс.тг',
                                                max_digits=15, decimal_places=3, null=True)

    payableCurrent = models.DecimalField('Объем кредиторской  задолженности текущего периода', help_text='Тыс.тг',
                                         max_digits=15, decimal_places=3, null=True)

    payablePrevious = models.DecimalField('Объем кредиторской  задолженности прошлого периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    illegalActions = models.PositiveIntegerField('Коррупционные и уголовные действия при освоении бюджетных средств',
                                         help_text='Ед.', null=True)

    disciplineSanctions = models.PositiveIntegerField('Дисциплинарные взыскания, дискредитирующие государственную службу',
                                              help_text='Ед.', null=True)

    materialEthics = models.PositiveIntegerField('Количество материалов рассмотренных советом по этике', help_text='Ед.',
                                         null=True)

    employeeEthics = models.PositiveIntegerField(
        'Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике', help_text='Ед.',
        null=True)

    administrativeMeasures = models.PositiveIntegerField(
        'Административные меры в результате выявленных нарушений по государственным закупкам', help_text='Ед.',
        null=True)

    disciplineMeasures = models.PositiveIntegerField(
        'Дисциплинарные меры в результате выявленных нарушений по государственным закупкам', help_text='Ед.', null=True)

    firedViolation = models.PositiveIntegerField('Увольнение в результате выявленных нарушений по государственным закупкам',
                                         help_text='Ед.', null=True)

    score = models.IntegerField(null=True)
    risk = models.IntegerField(null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'GU Organizations'  # Имя при обращении к множеству введенных данных.

    def __str__(self):
        "Возвращает представление модели."
        return self.name


class Organization_KVAZI(models.Model):
    """Ввод данных информации о бюджете."""
    type = models.CharField("Тип организации", default="КВАЗИ", max_length=5)

    name = models.CharField('Наименование организации', max_length=30)

    annualFunding = models.DecimalField('Годовой объем финансирования учреждения', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    finEndYear = models.DecimalField('Объем финансирования на конец финансового года', help_text='Тыс.тг',
                                     max_digits=15, decimal_places=3, null=True)

    cashExpense = models.DecimalField(
        'Кассовый расход(исполнение плаченных обязательств по бюджетным программам (подпрограммам)', help_text='Тыс.тг',
        max_digits=15, decimal_places=3, null=True)

    dateLastCheck = models.DateField('Дата проведения последней проверки', null=True)

    dateReport = models.DateField('Фактическая дата на конец отчетного периода', null=True)

    finViolations = models.DecimalField('Объем выявленных финансовых нарушений', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    volRecoverFin = models.DecimalField('Объем востановленных/возмещенных средств', help_text='Тыс.тг', max_digits=15,
                                        decimal_places=3, null=True)

    volReceivableCurrent = models.DecimalField('Объем дебиторской задолженности текущего периода', help_text='Тыс.тг',
                                               max_digits=15, decimal_places=3, null=True)

    volReceivablePrevious = models.DecimalField('Объем дебиторской задолженности прошлого периода', help_text='Тыс.тг',
                                                max_digits=15, decimal_places=3, null=True)

    payableCurrent = models.DecimalField('Объем кредиторской  задолженности текущего периода', help_text='Тыс.тг',
                                         max_digits=15, decimal_places=3, null=True)

    payablePrevious = models.DecimalField('Объем кредиторской  задолженности прошлого периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    illegalActions = models.PositiveIntegerField('Коррупционные и уголовные действия при освоении бюджетных средств',
                                         help_text='Ед.', null=True)

    disciplineSanctions = models.PositiveIntegerField('Дисциплинарные взыскания, дискредитирующие государственную службу',
                                              help_text='Ед.', null=True)

    employeeEthics = models.PositiveIntegerField(
        'Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике', help_text='Ед.',
        null=True)

    administrativeMeasures = models.PositiveIntegerField(
        'Административные меры в результате выявленных нарушений по государственным закупкам', help_text='Ед.',
        null=True)

    disciplineMeasures = models.PositiveIntegerField(
        'Дисциплинарные меры в результате выявленных нарушений по государственным закупкам', help_text='Ед.', null=True)

    firedViolation = models.PositiveIntegerField('Увольнение в результате выявленных нарушений по государственным закупкам',
                                         help_text='Ед.', null=True)

    volAuthorizedCapitalCurrent = models.DecimalField('Объем уставного капитала текущего периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    volAuthorizedCapitalPrevious = models.DecimalField('Объем уставного капитала прошлого периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    volIncomeCurrent = models.DecimalField('Объем чистой прибыли текущего периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    volIncomePrevious = models.DecimalField('Объем чистой прибыли прошлого периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    volDividentsCurrent = models.DecimalField('Объем дивидендов текущего периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    volAdministrativeSpendings = models.DecimalField('Объем административных расходов текущего периода', help_text='Тыс.тг',
                                          max_digits=15, decimal_places=3, null=True)

    score = models.IntegerField(null=True)
    risk = models.IntegerField(null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Organizations KVAZI'  # Имя при обращении к множеству введенных данных.

    def __str__(self):
        "Возвращает представление модели."
        return self.name