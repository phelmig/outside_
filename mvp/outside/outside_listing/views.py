from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from .forms import LeadClosedForm, LeadRepeatForm, LeadFeedbackForm
from frontend.models import Lead, ClosingEvent, Seller
from django.contrib.auth.decorators import login_required


def calculate_rev(request):
    ret = 0.0
    u = request.user
    for ce in u.closingevent_set.all():
        ret += ce.seller.reward
    # Reward minus 15% Service Fee
    return round(ret / 1.15,2)

# Create your views here.
@login_required
def index(request):
    ctx = {"leads": Lead.objects.all().order_by('created', 'lost', 'closed', '-repeat_at'),
           "rev": calculate_rev(request)}
    return render(request, 'outside_listing/index.html',ctx)

# Create your views here.
@login_required
def map(request):
    ctx = {"leads": Lead.objects.filter(lost=False, closed=False).filter(
        Q(repeat_at__lt=timezone.now()) | Q(repeat_at__isnull=True)).order_by('created', 'closed', '-repeat_at')
        , "rev": calculate_rev(request)}
    return render(request, 'outside_listing/lead_map.html',ctx)


@login_required
def lead_detail(request,id):
    ctx = {"lead": get_object_or_404(Lead, id=id),
           "rev": calculate_rev(request)}
    return render(request, 'outside_listing/lead_detail.html',ctx)


class LeadClosedView(FormView):
    template_name = 'outside_listing/lead_closed.html'
    form_class = LeadClosedForm
    success_url = reverse_lazy('index')



    def render_to_response(self, context, **response_kwargs):
        context['lead'] = get_object_or_404(Lead,id=self.kwargs.get('id'))
        context["rev"] = calculate_rev(self.request)
        return super(LeadClosedView, self).render_to_response(context,**response_kwargs)

    def form_valid(self, form):
        # Update Lead
        # TODO: Update User
        lead = get_object_or_404(Lead,id=self.kwargs.get('id'))
        lead.closed = True
        lead.lost = False
        lead.repeat_at = None
        lead.last_visited_at = timezone.now()
        lead.last_visited_by = self.request.user
        lead.save()

        # Create Closing Event
        # TODO: Update User
        # TODO: Figure out Seller
        c = ClosingEvent()
        c.user = self.request.user
        c.lead = lead
        c.seller = Seller.objects.last()  # TODO: Map these to users?
        c.proof = form.cleaned_data.get('proof')
        c.save()

        return super(LeadClosedView, self).form_valid(form)


class LeadRepeatView(FormView):
    template_name = 'outside_listing/lead_repeat.html'
    form_class = LeadRepeatForm
    success_url = reverse_lazy('index')



    def render_to_response(self, context, **response_kwargs):
        context["rev"] = calculate_rev(self.request)
        context['lead'] = get_object_or_404(Lead,id=self.kwargs.get('id'))
        return super(LeadRepeatView, self).render_to_response(context,**response_kwargs)

    def form_valid(self, form):
        # Update Lead
        # TODO: Update User
        lead = get_object_or_404(Lead,id=self.kwargs.get('id'))

        lead.repeat_at = form.cleaned_data.get('date')
        lead.comment = form.cleaned_data.get('comment')
        lead.lost = False
        lead.last_visited_at = timezone.now()
        lead.last_visited_by = self.request.user
        lead.save()

        return super(LeadRepeatView, self).form_valid(form)

class LeadFeedbackView(FormView):
    template_name = 'outside_listing/lead_feedback.html'
    form_class = LeadFeedbackForm
    success_url = reverse_lazy('index')



    def render_to_response(self, context, **response_kwargs):
        context["rev"] = calculate_rev(self.request)
        context['lead'] = get_object_or_404(Lead,id=self.kwargs.get('id'))
        return super(LeadFeedbackView, self).render_to_response(context,**response_kwargs)

    def form_valid(self, form):
        # Update Lead
        # TODO: Update User
        # TODO: Store Feedback Event?
        lead = get_object_or_404(Lead,id=self.kwargs.get('id'))

        lead.comment = form.cleaned_data.get('comment')
        lead.lost = form.cleaned_data.get('lost')
        lead.last_visited_at = timezone.now()
        lead.last_visited_by = self.request.user
        lead.save()

        return super(LeadFeedbackView, self).form_valid(form)