"""Auto-generated file, do not edit by hand. HR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HR = PhoneMetadata(id='HR', country_code=385, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{5,8}|[89]\\d{6,8}', possible_length=(6, 7, 8, 9), possible_length_local_only=(6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{7}|(?:2[0-3]|3[1-5]|4[02-47-9]|5[1-3])\\d{6,7}', example_number='12345678', possible_length=(8, 9), possible_length_local_only=(6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:01\\d|[1259]\\d{2}|7(?:[0679]\\d|51)|8\\d{1,2})\\d{5}', example_number='921234567', possible_length=(8, 9)),
    toll_free=PhoneNumberDesc(national_number_pattern='80[01]\\d{4,6}', example_number='800123456', possible_length=(7, 8, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='6(?:[01]\\d{0,2}|[459]\\d{2})\\d{4}', example_number='611234', possible_length=(6, 7, 8)),
    personal_number=PhoneNumberDesc(national_number_pattern='7[45]\\d{6}', example_number='74123456', possible_length=(8,)),
    uan=PhoneNumberDesc(national_number_pattern='(?:62\\d?|72)\\d{6}', example_number='62123456', possible_length=(8, 9)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(1)(\\d{4})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([2-5]\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2-5]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(6[01])(\\d{2})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['6[01]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([67]\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[67]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(80[01])(\\d{2})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(80[01])(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)