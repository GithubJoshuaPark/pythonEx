import utils

utils.show_base_name(__file__, True)

def main() -> None:
    user_name = "World"
    print(utils.greet(user_name))
    # Demonstrate emoji utility
    print("Random emojis:", end=" ")
    utils.show_random_emojis(5)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)
