# Generated by Django 2.2.7 on 2019-11-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DuliPeizhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cpeizhi_size', models.CharField(choices=[('基本配置', '2C4G100G'), ('推荐配置', '4C8G200G')], max_length=1)),
                ('wpeizhi_size', models.CharField(choices=[('少量应用', '8C32G500G'), ('中等应用', '16C64G500G'), ('大量应用', '32C128G500G')], max_length=1)),
                ('speizhi_size', models.CharField(choices=[('少量数据', '2C4G1T'), ('中等数据', '4C8G2T'), ('大量数据', '8C16G4T')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='HunhePeizhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('peizhi_size', models.CharField(choices=[('少量应用', '8C32G1T'), ('中等应用', '16C64G2T'), ('大量应用', '32C128G4T')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Leixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shirt_size', models.CharField(choices=[('小医院', '控制节点，工作节点，存储节点混合部署'), ('大医院', '控制节点，工作节点，存储节点单独部署')], max_length=1)),
            ],
        ),
    ]
