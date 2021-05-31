# Developed by Amresh Ranjan.

from plyer import notification

heading = 'Desktop Notifier!'

mes = 'This is My Personal Message Notifier!'

notification.notify(title= heading,
                    message= mes,
                    app_icon = None,
                    timeout= 12,
                    toast=False)
