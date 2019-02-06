import boto3

client_ses = boto3.client('ses')
#
# response = client_ses.create_custom_verification_email_template(
#     TemplateName='TemplatePrueba',
#     FromEmailAddress='no-reply@spotcloud.io',
#     TemplateSubject='Asunto del template',
#     TemplateContent='<html><head></head><body style="font-family:sans-serif;"><h1 style="text-align:center">Ready to start sending email with ProductName?</h1><p>We here at Example Corp are happy to have you on board! There\'s just one last step to complete before you can start sending email. Just click the following link to verify your email address. Once we confirm that you\'re really you, we\'ll give you some additional information to help you get started with ProductName.</p></body></html>',
#     SuccessRedirectionURL='https://spotcloud.io',
#     FailureRedirectionURL='https://spotcloud.io/Nosotros.html'
# )

response2 = client_ses.send_custom_verification_email(
    EmailAddress='gerardolopezbarrientos@hotmail.com',
    TemplateName='TemplatePrueba'
)

print(response2)