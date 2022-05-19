from gtp import GoToPython


def main():
    """In this version[1.0.0], We use GoToPython class to run GO commands.
    
    Unable to execute sequential commands with PIPE.
    """
    command = "subfinder -d sample.com -silent"
    gtp = GoToPython(command)
    result = gtp.run()
    print(result)


if __name__ == "__main__":
    main()