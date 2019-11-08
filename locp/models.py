from django.db import models

# Create your models here.

class Leixin(models.Model):
    LEIXIN_TEXT = (
        ('小医院', '控制节点，工作节点，存储节点混合部署'),
        ('大医院', '控制节点，工作节点，存储节点单独部署'),
    )
    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=LEIXIN_TEXT)

class HunhePeizhi(models.Model):
    HPEIZHI_TEXT = (
        ('少量应用', '8C32G1T'),
        ('中等应用', '16C64G2T'),
        ('大量应用', '32C128G4T')
    )
    name = models.CharField(max_length=50)
    peizhi_size = models.CharField(max_length=1, choices=HPEIZHI_TEXT)

class DuliPeizhi(models.Model):
    CPEIZHI_TEXT = (
        ('基本配置', '2C4G100G'),
        ('推荐配置', '4C8G200G'),
    )
    WPEIZHI_TEXT = (
        ('少量应用', '8C32G500G'),
        ('中等应用', '16C64G500G'),
        ('大量应用', '32C128G500G')
    )
    SPEIZHI_TEXT = (
        ('少量数据', '2C4G1T'),
        ('中等数据', '4C8G2T'),
        ('大量数据', '8C16G4T'),
    )

    name = models.CharField(max_length=50)
    cpeizhi_size = models.CharField(max_length=1, choices=CPEIZHI_TEXT)
    wpeizhi_size = models.CharField(max_length=1, choices=WPEIZHI_TEXT)
    speizhi_size = models.CharField(max_length=1, choices=SPEIZHI_TEXT)

