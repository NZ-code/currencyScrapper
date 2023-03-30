
import helpers



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exchanges = helpers.get_all_exchanges('EUR')
    helpers.save_exchanges_to_csv(exchanges)

