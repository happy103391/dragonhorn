from django.db import models
import datetime


# Create your models here.


# class Customer(models.Model):
#        name = models.CharField(max_length=10)
#        def __str__(self):
#            return self.name

class Matirial(models.Model):       
    m_number = models.IntegerField(primary_key=True,verbose_name="原料編號")                        
    m_name = models.CharField(max_length = 10,verbose_name="原料名稱")                              #原料名

    # choices = (
    #      ('存貨足夠：','不用訂貨'),
    #      ('存貨不足','記得訂貨')
    # )
    #m_status = models.CharField(max_length=50)             #狀態（足夠 or 缺貨）

    m_left_amount = models.IntegerField(verbose_name="剩餘數量")                                   #剩餘量
    m_safe_inventory = models.IntegerField(verbose_name="安全存貨量")   #安全存貨：三位數，小數點後一位
    
    def __str__(self):
        return '原料編號:{0} 原料名稱:{1}'.format(self.m_number, self.m_name)
    class Meta:
        verbose_name_plural="原料量"


class product(models.Model):                        #各飲料配方資料庫
    #p_record = models.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    p_id = models.IntegerField(verbose_name="飲品編號")            #1~5
    p_name = models.CharField(max_length = 10,verbose_name="飲品名稱")
    p_price = models.IntegerField(verbose_name="飲品價格")
    blacktea = models.IntegerField(default=0,verbose_name="紅茶用量")
    milk = models.IntegerField(default=0,verbose_name="牛奶用量")
    pearl = models.IntegerField(default=0,verbose_name="珍珠用量")
    taro = models.IntegerField(default=0,verbose_name="芋圓用量")
    honey = models.IntegerField(default=0,verbose_name="蜂蜜用量")

    class Meta:
        verbose_name_plural="各飲品原料用量"


class DailyRecord(models.Model):                                            #記錄每天的量
    
    sell_date = models.DateField(('Date'), default=datetime.date.today)
    sell_pd1 = models.IntegerField(default=0,verbose_name="濃厚奶茶 銷量")     #濃厚奶茶今天的銷量
    sell_pd2 = models.IntegerField(default=0,verbose_name="濃厚小芋圓奶茶 銷量")     #濃厚小芋圓今天的銷量
    sell_pd3 = models.IntegerField(default=0,verbose_name="濃厚珍珠奶茶 銷量")   #濃厚珍珠奶茶今天的銷量
    sell_pd4 = models.IntegerField(default=0,verbose_name="特濃蜂蜜牛奶 銷量")   #特濃蜂蜜牛奶今天的銷量
    # choices = (
    #     ('存貨足夠：','不用訂貨'),
    #     ('存貨不足','記得訂貨')
    # )
    sell_pd5 = models.IntegerField(default=0,verbose_name="蜂蜜珍珠鮮奶 銷量")   #蜂蜜珍珠鮮奶今天的銷量
    
    # p_name = models.CharField(max_length = 10)
    # p_price = models.IntegerField()
    # blacktea = models.IntegerField(default=0)
    # milk = models.IntegerField(default=0)
    # pearl = models.IntegerField(default=0)
    # taro = models.IntegerField(default=0)
    # honey = models.IntegerField(default=0)
    
    def __datetime__(self):
           return self.sell_date                #從後台選日期
    class Meta:
        verbose_name_plural="產品每日銷售量"

class addMaterial(models.Model):               #從後台新增進貨量
    add_date = models.DateField(('Date'), default=datetime.date.today)
    add_blacktea = models.IntegerField(default=0,verbose_name="紅茶進貨（袋）")
    add_milk = models.IntegerField(default=0,verbose_name="牛奶進貨（罐）")
    add_pearl = models.IntegerField(default=0,verbose_name="珍珠進貨（包）")
    add_taro = models.IntegerField(default=0, verbose_name="芋圓進貨（包）")
    add_honey = models.IntegerField(default=0,verbose_name="蜂蜜進貨（罐）")

    class Meta:
        verbose_name_plural="新增產品每日進貨量"
    

# class LeftMatirial(models.Model): 
#     left_blacktea = models.DecimalField(max_digits=10, decimal_places=2,default =0)                                           #記錄每天的量
#     left_milk = models.DecimalField(max_digits=10, decimal_places=2,default = 0)     #濃厚奶茶剩下的量
#     left_peral = models.DecimalField(max_digits=10, decimal_places=2,default = 0)     #濃厚小芋圓剩下的量
#     left_toro = models.DecimalField(max_digits=10, decimal_places=2,default = 0)   #濃厚珍珠奶茶剩下的量

    
    

    

    
#     def __datetime__(self):
#            return self.sell_date

#class DailyUse(models.Model):                                            #記錄每個原料一天的用量
#     sell_blacktea = int(DailyRecord.sell_pd1)*300     #濃厚奶茶今天的銷量
#     sell_milk = int(DailyRecord.sell_pd1)*200     #濃厚小芋圓今天的銷量
#     sell_pearl = int(DailyRecord.sell_pd1)*20   #濃厚珍珠奶茶今天的銷量
#     sell_toro = int(DailyRecord.sell_pd1)*20   #特濃蜂蜜牛奶今天的銷量
#     sell_honey = int(DailyRecord.sell_pd1)*20    #蜂蜜珍珠鮮奶今天的銷量
    
#     def __datetime__(self):
#            return self.sell_date


                