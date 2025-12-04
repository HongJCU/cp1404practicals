"""
Wikipedia lookup program
CP1404 Practical — Using the wikipedia package
"""

import wikipedia


def main():
    print("Wikipedia Page Lookup\n")

    while True:
        title = input("Enter page title: ").strip()

        if title == "":
            print("Thank you.")
            break

        try:
            # Attempt to get a page without autosuggest changing the title
            page = wikipedia.page(title, autosuggest=False)

            print(page.title)
            print(page.summary[:500] + "...")   # limit summary output
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])   # show first 10 options

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            # Other unexpected issues (network, encoding, etc.)
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
