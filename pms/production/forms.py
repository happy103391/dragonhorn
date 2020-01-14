from django import forms
from pms.production.models import DailyRecord

class TodaySellForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]  