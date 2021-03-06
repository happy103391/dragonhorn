# Generated by Django 3.0 on 2020-01-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0013_auto_20191231_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addmaterial',
            options={'verbose_name': '新增產品每日進貨量'},
        ),
        migrations.AlterModelOptions(
            name='dailyrecord',
            options={'verbose_name': '產品每日銷售量'},
        ),
        migrations.AlterModelOptions(
            name='matirial',
            options={'verbose_name': '原料量'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '各飲品原料用量'},
        ),
        migrations.AlterField(
            model_name='addmaterial',
            name='add_blacktea',
            field=models.IntegerField(default=0, verbose_name='紅茶進貨（袋）'),
        ),
        migrations.AlterField(
            model_name='addmaterial',
            name='add_honey',
            field=models.IntegerField(default=0, verbose_name='蜂蜜進貨（罐）'),
        ),
        migrations.AlterField(
            model_name='addmaterial',
            name='add_milk',
            field=models.IntegerField(default=0, verbose_name='牛奶進貨（罐）'),
        ),
        migrations.AlterField(
            model_name='addmaterial',
            name='add_pearl',
            field=models.IntegerField(default=0, verbose_name='珍珠進貨（包）'),
        ),
        migrations.AlterField(
            model_name='addmaterial',
            name='add_taro',
            field=models.IntegerField(default=0, verbose_name='芋圓進貨（包）'),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='sell_pd1',
            field=models.IntegerField(default=0, verbose_name='濃厚奶茶 銷量'),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='sell_pd2',
            field=models.IntegerField(default=0, verbose_name='濃厚小芋圓奶茶 銷量'),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='sell_pd3',
            field=models.IntegerField(default=0, verbose_name='濃厚珍珠奶茶 銷量'),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='sell_pd4',
            field=models.IntegerField(default=0, verbose_name='特濃蜂蜜牛奶 銷量'),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='sell_pd5',
            field=models.IntegerField(default=0, verbose_name='蜂蜜珍珠鮮奶 銷量'),
        ),
        migrations.AlterField(
            model_name='matirial',
            name='m_left_amount',
            field=models.IntegerField(verbose_name='剩餘數量'),
        ),
        migrations.AlterField(
            model_name='matirial',
            name='m_name',
            field=models.CharField(max_length=10, verbose_name='原料名稱'),
        ),
        migrations.AlterField(
            model_name='matirial',
            name='m_number',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='原料編號'),
        ),
        migrations.AlterField(
            model_name='matirial',
            name='m_safe_inventory',
            field=models.IntegerField(verbose_name='安全存貨量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='blacktea',
            field=models.IntegerField(default=0, verbose_name='紅茶用量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='honey',
            field=models.IntegerField(default=0, verbose_name='蜂蜜用量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='milk',
            field=models.IntegerField(default=0, verbose_name='牛奶用量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_id',
            field=models.IntegerField(verbose_name='飲品編號'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_name',
            field=models.CharField(max_length=10, verbose_name='飲品名稱'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.IntegerField(verbose_name='飲品價格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pearl',
            field=models.IntegerField(default=0, verbose_name='珍珠用量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='taro',
            field=models.IntegerField(default=0, verbose_name='芋圓用量'),
        ),
    ]
