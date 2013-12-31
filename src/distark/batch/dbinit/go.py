import argparse



def main():
    pass


if __name__ == "__main__":

    #arg parsing 1st argument shoud be a path
    parser = argparse.ArgumentParser(description=("minimal db creation"))
    parser.add_argument('--logpath', help='log directory', type=str)
    args = parser.parse_args()
    main()

