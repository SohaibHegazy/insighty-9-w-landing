from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def convert_home(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        data = pd.read_excel(excel_file)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="converted.csv"'
        data.to_csv(path_or_buf=response, index=False)
        
        return response
    
    return render(request, 'convert/convert_home.html')
