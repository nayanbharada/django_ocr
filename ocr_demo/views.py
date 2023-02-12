import cv2
import os
import pytesseract
import xlsxwriter
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from PIL import Image
from ocr_demo.models import NetworkData
from ocr_demo.serializers import NetworkDataSerializer

# Create your views here.


class ImageProcessView(GenericAPIView):
    """
    http://127.0.0.1:8000/ocr/ocr-data-store
    this api through image data get and extract
    store in table and excel file as well
    """

    def get(self, request):
        # image process start
        images = cv2.imread("image.png")
        # convert to grayscale image
        gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
        filename = "{}.jpg".format(os.getpid())
        cv2.imwrite(filename, gray)
        text = pytesseract.image_to_string(Image.open(filename))
        # image process end

        # image data cleaning
        all_table_data_extract = text.split("\n\n")[2].split("\n")
        # excel data sheet create
        workbook = xlsxwriter.Workbook('network_data.xlsx')
        worksheet = workbook.add_worksheet()
        row_num = 0
        columns = [
            "Method",
            "Category 1",
            "Category 2",
            "Category 3",
            "Category 4"
        ]

        # excel sheet in header add
        for col_num in range(len(columns)):
            worksheet.write(row_num, col_num, columns[col_num])

        # excel sheet in data add
        for table_data in all_table_data_extract[1:]:
            row_num += 1
            row_data = table_data.split(" ")
            # table in data add
            NetworkData.objects.create(method_name=row_data[0],
                                       category_one=row_data[1],
                                       category_two=row_data[2],
                                       category_three=row_data[3],
                                       category_four=row_data[4])

            worksheet.write(row_num, 0, row_data[0])
            worksheet.write(row_num, 1, row_data[1])
            worksheet.write(row_num, 2, row_data[2])
            worksheet.write(row_num, 3, row_data[3])
            worksheet.write(row_num, 4, row_data[4])
        workbook.close()
        os.remove(filename)
        return Response("Data add successfully on table and excel sheet.")


class NetworkDataListAPIView(ListAPIView):
    """
    class for getting list of NetworkData.
    """
    serializer_class = NetworkDataSerializer

    def get_queryset(self):
        return NetworkData.objects.all()
