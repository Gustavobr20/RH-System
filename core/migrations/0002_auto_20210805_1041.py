# Generated by Django 3.1.1 on 2021-08-05 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='legal_number',
            field=models.CharField(default='', max_length=14, unique=True, verbose_name='CNPJ'),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='', upload_to='media', verbose_name='Logo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Nome Fantasia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='Admin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='core.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='core.department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
