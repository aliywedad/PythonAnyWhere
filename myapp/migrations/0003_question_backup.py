# Generated by Django 2.2.22 on 2024-05-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240506_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('choices', models.TextField()),
                ('sub_categorie', models.TextField()),
                ('categorie', models.TextField()),
                ('parent', models.TextField()),
                ('type', models.CharField(choices=[('text', 'Text'), ('choice', 'Choice'), ('composite', 'Composite'), ('checkbox', 'Checkbox'), ('radio', 'Radio')], max_length=10)),
            ],
            options={
                'db_table': 'question-backup',
            },
        ),
    ]
