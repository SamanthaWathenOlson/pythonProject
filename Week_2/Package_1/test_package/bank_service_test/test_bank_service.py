from customer_exceptions.bad_customer_info import BadCustomerInfo
from dal_layer.customer.dao.customer_imp import CustomerDAOImp
from objects.customer_id import CustomerId
from team_services.team_service_imp import TeamServiceImp

team_dao = CustomerDAOImp()
team_service = TeamServiceImp(customer_dao)
duplicate_team_name = CustomerId(0, "Tamara", "Green")
#duplicate_city_name = CustomerId(0, "name is fine", )
Non_string_customer_name = CustomerId(0, 13.8, "city is fine")
duplicate_team_name_update = CustomerId(0, "Tamara", "Green")
#duplicate_city_name_update = CustomerId(0, "name is fine", )
Non_string_customer_name_update = CustomerId(0, 13.8, "city is fine", True)

def test_check_no_duplicate_names_create_team():
    try:
        team_service.service_create_customer(duplicate_customer_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) =="This team already exits in the database"

#def test_check_no_duplicate_cities_create_team():
#    try:
#        team_service.service_create_team(duplicate_customer_name)
#        assert False
#    except BadCustomerInfo as e:
#        assert str(e) == "This team already exits in the database"

def test_catch_non_string_city_create_team():
    try:
    team_service.service_create_team(duplicate_customer_name)
    assert False
except BadCustomerInfo as e:
    assert str(e) == "This team already exits in the database"

def test_catch_non_string_team_name_create_team():
    try:
        team_service.service_create_team(duplicate_customer_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This team already exits in the database"

# select team tests
def test_catch_non_numeric_id():
    try:
        team_service.service_create_team("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This team already exits in the database"

#update customer

def test_check_no_duplicate_names_update_team():
    try:
        team_service.service_create_customer(duplicate_customer_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) =="This team already exits in the database"

def test_check_no_duplicate_cities_update_team():
    try:
        team_service.service_create_team(duplicate_customer_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This team already exits in the database"

def test_catch_non_string_city_update_team():
    try:
    team_service.service_create_team(non_string_city_update)
    assert False
except BadCustomerInfo as e:
    assert str(e) == "This team already exits in the database"

def catch_non_string_team_name_update_team():
    try:
        team_service.service_create_team(duplicate_customer_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This team already exits in the database"
# delete team tests
def test_catch_non_numeric_id_delete_team():
    try:
        team_service.service_create_team("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This team already exits in the database"