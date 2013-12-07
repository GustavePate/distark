from lescalories2csv import main


def go():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for l in letters:
        url = "http://www.les-calories.com/calories-" + l + ".html"
        main(None, url, l + ".txt")


if __name__ == '__main__':
    go()
