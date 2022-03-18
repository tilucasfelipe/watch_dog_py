import socket   # Permite a realização de operações relacionadas a rede, como por exemplo, retornar IP
import os       # Permite realizar interações com o S.O
import sys      #
import logging  # Permite realizar operações de logging
import time     # Permite realizar operações relacionas ao tempo, como hora, min, seg, etc..
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers import Observer

# Criando a classe responsável pelos retornos de eventos
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event): # Dispara evento de criação de arquivos
        print(f'O arquivo {event.src_path} foi criado por user {os.getlogin()}, IP {socket.gethostbyname(socket.gethostname())}.')

    @staticmethod
    def on_modified(event): # Dispara evento de modificacao de arquivos
        print(f'O arquivo {event.src_path} foi modificado por user {os.getlogin()}, IP {socket.gethostbyname(socket.gethostname())}.')
        # TODO
        # Realizar uma tratativa específica para cada tipo de modificação

    @staticmethod
    def on_deleted(event): # Dispara evento de exclusao de arquivos
        print(f'O arquivo {event.src_path} foi deletado por user {os.getlogin()}, IP {socket.gethostbyname(socket.gethostname())}.')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    keepAlive = Observer()
    keepAlive.schedule(event_handler, path, recursive=True)
    keepAlive.start()

alteraArquivo = Handler()
observer = Observer()
observer.schedule(alteraArquivo, os.getcwd(), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()