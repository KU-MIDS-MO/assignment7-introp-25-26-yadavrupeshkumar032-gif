
def safe_call(func, a, b):
    try:
        return True, func(a,b), None

    except ZeroDivisionError:
        return False, None, "ZeroDivisionError"

    except TypeError:
        return False, None, "TypeError"

    except ValueError:
        return False, None, "ValueError"

    except IndexError:
        return False, None, "IndexError"

    except KeyError:
        return False, None, "KeyError"
    
