from django.http import HttpResponse
from django.views.generic import View

from BillofLading.utils import render_to_pdf #created in step 4
import datetime

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Bill_Of_Lading_%s.pdf" %("1234567")
            content = "inline; filename='%s'" %(filename)
            
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")