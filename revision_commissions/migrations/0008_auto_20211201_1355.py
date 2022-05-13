# Generated by Django 3.2.8 on 2021-12-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision_commissions', '0007_auto_20211125_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='administrativeMeasures',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Административные меры в результате выявленных нарушений по государственным закупкам'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='annualFunding',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Годовой объем финансирования учреждения'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='cashExpense',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Кассовый расход(исполнение плаченных обязательств по бюджетным программам (подпрограммам)'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='cashExpenseCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Кассовый расход (исполнение оплаченных обязательств по бюджетным программам (подпрограммам)) текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='disciplineMeasures',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Дисциплинарные меры в результате выявленных нарушений по государственным закупкам'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='disciplineSanctions',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Дисциплинарные взыскания, дискредитирующие государственную службу'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='employeeEthics',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='finCurPeriod',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем финансирования текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='finEndYear',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем финансирования на конец финансового года'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='finPrePeriod',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем финансирования прошлого периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='finViolations',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем выявленных финансовых нарушений'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='firedViolation',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Увольнение в результате выявленных нарушений по государственным закупкам'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='illegalActions',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Коррупционные и уголовные действия при освоении бюджетных средств'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='materialEthics',
            field=models.PositiveIntegerField(help_text='Ед.', null=True, verbose_name='Количество материалов рассмотренных советом по этике'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='payableCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем кредиторской  задолженности текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='payablePrevious',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем кредиторской  задолженности прошлого периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='preLastAudit',
            field=models.PositiveIntegerField(help_text='Год', null=True, verbose_name='Срок с момента проведения последнего государственного аудита'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volAdministrativeSpendings',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем административных расходов текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volAuthorizedCapitalCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем уставного капитала текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volAuthorizedCapitalPrevious',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем уставного капитала прошлого периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volDividentsCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем дивидендов текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volIncomeCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем чистой прибыли текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volIncomePrevious',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем чистой прибыли прошлого периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volReceivableCurrent',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем дебиторской задолженности текущего периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volReceivablePrevious',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем дебиторской задолженности прошлого периода'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='volRecoverFin',
            field=models.DecimalField(decimal_places=3, help_text='Тыс.тг', max_digits=15, null=True, verbose_name='Объем востановленных/возмещенных средств'),
        ),
    ]
