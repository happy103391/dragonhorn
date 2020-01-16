from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import DailyRecord, Matirial,product,addMaterial
from .admin import DailyRecordAdmin
from django.views.generic.list import ListView
from django import forms
from django.http import HttpResponseRedirect
from django.db.models import F
# from docutils.parsers import null
from django.db.models import Sum
import datetime
import math
from django.views.generic import TemplateView
import sqlite3



# Create your views here.

# def index(request):
#     return render(request,'index.html')
# def member(request):
#     return render(request,'member.html')
# def rfm (request):
#     return render(request,'rfm.html')
# def data(request):
#     return render(request,'data.html')
# def historyrecord(request):
#     return render(request,'historyrecord.html')
# def inventory(request):
#     return render(request,'inventory.html')
# def create_inventory(request):
#     return render(request,'create_inventory.html')

# def material(request):
#     return render(request,'material.html')

def inventory(request):
    if request.method == "POST":#如果是以POST的方式才處理
        sell_date = request.POST['sell_date']    #取得表單輸入資料
        sell_pd1 = request.POST['sell_pd1']
        sell_pd2 = request.POST['sell_pd2']
        sell_pd3 = request.POST['sell_pd3']
        sell_pd4 = request.POST['sell_pd4']
        sell_pd5 = request.POST['sell_pd5']
        unit = DailyRecord.objects.create(sell_date=sell_date, sell_pd1=sell_pd1, sell_pd2=sell_pd2, sell_pd3=sell_pd3, sell_pd4=sell_pd4, sell_pd5=sell_pd5)
        unit.save()                      #寫入資料庫
        return redirect('home/inventory/')       #重導到<index.html>網頁
    else:
        message = '請輸入資料(資料不作驗證)'
    return render(request, "inventory.html", locals())



def inventory(request):


    use_list = Matirial.objects.all().order_by('m_number')

    class Meta:
        model = Matirial
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
    return render(request,'inventory.html', locals())

class CurrentUseForm(HttpResponseRedirect):
    class Meta:
        model = Matirial
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
        latest_record = DailyRecord.objects.latest('id')
        used_blacktea= (latest_record.sell_pd1 + latest_record.sell_pd2 + latest_record.sell_pd3 )*300
        Matirial.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount') - used_blacktea)


        used_milk =(latest_record.sell_pd1 + latest_record.sell_pd2 + latest_record.sell_pd3 + latest_record.sell_pd4 + latest_record.sell_pd5)*200
        Matirial.objects.all().filter(m_name='牛奶（ml）').update(m_left_amount=F('m_left_amount') - used_milk)

        used_pearl =(latest_record.sell_pd3 + latest_record.sell_pd5)*20
        Matirial.objects.all().filter(m_name='珍珠（g）').update(m_left_amount=F('m_left_amount') - used_pearl)

        used_taro =(latest_record.sell_pd2)*20
        Matirial.objects.all().filter(m_name='芋圓（g）').update(m_left_amount=F('m_left_amount') - used_taro)

        used_honey =(latest_record.sell_pd4 + latest_record.sell_pd5)*100
        Matirial.objects.all().filter(m_name='蜂蜜（g）').update(m_left_amount=F('m_left_amount') - used_honey)


class AddUseForm(HttpResponseRedirect):
    class Meta:
        model = Matirial
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
        latest_add_record = addMaterial.objects.latest('add_date')
        new_blacktea= latest_add_record.add_blacktea*30000
        Matirial.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount') + new_blacktea)
        new_milk = latest_add_record.add_milk*5000
        Matirial.objects.all().filter(m_name='牛奶（ml）').update(m_left_amount=F('m_left_amount') + new_milk)

        new_pearl = latest_add_record.add_pearl*3000
        Matirial.objects.all().filter(m_name='珍珠（g）').update(m_left_amount=F('m_left_amount') + new_pearl)

        new_taro = latest_add_record.add_taro*3000
        Matirial.objects.all().filter(m_name='芋圓（g）').update(m_left_amount=F('m_left_amount') + new_taro)

        new_honey =latest_add_record.add_honey*3000
        Matirial.objects.all().filter(m_name='蜂蜜（g）').update(m_left_amount=F('m_left_amount') + new_honey)





def historyrecord(request):           #歷史紀錄，按照日期排序
    # drecord_list = DailyRecord.objects.all().order_by('-sell_date')
    # return render(request,'historyrecord.html', locals())

    query = request.GET.get('search_res', None)
    context = {}
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]

    if query and request.method == 'GET':
        results = DailyRecord.objects.filter(sell_date=query)
        context.update({'results': results})

    return render(request,'historyrecord.html',context)

#def CalculateTodayConsume(request):


# def CountUseAmount(request):
#     result = DailyRecord.objects.all().annotate(prod=F('sell_pd1') * F('blacktea'))

class TodaySellForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]




# def material(request):
#     drecord_list = DailyRecord.objects.all().order_by('-sell_date')
#     for d in drecord_list:
#         spring_predictsell = d.filter(date__range=["2019-01-01", "2019-03-31"])

#     return render(request,'material.html',locals())

def material(request):                             #讓使用者查詢，並列出預測的量

    query = request.GET.get('search_res', None)
    context = {}
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]

    if query and request.method == 'GET':
        results = DailyRecord.objects.filter(sell_date=query)
        context.update({'results': results})
        use_list = Matirial.objects.all().order_by('m_number')

        # spring_start_date = datetime.date(2019, 1, 1)                  #春天的銷量
        # spring_end_date =  datetime.date(2019, 3, 31)
        # DailyRecord.sell_date.strftime('%Y-%m-%d')
        # spring = DailyRecord.objects.filter(sell_date=[spring_start_date, spring_end_date])
        for r in results:
                r.predicted_sell＿pd1 =math.ceil((r.sell_pd1)* 0.9)     #預測的銷售量
                r.predicted_sell＿pd2 =math.ceil((r.sell_pd2)* 1.1)
                r.predicted_sell＿pd3 =math.ceil((r.sell_pd3)* 1.2)
                r.predicted_sell＿pd4 =math.ceil((r.sell_pd4)* 0.9)
                r.predicted_sell＿pd5 =math.ceil((r.sell_pd5)* 0.8)

                r.predicted_blacktea_usage = math.ceil(r.sell_pd1 + r.sell_pd2 + r.sell_pd3 )*300     #預測的原料用量
                r.predicted_milk_usage = math.ceil(r.sell_pd1 + r.sell_pd2 + r.sell_pd3 + r.sell_pd4 + r.sell_pd5 )*200
                r.predicted_pearl_usage = math.ceil(r.sell_pd3 + r.sell_pd5 )*20
                r.predicted_taro_usage = math.ceil(r.sell_pd2)*20
                r.predicted_honey_usage = math.ceil(r.sell_pd4 + r.sell_pd5 )*100

                r.predicted_blacktea_unit = round(((r.sell_pd1 + r.sell_pd2 + r.sell_pd3 )*300/30000),1)    #預測的原料包數
                r.predicted_milk_unit = round(((r.sell_pd1 + r.sell_pd2 + r.sell_pd3 + r.sell_pd4 + r.sell_pd5 )*200/5000),2)
                r.predicted_pearl_unit = round(((r.sell_pd3 + r.sell_pd5 )*20/3000),2)
                r.predicted_taro_unit = round(((r.sell_pd2)*20/3000),2)
                r.predicted_honey_unit = round(((r.sell_pd4 + r.sell_pd5 )*100/3000),2)



                #r.need_to_buy_milk = math.ceil((use_list.m_safe_inventory - use_list.m_left_amount + r.predicted_milk_usage)/30000)

        model = Matirial
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
        for u in use_list:
            u.need_to_buy_blacktea = math.ceil((Matirial.objects.get(m_number ='1').m_safe_inventory - Matirial.objects.get(m_number ='1').m_left_amount + r.predicted_blacktea_usage)/30000)
            u.need_to_buy_milk = math.ceil((Matirial.objects.get(m_number ='2').m_safe_inventory - Matirial.objects.get(m_number ='2').m_left_amount + r.predicted_milk_usage)/5000)

            u.need_to_buy_pearl = math.ceil((Matirial.objects.get(m_number ='3').m_safe_inventory - Matirial.objects.get(m_number ='3').m_left_amount + r.predicted_pearl_usage)/3000)
            u.need_to_buy_taro = math.ceil((Matirial.objects.get(m_number ='4').m_safe_inventory - Matirial.objects.get(m_number ='4').m_left_amount + r.predicted_taro_usage)/3000)
            u.need_to_buy_honey = math.ceil((Matirial.objects.get(m_number ='5').m_safe_inventory - Matirial.objects.get(m_number ='5').m_left_amount + r.predicted_honey_usage)/3000)
    return render(request,'material.html', locals())


        # r.need_to_buy_blacktea = math.ceil((Matirial.objects.get(m_number ='1').m_safe_inventory - Matirial.objects.get(m_number ='1').m_left_amount + r.predicted_blacktea_usage)/30000)
        # r.need_to_buy_milk = math.ceil((Matirial.objects.get(m_number ='2').m_safe_inventory - Matirial.objects.get(m_number ='2').m_left_amount + r.predicted_milk_usage)/5000)
        # r.need_to_buy_pearl = math.ceil((Matirial.objects.get(m_number ='3').m_safe_inventory - Matirial.objects.get(m_number ='3').m_left_amount + r.predicted_pearl_usage)/3000)
        # r.need_to_buy_taro = math.ceil((Matirial.objects.get(m_number ='4').m_safe_inventory - Matirial.objects.get(m_number ='4').m_left_amount + r.predicted_taro_usage)/3000)
        # r.need_to_buy_honey = math.ceil((Matirial.objects.get(m_number ='5').m_safe_inventory - Matirial.objects.get(m_number ='5').m_left_amount + r.predicted_honey_usage)/3000)


        # Matirial.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount')/30000)
        # for a in use_list:
        #     a.predictday_blacktea = math.ceil((a.m_left_amount - a.m_safe_inventory)/r.predicted_blacktea_usage)


    # class Meta:                 #沒用的東西
    #     model = Matirial
    #     fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
    #     use_list = Matirial.objects.all().order_by('m_number')
    #     for a in use_list:
    #         a.predictday_blacktea = math.ceil((a.m_left_amount - a.m_safe_inventory)/r.predicted_blacktea_usage)
    # return render(request,'material.html', locals())



# month_list = DailyRecord.objects.dates('sell_date', 'month')
        # for results.sell_date in month_list:
        #     print(results)

        # spring = DailyRecord.objects.filter(sell_date__range=(spring_start_date, spring_end_date))
        #  for s in spring :
        #      spring_result_pd1 = s.sell_pd1*0.9
        #      print(spring_result_pd1)




# def inventory(request):
#     if request.method == 'POST':
#         form = TodaySellForm(request.POST)
#         if form.is_valid():
#             new_record = form.save()
#             return HttpResponseRedirect('/inventory/' + str(new_record.pk))
#     form = TodaySellForm()
#     return render(request, 'inventory.html', {'form': form})



    # return render(request,'inventory_cal.html', locals())

    #  if request.method == "POST":#如果是以POST的方式才處理
    #      sell_date = request.POST['輸入日期']    #取得表單輸入資料
    #      sell_pd1 = request.POST['濃厚奶茶 銷量：']
    #      sell_pd2 = request.POST['濃厚小芋圓奶茶 銷量：']
    #      sell_pd3 = request.POST['濃厚珍珠奶茶 銷量：']
    #      sell_pd4 = request.POST['特濃蜂蜜牛奶 銷量：']
    #      sell_pd5 = request.POST['蜂蜜珍珠鮮奶 銷量：']
    #      sellrecord = DailyRecord.objects.create(sell_date=sell_date, sell_pd1=sell_pd1, sell_pd2=sell_pd2, sell_pd3=sell_pd3, sell_pd4=sell_pd4, sell_pd5=sell_pd5)
    #      sellrecord.save()                      #寫入資料庫
    #      return redirect('/inventory/')       #重導到<index.html>網頁
    #  else:
    #     message = '請輸入資料(資料不作驗證)'
    #  return render(request, "inventory.html", locals())
