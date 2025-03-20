from io import BytesIO
import pandas as pd
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from statistic.models import LossRecords


# Create your views here.
class LossRecordsListView(TemplateView):
    template_name = 'statistic/temp_lossrecords_list.html'

class PaymentStatsView(TemplateView):
    template_name = 'statistic/payment_stats.html'


class ReportView(LoginRequiredMixin, View):
    report_types = {
        'tactical': {
            'name': 'Тактическая сводка',
            'file_type': 'xlsx'
        },
        'financial': {
            'name': 'Финансовый отчет',
            'file_type': 'xlsx'
        }
    }

    def get(self, request):
        return render(request, 'statistic/report_form.html', {
            'report_types': self.report_types.items()
        })

    def post(self, request):
        report_type = request.POST.get('report_type')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        if not date_from or not date_to:
            return HttpResponse("Необходимо указать обе даты", status=400)

        try:
            data = LossRecords.objects.filter(
                date__gte=date_from,
                date__lte=date_to
            ).select_related('soldier', 'equipment_type', 'battle_zone')

            if not data.exists():
                return HttpResponse("Нет данных за выбранный период", status=404)

            report_data = []
            for item in data:
                report_data.append({
                    'Дата': item.date.strftime("%Y-%m-%d"),
                    'Фамилия': item.soldier.last_name,
                    'Имя': item.soldier.first_name,
                    'Техника': item.equipment_type.name,
                    'Количество': item.quantity,
                    'Награда за единицу': item.equipment_type.reward,
                    'Общая сумма': item.quantity * item.equipment_type.reward,
                    'Зона боев': item.battle_zone.name
                })

            df = pd.DataFrame(report_data)
            output = BytesIO()

            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Данные')

                # Добавляем итоги
                if report_type == 'financial':
                    summary = df.groupby('Техника').agg({
                        'Количество': 'sum',
                        'Общая сумма': 'sum'
                    }).reset_index()
                    summary.to_excel(writer, index=False, sheet_name='Итоги')

            output.seek(0)
            filename = f"{self.report_types[report_type]['name']}_{date_from}_{date_to}.xlsx"
            return FileResponse(output, as_attachment=True, filename=filename)

        except Exception as e:
            return HttpResponse(f"Ошибка генерации отчета: {str(e)}", status=500)