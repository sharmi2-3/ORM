# Generated by Django 5.1.2 on 2024-10-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankLoan',
            fields=[
                ('Name', models.CharField(max_length=8)),
                ('Accountno', models.IntegerField(primary_key='Accountno', serialize=False)),
                ('age', models.IntegerField()),
                ('Income', models.IntegerField()),
                ('Loanamount', models.IntegerField()),
            ],
        ),
    ]