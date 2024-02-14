

import requests
import openpyxl
from bs4 import BeautifulSoup

# Create a new Excel workbook and select the active sheet
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Laptops from A"

# Write headers to the first row of the Excel sheet
sheet.append(['Laptop Name', 'Price'])

# Define the URL to scrape
url = "https://www.amazon.in/s?hidden-keywords=B09V83L8H9+%7C+B09RMTMBSM+%7C+B09MM58Y7Q+%7C+B0B4JQ9X9C+%7C+B09R1L73TM+%7C+B0B1M99Y9M+%7C+B09TNY95RK+%7C+B09RZRF1PJ+%7C+B09Y5VD8N7+%7C+B098XLXDRS+%7C+B098QBT5KT+%7C+B0B1M9V5KT+%7C+B09VPV1HCG+%7C+B09NDTFY68+%7C+B09Y5V7BFH+%7C+B09M423NVT+%7C+B09N19ZMTP+%7C+B09QD3DQ49+%7C+B0B4KBCRJ3+%7C+B09W9MBS1G+%7C+B098XL8VSM+%7C+B09X5L41XH+%7C+B09Q5JGSX1+%7C+B09YTVB91N+%7C+B09DX8FZSL+%7C+B09VZ88HZY+%7C+B09V1GMW72&pf_rd_i=1320006031&pf_rd_i=1375424031&pf_rd_m=A1K21FY43GMZF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=353b3c90-bc15-4f49-a463-37efbe0c4ed4&pf_rd_p=previewPlacement_center-1&pf_rd_r=4XXFRV8WKQRAM3YB8RFG&pf_rd_r=QG2YDBQM5YEH025897HJ&pf_rd_s=center-1&pf_rd_s=merchandised-search-12&pf_rd_t=101&pf_rd_t=101&ref=s9_acss_bw_cg_PDPrint_2b1_w"
# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all laptop names and prices
names = soup.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
prices = soup.find_all("span", {"class": "a-price-whole"})

# Iterate over the laptop names and prices, and write them to the Excel sheet
for name, price in zip(names, prices):
    nm = name.get_text().strip()
    pr = price.get_text().strip()
    sheet.append([nm, pr])

# Save the Excel file with a specific name
excel.save('D:\B.TECH\PYTHON PROJECT\Laptops_from_A2')
