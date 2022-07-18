#
# Задание №3: Рефакторинг кода
#

import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#
# Определение глобальных переменных и констант
#

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"
LOGIN = 'login@gmail.com'
PASSWORD = 'qwerty'

TEST_MESSAGE = 'Message'
TEST_SUBJECT = 'Subject'
RECIPIENTS = ['vasya@email.com', 'petya@email.com']

# Глобальные классы и фцнкции модуля

class Mail(object):

    def __init__(self, smtp : str, imap : str, login : str, pwd : str) -> None:
        super().__init__()

        self.smtp = smtp
        self.imap = imap
        self.login = login
        self.pwd = pwd

    # end __init__()

    # отправка сообщений
    def send(self, _from: str, _to: list, _subj: str, _msg: str) -> bool:
        msg = MIMEMultipart()
        msg['From'] = _from
        msg['To'] = ', '.join(_to)
        msg['Subject'] = _subj
        msg.attach(MIMEText(_msg))

        ms = smtplib.SMTP(self.smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        try:
            ms.login(self.login, self.pwd)
        except Exception as e:
            return False
        
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()
        return True
    # end send()

    # получаем последнее письмо
    def receive(self, header = None, mail_folder = 'inbox'):
        _mail = imaplib.IMAP4_SSL(self.imap)
        # попытка установить соединение 
        try:
            _mail.login(self.login, self.pwd)
        except Exception as e:
            return e
        # получаем список папок
        _mail.list()
        _mail.select(mail_folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = _mail.uid('search', None, criterion)
        # проверяем есть ли новые сообщения
        if not data[0]:
            return 'There are no letters with current header'
        # разбираем сообщения и возвращаем текст последнего
        latest_email_uid = data[0].split()[-1]
        result, data = _mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        _mail.logout()
        return email_message
    # end receive()

# end class Mail

#
# Главная функция программы
#

def main():
    
    # инициализация класса для отправки почты
    mail = Mail(GMAIL_SMTP, GMAIL_IMAP, LOGIN, PASSWORD)

    # отправка сообщения
    mail.send(LOGIN, RECIPIENTS, TEST_SUBJECT, TEST_MESSAGE)

    # получение новой почты
    email_message = mail.receive()
    print(email_message)

# end main()

#
# Основная программа
#

if __name__ == '__main__':
    main()
