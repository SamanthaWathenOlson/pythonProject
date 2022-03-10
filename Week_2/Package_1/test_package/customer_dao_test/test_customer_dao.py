from customer_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from objects.customer_name import CustomerId

customer_dao = CustomerDAOInterface()

def test_create_customer_id_success():
    test_customer = CustomerId(0, "Samantha", "Wathen")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0

def test_catch__non_unique_id():
    test_customer = CustomerId(1, "Christopher", "Abraham")
    result = customer_dao.create_customer_id(test_customer)
    assert result.customer_id != 1

"""Get customer id tests"""

def test_get_customer_id_by_id_success():
    result = customer_dao.get_customer_information_by_id()
    assert result.customer_id == 1

def test_get_customer_using_non_existant_id():
    try:
        customer_dao.get_customer_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given. Please try again."

"""update customer id tests"""

def test_update_customer_information_by_id():
    new_customer_name = CustomerId(1, "Gary", "Sheldon")
    result = customer_dao.update_customer_id(new_customer_name)
    assert result.customer_name == "Underwear"
    pass

def test_update_customer_using_non_existent_id():
    try:
        new_customer_name = CustomerId(0, "Underwear", "Sheldon")
        customer_dao.update_customer_id(0)(new_customer_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given. Please try again."


"""Delete customer id tests"""

def test_delete_customer_information_by_id_success():
    result = customer_dao.delete_customer_id(1)
    assert result

def test_delete_customer_with_non_existent_id():
    try:
        result = customer_dao.delete_customer_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given. Please try again."