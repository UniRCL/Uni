from behave import given, when, then
from volunteer import VolunteerRegistry


@given('a volunteer named "{name}" aged {age:d}')
def step_given_volunteer(context, name, age):

    context.registry = VolunteerRegistry()
    context.name = name
    context.age = age


@when('the registration is submitted')
def step_when_registration(context):

    context.result = context.registry.register_volunteer(
        context.name,
        context.age
    )


@then('the volunteer should be registered successfully')
def step_then_success(context):

    assert context.result is True
    assert context.registry.volunteer_exists(
        context.name
    )


@then('the registration should be rejected')
def step_then_rejected(context):

    assert context.result is False


@given('volunteers "{name1}" aged {age1:d} and "{name2}" aged {age2:d} are registered')
def step_given_multiple(
    context,
    name1,
    age1,
    name2,
    age2
):

    context.registry = VolunteerRegistry()

    context.registry.register_volunteer(
        name1,
        age1
    )

    context.registry.register_volunteer(
        name2,
        age2
    )


@when('the total volunteers are counted')
def step_when_total(context):

    context.total = context.registry.total_volunteers()


@then('the total should be {expected:d}')
def step_then_total(context, expected):

    assert context.total == expected