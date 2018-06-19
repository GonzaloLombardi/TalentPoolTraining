from behave import *
from selenium import webdriver


def selenium_browser_firefox(context):
    context.mercado_libre = webdriver.Firefox()


def before_all(context):
    selenium_browser_firefox(context)


@given('A Firefox driver')
def step_impl(context):
    pass


@when('Hola')
def step_impl(context):
    print "Hola hola"
    assert False


@then('Chau')
def step_impl(context):
    print "Chau chau"
