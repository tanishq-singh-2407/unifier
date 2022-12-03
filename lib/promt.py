def ask_message(message: str, minLength: int = 1, maxLength: int = None, default=None) -> str:
    ans = ""

    while True:
        ans = input(message)

        if maxLength and len(ans) > maxLength:
            print("Length of characters exceded (limit {0})".format(maxLength))

        elif len(ans) < minLength:
            print("String must contain min {0} characters".format(minLength))

            if default:
                return default

        else:
            break

    return ans

def ask_enum(message: str, enum: list[str], default=None):
    ans = ""

    while True:
        ans = input(message)

        if ans in list:
            return ans

        return default