from utils.read_env import read_env as env

def main():
    values = env()
    print(values)


if __name__ == '__main__':
    main()