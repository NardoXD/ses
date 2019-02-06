import boto3
from email.message import EmailMessage
from email.utils import make_msgid
from urllib.request import urlopen
from string import Template

client_ses = boto3.client('ses')

# response = client_ses.create_custom_verification_email_template(
#     TemplateName='TemplatePrueba',
#     FromEmailAddress='no-reply@spotcloud.io',
#     TemplateSubject='Asunto del template',
#     TemplateContent='<html><head></head><body style="font-family:sans-serif;"><h1 style="text-align:center">Ready to start sending email with ProductName?</h1><p>We here at Example Corp are happy to have you on board! There\'s just one last step to complete before you can start sending email. Just click the following link to verify your email address. Once we confirm that you\'re really you, we\'ll give you some additional information to help you get started with ProductName.</p></body></html>',
#     SuccessRedirectionURL='https://spotcloud.io',
#     FailureRedirectionURL='https://spotcloud.io/Nosotros.html'
# )

# response2 = client_ses.send_custom_verification_email(
#     EmailAddress='lopezcesar292@gmail.com',
#     TemplateName='TemplatePrueba'
# )

# print(response2)

html = Template("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html style="width:100%;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;"> <head> <meta charset="UTF-8"> <meta content="width=device-width, initial-scale=1" name="viewport"> <meta name="x-apple-disable-message-reformatting"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta content="telephone=no" name="format-detection"> <title>Nuevo correo electrónico</title><!--[if (mso 16)]> <style type="text/css"> a{text-decoration: none;}</style><![endif]--> <link href="https://fonts.googleapis.com/css?family=Lato:400,400i,700,700i" rel="stylesheet"> <style type="text/css">@media only screen and (max-width:600px){p, ul li, ol li, a{font-size:16px!important; line-height:150%!important}h1{font-size:30px!important; text-align:center; line-height:120%!important}h2{font-size:26px!important; text-align:center; line-height:120%!important}h3{font-size:20px!important; text-align:center; line-height:120%!important}h1 a{font-size:30px!important}h2 a{font-size:26px!important}h3 a{font-size:20px!important}.es-menu td a{font-size:16px!important}.es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a{font-size:16px!important}.es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a{font-size:16px!important}.es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a{font-size:12px!important}*[class="gmail-fix"]{display:none!important}.es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3{text-align:center!important}.es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3{text-align:right!important}.es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3{text-align:left!important}.es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img{display:inline!important}.es-button-border{display:block!important}a.es-button{font-size:20px!important; display:block!important; border-width:15px 25px 15px 25px!important}.es-btn-fw{border-width:10px 0px!important; text-align:center!important}.es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right{width:100%!important}.es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header{width:100%!important; max-width:600px!important}.es-adapt-td{display:block!important; width:100%!important}.adapt-img{width:100%!important; height:auto!important}.es-m-p0{padding:0px!important}.es-m-p0r{padding-right:0px!important}.es-m-p0l{padding-left:0px!important}.es-m-p0t{padding-top:0px!important}.es-m-p0b{padding-bottom:0!important}.es-m-p20b{padding-bottom:20px!important}.es-mobile-hidden, .es-hidden{display:none!important}.es-desk-hidden{display:table-row!important; width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important}.es-desk-menu-hidden{display:table-cell!important}table.es-table-not-adapt, .esd-block-html table{width:auto!important}table.es-social{display:inline-block!important}table.es-social td{display:inline-block!important}}#outlook a{padding:0;}.ExternalClass{width:100%;}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:100%;}.es-button{mso-style-priority:100!important;text-decoration:none!important;}a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}.es-desk-hidden{display:none;float:left;overflow:hidden;width:0;max-height:0;line-height:0;mso-hide:all;}</style> </head> <body style="width:100%;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;"> <div class="es-wrapper-color" style="background-color:#F4F4F4;"><!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"><v:fill type="tile" color="#f4f4f4"></v:fill></v:background><![endif]--> <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;"> <tr class="gmail-fix" height="0" style="border-collapse:collapse;"> <td style="padding:0;Margin:0;"> <table width="600" cellspacing="0" cellpadding="0" border="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td cellpadding="0" cellspacing="0" border="0" style="padding:0;Margin:0;line-height:1px;min-width:600px;" height="0"> <img src="https://esputnik.com/repository/applications/images/blank.gif" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;max-height:0px;min-height:0px;min-width:600px;width:600px;" alt="" width="600" height="1"> </td></tr></table> </td></tr><tr style="border-collapse:collapse;"> <td valign="top" style="padding:0;Margin:0;"> <table class="es-header" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:#EC6D64;background-repeat:repeat;background-position:center top;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0;background-color:#333333;" bgcolor="#333333" align="center"> <table class="es-header-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#333333;" width="600" cellspacing="0" cellpadding="0" bgcolor="#333333" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="Margin:0;padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:20px;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="580" valign="top" align="center" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="Margin:0;padding-left:10px;padding-right:10px;padding-top:25px;padding-bottom:25px;"> <img src="cid:$retail_logo" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" class="adapt-img" width="350"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0;background-color:#333333;" bgcolor="#333333" align="center"> <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600" cellspacing="0" cellpadding="0" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;background-color:#FFFFFF;border-radius:4px;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff"> <tr style="border-collapse:collapse;"> <td align="center" style="Margin:0;padding-bottom:5px;padding-left:30px;padding-right:30px;padding-top:35px;"> <h1 style="Margin:0;line-height:48px;mso-line-height-rule:exactly;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;font-size:40px;font-style:normal;font-weight:normal;color:#111111;"><strong>Notificación de seguridad</strong><br></h1> </td></tr><tr style="border-collapse:collapse;"> <td bgcolor="#ffffff" align="center" style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:20px;padding-right:20px;"> <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0px;border-bottom:1px solid #FFFFFF;background:rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff"> <tr style="border-collapse:collapse;"> <td class="es-m-txt-l" bgcolor="#ffffff" align="center" style="Margin:0;padding-bottom:15px;padding-top:20px;padding-left:30px;padding-right:30px;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:18px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:27px;color:#666666;">Se ha detectado a una persona cuyo rasgos físicos son parecidos a:</p></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"> <tr style="border-collapse:collapse;"> <td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:30px;padding-right:30px;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="540" valign="top" align="center" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:18px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:27px;color:#696969;text-align:center;"><strong>Nombre</strong>: Lorem ipsum<br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:18px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:27px;color:#696969;text-align:center;"><strong>Acción cometida</strong>: Robo a mano armada<br></p></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"> <tr style="border-collapse:collapse;"> <td align="left" style="Margin:0;padding-bottom:10px;padding-top:20px;padding-left:30px;padding-right:30px;"><!--[if mso]><table width="540" cellpadding="0" cellspacing="0"><tr><td width="260" valign="top"><![endif]--> <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"> <tr style="border-collapse:collapse;"> <td class="es-m-p20b" width="260" align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:18px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:27px;color:#000000;"><strong>Persona detectada</strong></p></td></tr></table> </td></tr></table> <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;"> <tr style="border-collapse:collapse;"> <td width="260" align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:18px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:27px;color:#000000;"><strong>Persona registrada</strong></p></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;padding-bottom:30px;padding-left:30px;padding-right:30px;"><!--[if mso]><table width="540" cellpadding="0" cellspacing="0"><tr><td width="260" valign="top"><![endif]--> <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"> <tr style="border-collapse:collapse;"> <td class="es-m-p20b" width="260" align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <img class="adapt-img" src="cid:$img_current" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="260"></td></tr></table> </td></tr></table> <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;"> <tr style="border-collapse:collapse;"> <td width="260" align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <img class="adapt-img" src="cid:$img_saved" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="260"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0;background-color:#F4F4F4;" bgcolor="#f4f4f4" align="left"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="Margin:0;padding-top:15px;padding-bottom:15px;padding-left:20px;padding-right:20px;"> <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0px;border-bottom:0px solid #F4F4F4;background:rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;border-radius:4px;background-color:#111111;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#111111"> <tr style="border-collapse:collapse;"> <td class="es-m-txt-l" bgcolor="#000000" align="left" style="padding:0;Margin:0;padding-left:30px;padding-right:30px;padding-top:35px;"> <h2 style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#FFFFFF;">Nota importante</h2> </td></tr><tr style="border-collapse:collapse;"> <td class="es-m-txt-l" bgcolor="#000000" style="Margin:0;padding-top:20px;padding-left:30px;padding-right:30px;padding-bottom:40px;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;line-height:24px;color:#666666;text-align:justify;"><strong>VISION RETAIL</strong>, <strong>VISION RETAIL LITE</strong>, <strong>VISION RETAIL ENTERPRISE</strong>, son marcas registradas de <strong>SPOT Technologies El Salvador S.A de C.V</strong>, el uso de <strong>VISION RETAIL</strong> en su versión con el ad-on <strong>SURVEILLANCE</strong> es de ayuda y soporte para la prevención del robo, <strong>VISION RETAIL</strong> ayuda a las organizaciones a atrapar a los ladrones de tiendas, identificar el robo de empleados y detener la contracción. Por medio de análisis facial se realiza el enrolamiento de sospechosos y al ser identificados se lanza una alerta. <strong>SPOT Technologies El Salvador S.A de C.V</strong> no se hace responsable del mal uso del sistema, es meramente una herramienta de ayuda para la prevención de pérdidas de inventario, las acciones que se tomen con el sospechoso luego de la alerta son bajo responsabilidad del cliente.<br></p></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600" cellspacing="0" cellpadding="0" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="Margin:0;padding-top:15px;padding-bottom:15px;padding-left:20px;padding-right:20px;"> <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td style="padding:0;Margin:0px;border-bottom:1px solid #F4F4F4;background:rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#D83F3A;" width="600" cellspacing="0" cellpadding="0" bgcolor="#d83f3a" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="600" valign="top" align="center" style="padding:0;Margin:0;"> <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;border-radius:4px;" width="100%" cellspacing="0" cellpadding="0"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;padding-top:30px;padding-left:30px;padding-right:30px;"> <h3 style="Margin:0;line-height:24px;mso-line-height-rule:exactly;font-family:lato, 'helvetica neue', helvetica, arial, sans-serif;font-size:20px;font-style:normal;font-weight:normal;color:#FFFFFF;">¿Necesitas ayuda?<br></h3> </td></tr><tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;padding-bottom:30px;padding-left:30px;padding-right:30px;"> <span style="font-size:16px;color:#FFFFFF;">Escríbenos a support@spotcloud.io</span></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;"> <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600" cellspacing="0" cellpadding="0" bgcolor="transparent" align="center"> <tr style="border-collapse:collapse;"> <td align="left" style="Margin:0;padding-bottom:15px;padding-top:25px;padding-left:30px;padding-right:30px;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td width="540" valign="top" align="center" style="padding:0;Margin:0;"> <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> <tr style="border-collapse:collapse;"> <td align="center" style="padding:0;Margin:0;padding-top:25px;padding-bottom:25px;"> <img class="adapt-img" src="https://ogtkb.stripocdn.email/content/guids/CABINET_be5a5ce2a0326e13b9ab6745d9ebbeb0/images/28541548948904655.png" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="150"></td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> </td></tr></table> </div></body></html>""")
retail_logo = 'https://s3.amazonaws.com/spot-resources/logo_retail_pro.png'
spot_logo = 'https://s3.amazonaws.com/spot-resources/logospot.png'
key = 'img/00-00-00-00-00-00/sospechosos/2019-01-25T09_25_40.346215.jpg'
key_saved = 'img/00-00-00-00-00-00/sospechosos/2019-01-28T11_54_48.39866%260.jpg'
base_img = Template('https://s3.amazonaws.com/fernandoprueba/$key')

msg = EmailMessage()
msg['From'] = 'no-reply@spotcloud.io'
msg['To'] = 'lopezcesar292@gmail.com'
msg['Subject'] = 'Alerta sobre actividad sospechosa LOGRADO!! :V'

img_retail_logo = urlopen(retail_logo).read()
img_spot_logo = urlopen(spot_logo).read()
img_saved = urlopen(base_img.safe_substitute(key=key_saved)).read()
img_current = urlopen(base_img.safe_substitute(key=key)).read()

obj_retail_logo = make_msgid()
obj_spot_logo = make_msgid()
obj_img_current = make_msgid()
obj_img_saved = make_msgid()

msg.add_alternative(html.safe_substitute(retail_logo=obj_retail_logo[1:-1],
                                         spot_logo=obj_spot_logo[1:-1],
                                         img_current=obj_img_saved[1:-1],
                                         img_saved=obj_img_current[1:-1]), subtype='html')

msg.get_payload()[0].add_related(img_retail_logo, 'image', 'utf-8', cid=obj_retail_logo)
msg.get_payload()[0].add_related(img_spot_logo, 'image', 'base64_codec', cid=obj_spot_logo)
msg.get_payload()[0].add_related(img_current, 'image', 'base64_codec', cid=obj_img_current)
msg.get_payload()[0].add_related(img_saved, 'image', 'base64_codec', cid=obj_img_saved)

response = client_ses.send_raw_email(
    Source='no-reply@spotcloud.io',
    Destinations=['lopezcesar292@gmail.com'],
    RawMessage={
        'Data': msg.as_string(),
    }
)
