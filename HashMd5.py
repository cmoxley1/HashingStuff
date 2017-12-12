import smtplib
import logging
import hashlib
from email.mime.text import MIMEText

## setup logging
LOG_FILENAME = 'FileHashMon.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,format='%(asctime)s %(levelname)-8s %(message)s')

## hashing function MD5\

def hash_file(path):
    h = hashlib.md5();
    with open("yourfiel.txt",'rb') as file:
        chunk = 0
        while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
    return h.hexdigest()
message = hash_file("path")
str(message)


hashOrg = 'EnterYourHash'
## Compare Hash
if message == hashOrg: ## check to see if the hash has changed
    logging.info('Hash did not change') ## Log that the changed hasn't changed

else:
    ## Send email alerting that the hash has changed
    title = 'Alert!'
    msg_content = '<h2>{title}  <font color="red">File Hash has changed!!</font></h2>\n'.format(title=title)
    message = MIMEText(msg_content, 'html')
    message['From'] = 'email@domain.com'
    message['To'] = 'youremail@domain.com'
    message['Subject'] = 'File hash has changed'
    msg_full = message.as_string()
    server = smtplib.SMTP('smtp.yourRelay.com', 25)
    server.sendmail("From Addr","to_addr", msg_full )
    server.quit()
    ## Print that the hash has changed this will go away in the final version
    ## Log that the has change
    logging.info('Hash changed!')

