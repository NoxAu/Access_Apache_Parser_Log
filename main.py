import setup

if __name__ == "__main__":
    print("Launching the application\n")
    setup.create_app()
    print("\nStopping the application")
    setup.close_app()