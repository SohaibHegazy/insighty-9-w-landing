from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def graph_home(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(csv_file.name, csv_file)
        file_url = fs.url(filename)

        logger.debug(f"File uploaded: {filename} at {file_url}")

        # Read the CSV file
        data = pd.read_csv(fs.path(filename))

        # Plot the data using Seaborn or Matplotlib
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data)
        plt.title('CSV Data Visualization')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Save the plot to a file in the media directory
        plot_filename = filename.split('.')[0] + '.png'
        plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
        plt.savefig(plot_path)

        logger.debug(f"Plot saved: {plot_path}")

        # Delete the uploaded file
        fs.delete(filename)

        logger.debug(f"Uploaded file deleted: {filename}")

        # Render the graph_home template with the plot
        return render(request, 'graph/graph_home.html', {'plot_url': settings.MEDIA_URL + plot_filename})

    return render(request, 'graph/graph_home.html')
