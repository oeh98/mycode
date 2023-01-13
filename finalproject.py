import win32com.client as win32
from datetime import datetime
import os

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.Subject = 'TEST ' + datetime.now().strftime('%#d %b %Y %H:%M')

mail.To = "elihernandez.sk@gmail.com"


attachment = mail.Attachments.Add(os.getcwd() + "\\Currencies.png")
attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "currency_img")
mail.HTMLBody = r"""
Dear Carrie,<br><br>
The highlighted of currencies exchange prices is as follow:<br><br>
<img src="cid:currency_img"><br><br>
For more details, you can check the table in the Excel file attached.<br><br>
Best regards,<br>
Daddy
"""
mail.Attachments.Add(os.getcwd() + "\\Currencies.xlsx")
mail.Send()
