def gen_confirm_code():
    code = "123456"
    return code


def send_mail(code):
    print(f"email: {code}")


def send_sms(code):
    print(f"sms: {code}")


def check(data):
    code = gen_confirm_code()
    match data["confirm"]:
        case "email":
            send_mail(code)
        case "telegram":
            send_sms(code)
        case _:
            print(f"неизвестный способ подтверждения")


if __name__ == '__main__':
    data = {
        "confirm": "email",
        "login": "user1",
        "password": "pass1",
    }
    check(data)
