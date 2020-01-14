from django.db import models
from _datetime import date

# Create your models here.
class Customer(models.Model):

    c_name = models.CharField(max_length=11,verbose_name="會員姓名")   #顧客名:最大長度為11
    c_ID = models.IntegerField(primary_key=True,verbose_name="會員卡號")    #卡號:是一串整數，最大長度為11 (2014/12/25辦卡的就打: 20141225001)
    c_sex = models.IntegerField(verbose_name="性別")                 #性別:1:male  2:female
    c_point = models.IntegerField(default=0,verbose_name="累計點數") 
    c_birth = models.DateField(default=date.today,verbose_name="會員生日")     #累計點數:預設為0
    def __integer__(self):
        return self.c_ID
    class Meta:
        verbose_name_plural="會員"
    


class Item(models.Model):                        #這裡記載，以及這個月的銷量
    item_num = models.IntegerField(primary_key=True,verbose_name="品項編號")             #品項編號:五杯品項有不同編號(1~5)
    item_name = models.CharField(max_length=20,verbose_name="品項名稱")  #品項名稱
    item_price = models.DecimalField(max_digits=3,decimal_places=0,verbose_name="品項價格")  #各品項價錢
    item_sales = models.IntegerField(default=0,verbose_name="銷量（杯）")        #這個月的銷量:預設為0
    class Meta:
        verbose_name_plural="各品項銷量"


# class PurRecord(models.Model):
#     trade_num = models.IntegerField()           #交易編號:最大長度為11(2019/12/25買的就打:20191225001)
#     c_ID = models.ForeignKey(Customer.c_ID,on_delete=models.CASCADE)     #顧客卡號(判斷這筆紀錄是誰的,若同個人買了不同飲料，就算兩筆不同紀錄)
#                                                                          #on_delete = models.CASCADE 表示一對一關係，要是有 foreign key的時候記得要加
#     item_num = models.ForeignKey(Item.item_num,on_delete=models.CASCADE) #買了甚麼
#     buy_amount = models.IntegerField(default=0)   #買了幾杯
#     buy_total = models.IntegerField()             #買的總價格  這裡之後要讓上面兩項相乘
#     pur_time = models.DateTimeField(auto_now_add=True)  #新增資料時會?你自動加上建立時間

class PurRecord(models.Model):
    trade_num = models.IntegerField(primary_key=True,verbose_name="交易記錄編號")           #交易編號:最大長度為11(2019/12/25買的就打:20191225001)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE,verbose_name="會員卡號")     #顧客卡號(判斷這筆紀錄是誰的,若同個人買了不同飲料，就算兩筆不同紀錄)
                                                                         #on_delete = models.CASCADE 表示一對一關係，要是有 foreign key的時候記得要加
   
    item_num = models.ForeignKey(Item, on_delete = models.CASCADE,verbose_name="購買品項") #買了甚麼
    buy_amount = models.IntegerField(default=0,verbose_name="購買數量")   #買了幾杯
    buy_total = models.IntegerField(verbose_name="購買總金額")              #買的總價格  這裡之後要讓上面兩項相乘
    pur_time = models.CharField(max_length=7,verbose_name="購買時間")    #新增資料時會?
    class Meta:
        verbose_name_plural="購買記錄"