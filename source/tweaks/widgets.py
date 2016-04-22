
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
from django.utils import formats


widget_template = '''
<div class='input-group date' id='{id:s}-wrap'>
	<input id='{id:s}' class='form-control {cls:s}' {attrs:s} />
</div>
<script type="text/javascript">
	$(function () {{
		$('#{id:s}').datetimepicker({{
			format: '{format:s}'
		}});
	}});
</script>'''

widget_start_template = '''
<div class='input-group date' id='{id:s}-wrap'>
	<input id='{id:s}' class='form-control datepicker-coupled-start {cls:s}' {attrs:s} />
</div>
<script type="text/javascript">
	$(function () {{
		$('#{id:s}').datetimepicker({{
			format: '{format:s}'
		}});
	}});
	$("#{id:s}-wrap").on("dp.change", function (e) {{
		console.log($("#{id:s}").next(".datepicker-coupled-end"));
		$("#{id:s}").next(".datepicker-coupled-end").data("DateTimePicker").minDate(e.date);
	}});
</script>'''

widget_end_template = '''
<div class='input-group date' id='{id:s}-wrap'>
	<input id='{id:s}' class='form-control datepicker-coupled-end {cls:s}' {attrs:s} />
</div>
<script type="text/javascript">
	$(function () {{
		$('#{id:s}').datetimepicker({{
			format: '{format:s}',
			useCurrent: false
		}});
	}});
	$("#{id:s}-wrap").on("dp.change", function (e) {{
		console.log($("#{id:s}").prev(".datepicker-coupled-start"));
		$("#{id:s}").prev(".datepicker-coupled-start").data("DateTimePicker").mmaxDate(e.date);
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

	# def _get_input_attrs(self, attrs, value, name, cls=''):
	# 	input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
	# 	if value:
	# 		input_attrs['value'] = force_text(self._format_value(value))
	# 	input_attrs['type'] = input_attrs.get('type', 'text')
	# 	cls = input_attrs.pop('class', '')
	# 	id = '{0:s}_{1:s}'.format(input_attrs.pop('id', ''), ''.join(choice(ascii_lowercase) for k in range(12)))
	# 	input_attrs = dict([(key, conditional_escape(val)) for key, val in input_attrs.items()])
	# 	return id, input_attrs

	template = widget_template

	def render(self, name, value, attrs=None):
		input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
		if value:
			input_attrs['value'] = force_text(self._format_value(value))
		input_attrs['type'] = input_attrs.get('type', 'text')
		cls = input_attrs.pop('class', '')
		id = '{0:s}_{1:s}'.format(input_attrs.pop('id', ''), ''.join(choice(ascii_lowercase) for k in range(12)))
		input_attrs = dict([(key, conditional_escape(val)) for key, val in input_attrs.items()])
		format = self.conv_dtformat_py2js(formats.get_format(self.format_key)[0])
		html = self.template.format(id=id, cls=cls, attrs=flatatt(input_attrs), format=format)
		return mark_safe(force_text(html))


class DateTimePicker(PickerWidget, DateTimeInput):
	pass


class DatePicker(PickerWidget, DateInput):
	pass


class TimePicker(PickerWidget, TimeInput):
	pass


class StartDatePicker(DatePicker):
	#todo: somehow the datepicker event doesn't fire
	template = widget_start_template
	# def render(self, name, value, attrs=None):
	# 	id, input_attrs = self._get_input_attrs(attrs, value, name, cls='datepicker-coupled-start')
	# 	format = self.conv_dtformat_py2js(formats.get_format(self.format_key)[0])
	# 	html = widget_start_template.format(id=id, attrs=flatatt(input_attrs), format=format)
	# 	return mark_safe(force_text(html))

class EndDatePicker(DatePicker):
	template = widget_end_template


