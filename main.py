from classes.store import Store
from classes.shop import Shop
from classes.request import Request
from utils import load_script, load_log


def main():
    store = Store({
        "миндаль": 16,
        "шоколадки": 23,
        "велосипеды": 7
    })
    shop = Shop({
        "шоколадки": 6,
        "велосипеды": 2,
        "торты": 1
    })

    print(load_script("greetings"))
    print(load_script("inst"))
    print(load_script("action1"))
    print(load_script("action1/req"))
    print(load_script("action2"))
    print(load_script("action2/req"))
    print(load_script("store/state"))
    print(store.get_items())
    print(load_script("shop/state"))
    print(shop.get_items())
    print(load_script("for/end"))
    print(load_script("start"))

    while True:
        req = input().lower()
        if req == "завершить":
            print(load_script("end"))
            break
        print(load_log("check/req"))
        request = Request(req)
        try:
            if not request.is_incorrect(shop, store):
                print(f'{load_log("info/req")}\n{request}')
        except ValueError:
            print(load_log('req/error'))
            continue
        if request.to == 'магазин':
            shop.add(request.product, request.amount)
            store.remove(request.product, request.amount)
        elif request.to == 'склад':
            store.add(request.product, request.amount)
            shop.remove(request.product, request.amount)
        else:
            print(load_log('loc/error'))
            continue

        print(load_script("store/state"))
        print(store.get_items())
        print(load_script("shop/state"))
        print(shop.get_items())


if __name__ == "__main__":
    main()
