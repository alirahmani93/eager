import datetime

import requests
from django.conf import settings


class SunWayHTTPException(Exception):
    pass


error_messages = {
    '51': 'Wrong password', '52': 'Wrong username', '54': 'Empty RecipientNumber', '59': 'Empty MessageBody',
    '60': 'Currently, the SunWaySMS server is unable to respond due to high traffic.',
    '63': ('This IP is not allowed to access this users web service.'
           ' To access the IP, please add the IP from the web service section in the system.'
           ' Look at the list of verified IPs.'),
    '70': 'User Deactivated', '72': 'Wrong combination of Hour, Minute parameters',
    '73': 'Wrong combination of Year, Month, Day parameters',
    '201': 'Wrong recipients number format', '202': 'Not Enough Credit',
    '203': 'Not Enough Credit', '300': 'Message contains invalid link (The link sending agreement has not been signed)',
    '400': 'Too Many Requests, SunWaySMS throttle our server', '666': 'Service Deactivated', '777': 'IP blocked',
    '999': 'Invalid SMS Message',
}


class SunWaySmsSender:
    """
    acceptance receiver numbers type: 10(9123456789) 11(09123456789) 12(989123456789) characters,
    the eleven characters type preferred.
    multi mobile number is acceptable with separator ','
    sample request:
    > https://sms.sunwaysms.com/SMSWS/HttpService.ashx?
        service={sun way service name}

        &to={receiver}
        &message={message_str}

        &from={settings.SUN_WAY_SERVICE_LINE}
        &username={settings.SUN_WAY_USERNAME}
        &password={settings.SUN_WAY_PASSWORD}

    This implementation is based on document version 06.
    SunWaySms Documentation: https://sunwaysms.com/webservice/downloads/
    """

    def __init__(self, receiver, plain_text=None, timeout=None, sender=None, priority=0):

        self._base_url = settings.SUN_WAY_BASE_URL
        self._sun_way_from_number = sender if sender else settings.SUN_WAY_SERVICE_LINE
        self._sun_way_username = settings.SUN_WAY_USERNAME
        self._sun_way_password = settings.SUN_WAY_PASSWORD
        self._timeout = timeout or settings.SUN_WAY_TIMEOUT

        self._receiver = receiver
        self._plain_text = plain_text
        self._priority = priority
        self._headers = {}

    def __repr__(self):
        return "SunWaySMS({!r})".format(self._sun_way_from_number)

    def __str__(self):
        return "SunWaySMS({!s})".format(self._sun_way_from_number)

    def _get_params(self, service_name, message, **kwargs):
        params = {
            'service': service_name,
            'to': self._receiver,
            'message': message,
            'from': self._sun_way_from_number,
            'username': self._sun_way_username,
            'password': self._sun_way_password,
        }
        if kwargs:
            params = {**params, **kwargs}
        return params

    def _request(self, params):
        try:
            response = requests.get(self._base_url, headers=self._headers, params=params,
                                    timeout=self._timeout)

            # SunWay returns a number less than 1000 when an error occurs.
            error = error_messages.get(response.text[:4])

        except requests.exceptions.RequestException as e:
            raise SunWayHTTPException(e)

        if error is not None:
            raise ValueError(error)
        return response

    def send_single_message_to_single_number(self):
        self._request(params=self._get_params(service_name='SendArray', message=self._plain_text))

    def send_schedule(self, schedule_datetime: datetime.datetime):
        year = schedule_datetime.year
        month = schedule_datetime.month
        day = schedule_datetime.day
        hour = schedule_datetime.hour
        minute = schedule_datetime.minute
        second = schedule_datetime.second

        extra = {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minute': minute,
            'second': second,
        }
        self._request(
            params=self._get_params(service_name='SendArraySchedule', message=self._plain_text, **
            extra))

    def get_message_id(self, target_message_id):
        extra = {'CheckingMessageID': target_message_id}
        self._request(
            params=self._get_params(service_name='GetMessageID', message=self._plain_text, **
            extra))

    def get_credit(self):
        credit_value = self._request(
            params={
                'service': 'GetCredit',
                'username': self._sun_way_username,
                'password': self._sun_way_password,
            })
        return credit_value.text

    def get_user_info(self):
        user_info = self._request(
            params={
                'service': 'GetUserInfo',
                'username': self._sun_way_username,
                'password': self._sun_way_password,
            })
        return user_info.json()
