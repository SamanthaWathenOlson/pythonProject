from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.account_dao.account_dao_imp import AccountDAOImp
from objects.account_class_info import Account

account_dao = AccountDAOImp()


def test_create_account_success():
    test_account = Account(0, 32867495, 34569847, 500.00)
    result = account_dao.create_account(test_account)
    assert result.account_id != 0


def test_catch_non_unique_id():
    test_account = Account(1, 32867521, 34569947, 300.00)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


def test_get_account_info_by_id_success():
    result = account_dao.get_account_information_by_id(1)
    assert result.account_id == 1


def test_get_account_using_non_existent_id():
    try:
        account_dao.get_account_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_update_account_by_id_success():
    previous_account_name = Account(1, 56792300, 34569947, 300.00)
    result = account_dao.update_account_by_id(previous_account_name)
    assert result.account_name == "Jennifer"


def test_update_account_using_non_existent_id():
    try:
        previous_account_name = Account(0, 56792300, 34569947, 120.69)
        account_dao.update_account_by_id(previous_account_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_delete_account_by_id_success():
    result = account_dao.delete_account_by_id(1)
    assert result


def test_delete_account_with_non_existent_id():
    try:
        account_dao.delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the i d given: please try again!"