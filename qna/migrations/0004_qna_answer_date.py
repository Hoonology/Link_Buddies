# Generated by Django 4.0.5 on 2022-06-17 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_qna_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='answer_date',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
