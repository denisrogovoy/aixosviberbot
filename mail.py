import smtplib
import secrets

gmail_user = secrets.email
gmail_password = secrets.email_password


def sendEmail(sendMessageToUser, securityCode, choice):
    try:
        addr_to = "To: %s\n" % (sendMessageToUser)
        htmlMailCheck = '''<!DOCTYPE html>
<html lang="uk">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Email</title>

		<style>
		.mainTable {
			width: 100%;
			height: 600px;
		}

		.smallTable {
			width: 80%;
			height: 80%;
			text-align: center;
			margin-right: auto;
			margin-left: auto;
		}

		.minionCell {
			width: 40%;
		}

		.minionPicture {
			width: 100%;
		}

		.contentHeader {
			font-family: Verdana;
			font-size: 30pt;
			color: #487a99;
			margin: 10px 0 0 0;
			border-radius: 30px 30px 0 0;
		}

		.content {
			text-align: left;
			margin: 0 0 0 10px;
			font-family: "Comic Sans MS";
			font-size: 13pt;
			color: #383838;
		}

		hr {
			margin: 20px auto 0 auto;
			border: 0; 
			height: 1px; 
			width: 80%;
			background-image: -webkit-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -moz-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -ms-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -o-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0); 
		}

		.code {
			font-family: Verdana;
			font-size: 22pt;
			color: #487a99;
		}

		.shadow {
			height: 100%;
			box-shadow: 0 0 10px #999;
			border-radius: 30px 30px 30px 30px;
			background-color: #f7f7f7;

		}

		.subFooter {
			height: 80px;
			text-align: right;

		}

		.footerPicture {
			height: 100%;
			margin: 0 5px 0 0;
		}

		</style>
	</head>
	<body>
		 <table class="mainTable">
				<tr>
				   <td>
						<table class="smallTable">
								<tr>
									<td class="minionCell"><img class="minionPicture" src="https://aixbot.s3.amazonaws.com/mail/letterWelcome.png" alt="Greatings from minion!"></td>
									<td>
										<table class="shadow">
											<tr>
												<td colspan="2"><div class="contentHeader"><b>Ласкаво просимо!</b></div><hr></td>

											</tr>
											<tr><td colspan="2">
												<div class="content"><p>Будь-ласка використайте наступний код для підтвердження свого акаунту:</p></div>
												<div class="code"><p><b>''' + str(securityCode) + '''</b></p></div>
												<div class="content"><p>Повідомлення було відправлено автоматично. Якщо повідомлення надійшло вам помилково проігноруйте його.</p></div>
											</td></tr>
											<tr>
												<td><div class="content">Гарного Вам дня,<br>Віртуальний помічник викладача</div></td>
												<td class="subFooter"><a href="viber://pa?chatURI=aixbot"><img class="footerPicture" src="https://aixbot.s3.amazonaws.com/mail/aixFooter.png" alt="Greatings from minion!"></a></td>
											</tr>
										</table>
									</td>
								</tr>
						</table>
				   </td>
				</tr>
		 </table>
	</body>
</html>'''

        htmlMailRegistration = '''<!DOCTYPE html>
<html lang="uk">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Email</title>

		<style>
		.mainTable {
			width: 100%;
			height: 600px;
		}

		.smallTable {
			width: 90%;
			height: 80%;
			text-align: center;
			margin-right: auto;
			margin-left: auto;
		}

		.minionCell {
			width: 40%;
		}

		.minionPicture {
			width: 80%;
		}

		.contentHeader {
			font-family: Verdana;
			font-size: 25pt;
			color: #487a99;
			margin: 10px 0 0 0;
			border-radius: 30px 30px 0 0;
		}

		.content {
			text-align: left;
			margin: 0 0 0 10px;
			font-family: "Comic Sans MS";
			font-size: 13pt;
			color: #383838;
		}

		hr {
			margin: 20px auto 0 auto;
			border: 0; 
			height: 1px; 
			width: 80%;
			background-image: -webkit-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -moz-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -ms-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0);
			background-image: -o-linear-gradient(left, #f0f0f0, #8c8b8b, #f0f0f0); 
		}

		.code {
			font-family: Verdana;
			font-size: 18pt;
			color: #487a99;
		}

		.shadow {
			height: 100%;
			box-shadow: 0 0 10px #999 !important;
			border-radius: 30px 30px 30px 30px;
			background-color: #f7f7f7;
			text-align: center;
		}

		.subFooter {
			height: 80px;
			text-align: right;
		}

		.footerPicture {
			height: 100%;
			margin: 0 5px 0 0;
		}

		a {
		    text-decoration: none;
		}

		.button {
			text-decoration: none;
			-webkit-transition-duration: 0.4s; /* Safari */
			transition-duration: 0.4s;
			border-radius: 5px;
			background-color: #487a99;
			text-align: center;
			color: white !important;
			font-family: Verdana;
			font-size: 16px;
			padding: 15px 32px;
		}

		.button:hover {
			background-color: #4CAF50; /* Green */
			color: white;
		}

		a {
		    color: white;
		}

		</style>
	</head>
	<body>
		 <table class="mainTable">
				<tr>
				   <td>
						<table class="smallTable">
								<tr>
									<td class="minionCell"><img class="minionPicture" src="https://aixbot.s3.amazonaws.com/mail/ups.png" alt="Greatings from minion!"></td>
									<td>
										<table class="shadow">
											<tr>
												<td colspan="2"><div class="contentHeader"><b>Упс, щось пішло не так...</b></div><hr></td>

											</tr>
											<tr><td colspan="2">
												<div class="content"><p>Ви не зараховані до курсу "AIX for beginners" у системі Moodle Education. Будь-ласка перейдіть за посиланням та зареєструйтеся:</p></div>
												<div><p><b><a class="button" href="http://aixbot.westeurope.cloudapp.azure.com/course/view.php?id=2/">Зареєструватися</a></b></p></div>
												<div class="code"><p><b>Token для реєстрації: AIX2020</b></p></div>
												<div class="content"><p>Повідомлення було відправлено автоматично. Якщо повідомлення надійшло вам помилково проігноруйте його.</p></div>
											</td></tr>
											<tr>
												<td><div class="content">Гарного Вам дня,<br>Віртуальний помічник викладача</div></td>
												<td class="subFooter"><a href="viber://pa?chatURI=aixbot"><img class="footerPicture" src="https://aixbot.s3.amazonaws.com/mail/aixFooter.png" alt="Greatings from minion!"></a></td>
											</tr>
										</table>
									</td>
								</tr>

						</table>
				   </td>
				</tr>

		 </table>
	</body>
</html>
        '''
        body = ""
        if choice:
            body = htmlMailCheck
        else:
            body = htmlMailRegistration

        email_text = "From: AIX Bot verification<aixos.bot@knu.ua>\n" + addr_to + "Subject: AIX Bot security code\n" + \
                     "MIME-Version: 1.0\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 8bit\n\n" + body

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, sendMessageToUser, email_text.encode('utf-8'))
        server.close()

        print('Email sent!')
    except Exception as e:
        print('Something went wrong...')
        print(e)