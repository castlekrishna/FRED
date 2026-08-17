from .runtime.bootstrap import Bootstrap

def main():
    bootstarp = Bootstrap()

    bootstarp.initialize()
    bootstarp.start()
    bootstarp.shutdown()

if __name__ == "__main__":
    main()