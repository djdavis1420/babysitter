from src.models.babysitter import Babysitter
from src.models.family import Family
from src.models.job import Job


def validate_input(expected_type, prompt):
    response = None
    while type(response) is not expected_type:
        response = input(prompt)
        try:
            if expected_type == int and int(response) > 0:
                response = int(response)
            elif expected_type == float and float(response) > 0:
                response = float(response)
            elif expected_type == str:
                continue
            else:
                raise ValueError
        except ValueError:
            print('That input is not valid. Try again.')
    return response


print('-' * 100)
print('Babysitter Payment Calculator')
print('Please see the README for basic assumptions.')
print('-' * 100)

babysitter_name = validate_input(str, 'What is your name? ')
babysitter_start_time = validate_input(int, 'What is your start time? ')
babysitter_end_time = validate_input(int, 'What is your end time? ')
babysitter = Babysitter(babysitter_name, babysitter_start_time, babysitter_end_time)

family_name = validate_input(str, 'What is the client\'s family name? ')
family_rates_of_pay = validate_input(int, 'How many rates of pay does this family offer? Please enter 2 or 3. ')
family_standard_rate = validate_input(float, 'What is their standard rate of pay? ')
family_overtime_rate = validate_input(float, 'What is their overtime rate of pay? ')
family_standard_rate_limit = validate_input(int, 'At what time does standard pay end and overtime pay begin? ')
if family_rates_of_pay == 3:
    family_alternate_rate = validate_input(float, 'What is their alternate rate of pay? ')
    family_overtime_rate_limit = validate_input(int, 'At what time does overtime pay end and alternate pay begin? ')
    family = Family(family_name, family_standard_rate, family_overtime_rate, family_alternate_rate)
    family.hour_schedule['standard_rate_limit'] = family_standard_rate_limit
    family.hour_schedule['overtime_rate_limit'] = family_overtime_rate_limit
else:
    family = Family(family_name, family_standard_rate, family_overtime_rate)
    family.hour_schedule['standard_rate_limit'] = family_standard_rate_limit

job_start_time = validate_input(int, 'What time does this job start? ')
job_end_time = validate_input(int, 'What time does this job end? ')
job = Job(job_start_time, job_end_time)

try:
    job.parse_hours(babysitter, family)
    job.calculate_total_pay(family)
    total_pay = '${:,.2f}'.format(job.total_pay)
    print('This job will pay ' + total_pay + '.')
except ValueError:
    print('The job hours are not valid based upon your working hours.')
