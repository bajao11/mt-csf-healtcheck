import smtplib
import os

### Change working dir ###
directory = "E:\\MTScreenshots"
checknewdir = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)
checkM1 = checknewdir + '\\OK_CSFM1.png'
checkD1 = checknewdir + '\\OK_CSFD1.png'
checkR2 = checknewdir + '\\OK_CSFR2.png'
checkE1 = checknewdir + '\\OK_CSFE1.png'

### File Validation ###
for csfList in [checkM1, checkD1, checkE1, checkR2]:
    if os.path.isfile(csfList):
        print(csfList, 'is Ok')
    else:
        print('Send Email')
        sliceString = csfList.replace('\\', ' ').replace('_', ' ').replace('.', ' ').split()
        print(sliceString)
        ### Send Email ###
        sender = 'noreply@mtalert.com'
        receivers = ['kevinjames.bajao@infor.com']
        message = 'Subject: {}\n\n{}'.format(sliceString[4] + ' is down', 'Please check the CSF of the reported stack')
        try:
            smtpObj = smtplib.SMTP('mail.infor.com')
            #smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            #smtpObj.ehlo()
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except SMTPException:
            print("Error: unable to send email")

### File Validation ###
'''
if os.path.isfile(checkM1):
    print('CSFM1 is ok')
else:
    print('Send Email')

if os.path.isfile(checkD1):
    print('CSFD1 is ok')
else:
    print('Send Email')

if os.path.isfile(checkE1):
    print('CSFE1 is ok')
else:
    print('Send Email')

if os.path.isfile(checkR2):
    print('CSFR2 is ok')
else:
    print('Send Email')
'''