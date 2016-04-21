
"""
Date/time pickers. Needs `eonasdan-bootstrap-datetimepicker`.
Based on https://github.com/nkunihiko/django-bootstrap3-datetimepicker
"""

from string import ascii_lowercase
from django.forms import DateTimeInput, DateInput, TimeInput
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from random import choice
from django.utils import formats, six


widget_template = '''<input id='{id:s}' {attrs:s} />
<script type="text/javascript">
	$(function () {{
		$('#{id:s}').datetimepicker({{
			format: '{format:s}'
		}});
	}});
</script>'''
#todo: YYYY-MM-DD HH:mm


FORMAT_MAP = {'DDD': r'%j',
	'DD': r'%d',
	'MMMM': r'%B',
	'MMM': r'%b',
	'MM': r'%m',
	'YYYY': r'%Y',
	'YY': r'%y',
	'HH': r'%H',
	'hh': r'%I',
	'mm': r'%M',
	'ss': r'%S',
	'a': r'%p',
	'ZZ': r'%z',
}


class PickerWidget:
	@classmethod
	def conv_dtformat_py2js(cls, format):
		for js, py in FORMAT_MAP.items():
			format = format.replace(py, js)
		return format

	def render(self, name, value, attrs=None):
		DateTimePicker._counter = getattr(DateTimePicker, '_counter', 0) + 1
		input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
		if value:
			input_attrs['value'] = force_text(self._format_value(value))
		input_attrs['type'] = input_attrs.get('type', 'text')
		input_attrs['class'] = ('form-control ' + input_attrs.get('class', '')).strip()
		input_attrs = dict([(key, conditional_escape(val)) for key, val in input_attrs.items()])
		id = 'pick_{0:s}'.format(''.join(choice(ascii_lowercase) for k in range(12)))
		format = self.conv_dtformat_py2js(formats.get_format(self.format_key)[0])
		html = widget_template.format(id=id, attrs=flatatt(input_attrs), format=format)
		return mark_safe(force_text(html))


class DateTimePicker(PickerWidget, DateTimeInput):
	pass


class DatePicker(PickerWidget, DateInput):
	pass


class TimePicker(PickerWidget, TimeInput):
	pass


