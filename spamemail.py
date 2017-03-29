from email.mime.text import MIMEText
from email.header import Header
from dns import resolver
import smtplib
import threading
def addr_verify(email_address,i):
    # email_address = 'example@example.com'

    # Step 1: Check email
    # Check using Regex that an email meets minimum requirements, throw an error if not
    addressToVerify = email_address
    # match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    #
    # if match == None:
    #     print('Bad Syntax in ' + addressToVerify)
    #     raise ValueError('Bad Syntax')

    # Step 2: Getting MX record
    # Pull domain name from email address
    domain_name = email_address.split('@')[1]

    # get the MX record for the domain
    records = resolver.query(domain_name, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # Step 3: ping email server
    # check if the email address exists

    # Get local server hostname
    host = 'superjack5'#socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('admin@du.edu')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        log('Y')
        log(message)
        with open('validaddress.txt','a') as f:
            f.write(addressToVerify+','+str(i)+'\n')
    else:
        log('N')
        log(message)
def log(msg):
    print(msg)
    with open('log.txt','a') as f:
        f.write(str(msg))

def send():
    # 第三方 SMTP 服务
    mail_host = "127.0.0.1"  # 设置服务器
    mail_user = "superjack@gmail.com"  # 用户名
    # mail_pass = "ddtuauwmqygjdcfe"  # 口令
    mail_pass="test"
    sender = 'superjack@gmail.com'
    receivers = ['superjack1@gmail.com','418586403@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msg="""
     今晚放学别走!12sss
    """
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("Notice", 'utf-8')
    message['To'] = Header(receivers[0], 'utf-8')

    subject = 'excited'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()

        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.set_debuglevel(2)
        smtpObj.login(mail_user, mail_pass)
        a=smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)

def filesplit(filepath):
    """分割文件,按照配置文件的分段上传part大小来分割文件"""
    partnum = 0
    inputfile = open(filepath, 'rb')  # open the fromfile
    while True:
        chunk = inputfile.read(10 * 1024 * 1024)
        if not chunk:  # check the chunk is empty
            break
        partnum += 1
        newfilename = filepath + ('part%04d' % partnum)
        fileobj = open(newfilename, 'wb')  # make partfile
        fileobj.write(chunk)  # write data into partfile
        fileobj.close()
    return partnum
# addr_verify('hao.wu@illinois.edu', 0)
def runtest(file):
    i=0
    with open(file,'r') as f:
        for line in f.readlines():
            try:
                i+=1
                addr_verify(line.rstrip(),i)
            except:
                continue

if __name__=='__main__':
    for i in range(1,5):
        threading.Thread(target=lambda :runtest('illinoisnames.txtpart000'+str(i))).start()
    # filesplit('c:/email_spammer/illinoisnames.txt')
# addr_verify('fu.chen@du.edu')

# myemail='anazone@foxmail.com'
# mypwd='ddtuauwmqygjdcfe'