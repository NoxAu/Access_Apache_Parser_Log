import os
import subprocess

from consolecontroller import ConsoleController
from parser_1 import config
from service_log import LogService
from model import Model
from scheduler import Scheduler

def start_server():
    """Start Apache web server"""
    try:
        os.chdir("server/Apache24/bin")
        subprocess.Popen(['./httpd.exe'])
        print("Веб-сервер Apache запущен")
        os.chdir("../../../")
    except Exception as ex:
        print(f"An unexpected error occurred when starting the Apache web server: {ex}")

def stop_server():
    """Stop Apache web server"""
    try:
        subprocess.run(['TASKKILL', '/F', '/IM', 'httpd.exe', '/T'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)  # Остановить сервер
        print("Apache Web server is stopped")
    except Exception as ex:
        print(f"An unexpected error occurred when stopping the Apache web server: {ex}")

def create_app():
    """Initialize and configure the application"""
    if config['app']['start_apache_server']:
        start_server()

    model = Model()
    service = LogService(model)
    controller = ConsoleController(service, model)
    scheduler = Scheduler.create_scheduler(controller)

    controller.console_input()

def close_app():
    """Shutdown the application"""
    if config['app']['start_apache_server']:
        stop_server()