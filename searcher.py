import movie_service
import requests


def main():
    print_header()
    search_movie()


def print_header():
    print("----------------------------------------")
    print("           MOVIE SEARCH APP             ")
    print("----------------------------------------")
    print()


def search_movie():
    search_text = 'Press x when done'
    print(search_text)

    while search_text != 'x':
        try:
            search_text = input("What movie are you looking for? ")
            print()
            search_text = search_text.lower().strip()
            if search_text != 'x':
                results = movie_service.find_movie(search_text)
                if len(results) >= 1:
                    print("Found {} movies for {}".format(len(results), search_text))
                    print("-----------------------")
                    for idx, mv in enumerate(results):
                        print("{}. {} -- {}".format((idx + 1), mv.year, mv.title))
                else:
                    print(f"No movies found for {search_text}")
            print()
        except ValueError:
            print("Search text is required")
            print()
        except requests.exceptions.ConnectionError:
            print("Sorry, couldn't retrieve data. Check your internet connection")
        except Exception as x:
            print("Sorry, something went wrong there. Check and try again")
            print(x)

    print("....exiting")


if __name__ == '__main__':
    main()
