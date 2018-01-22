
# coding: utf-8

# This version of send mail sends an email through sendgrid api. This is a secured way of sending emails and the mail will not be blocked by outlook.

# In[11]:


import base64
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail, Attachment
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("dvsprojectdev@gmail.com")
subject = "test sending attachment"
to_email = Email("xie_yilin@singstat.gov.sg")
content = Content("text/html", "I'm a content example")

file_path = "DGS-extract.zip"
with open(file_path,'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()

attachment = Attachment()
attachment.content = encoded
attachment.type = "application/pdf"
attachment.filename = "test.pdf"
attachment.disposition = "attachment"
attachment.content_id = "Example Content ID"

mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print(e.read())
    exit()

print(response.status_code)
print(response.body)
print(response.headers)

