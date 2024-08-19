from string_utils import StringUtils


utils = StringUtils()
def test_capitilize():
    assert utils.capitilize("владимир") == "Владимир"
    assert utils.capitilize("123") == "123"
    assert utils.capitilize("  ") == "  "


def test_trim():
    assert utils.trim("   Владимир") == "Владимир"
    assert utils.trim("   777") == "777"
    assert utils.trim("  ") == ""


def test_to_list():
    assert utils.to_list("Васильев,Владимир,Александрович") == ["Васильев", "Владимир", "Александрович"]
    assert utils.to_list("11:12:13:14", ":") == ["11", "12", "13", "14"]
    assert utils.to_list("!,@,№,$,%") == ["!", "@", "№", "$", "%"]


def test_contains():
    assert utils.contains("Васильев", "В") == True
    assert utils.contains("12345678", "567") == True
    assert utils.contains("!@#$%^&", "!№$") == False


def test_delete_symbol():
    assert utils.delete_symbol("Васильев", "В") == "асильев"
    assert utils.delete_symbol("12345678", "567") == "12348"
    assert utils.delete_symbol("!@#$%^&", "!@#$") == "%^&"


def test_starts_with():
    assert utils.starts_with("Васильев", "В") == True
    assert utils.starts_with("12345678", "5") == False
    assert utils.starts_with("!@#$%^&", "!") == True


def test_end_with():
    assert utils.end_with("Васильев", "в") == True
    assert utils.end_with("12345678", "5") == False
    assert utils.end_with("!@#$%^&", "&") == True


def test_is_empty():
    assert utils.is_empty("") == True
    assert utils.is_empty("12345678") == False
    assert utils.is_empty("   ") == True


def test_list_to_string():
    assert utils.list_to_string(["Васильев, Владимир, Александрович"]) == "Васильев, Владимир, Александрович"
    assert utils.list_to_string(["1,2,3,4,5,6,7,8"]) == "1,2,3,4,5,6,7,8"
    assert utils.list_to_string(["!@#", "$%^&"], "-") == "!@#-$%^&"
