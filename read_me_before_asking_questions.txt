Hello, reader!
I'd tried to make email verification, but I didn't successed(
It's beacuse I couldn't login with smtp

I'd tried to check sending email messages in another python file, but I got the next error:

Traceback (most recent call last):
  File "C:\Code\Python\sending_email.py", line 5, in <module>
    server.login('rudenkokostya20@gmail.com', 'ybpx nvyl nnay anmx')
  File "C:\Users\FreemanKitch\AppData\Local\Programs\Python\Python312\Lib\smtplib.py", line 750, in login
    raise last_exception
  File "C:\Users\FreemanKitch\AppData\Local\Programs\Python\Python312\Lib\smtplib.py", line 739, in login
    (code, resp) = self.auth(
                   ^^^^^^^^^^
  File "C:\Users\FreemanKitch\AppData\Local\Programs\Python\Python312\Lib\smtplib.py", line 662, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (
    535, b'5.7.8 Username and Password not accepted. For more information,
    go to\n5.7.8  https://support.google.com/mail/?p=BadCredentials
    38308e7fff4ca-30be9a07204sm1391591fa.114 - gsmtp'
)

I leave this branch as a try of making email verification.