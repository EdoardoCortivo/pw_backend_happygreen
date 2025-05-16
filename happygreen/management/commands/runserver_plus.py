import os
from django.core.management.commands.runserver import Command as RunserverCommand
from ngrok import ngrok

class Command(RunserverCommand):
    help = "Avvia il server Django e apre un tunnel ngrok"

    def run(self, **options):
        print(os.environ.get("NGROK_AUTHTOKEN"))
        ngrok.set_auth_token(os.environ.get("NGROK_AUTHTOKEN"))
        public_url = ngrok.connect(self.addr, bind_tls=True)
        print(f" * ngrok tunnel disponibile all'indirizzo: {public_url}")
        print(" * Ricorda di aggiungere questo URL ai tuoi webhook o servizi esterni, se necessario.")
        super().run(**options)
