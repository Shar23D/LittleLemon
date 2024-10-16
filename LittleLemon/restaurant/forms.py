from django.forms import ModelForm, DateInput, TimeInput
from .models import Booking

# Add loading form data in the booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'reservation_date': DateInput(attrs={'type': 'date'}),
            'reservation_time': TimeInput(attrs={'type': 'time'}),
        }