import mailtrap as mt

mail = mt.Mail(
               sender   =mt.Address(email ="Mail-MACS@demomailtrap.co",
                                    name  ="Maximo Carranza"),
               to       =[mt.Address(email="usau_calidad01@minedu.gob.pe")],
               subject  ="Esto es el asunto",
               text     ="Este es el cuerpo del mensaje",
               category ="Integration Test",
)

client = mt.MailtrapClient("32fdc8f58f72070342df8be48dcc3a3c")
response = client.send(mail)

print(response)