from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class AboutPageView(TemplateView):
    template_name = 'about.html'

class AdminAboutmenuPageView(TemplateView):
    template_name = 'admin-about-menu.html'

class AdminAddcoursesPageView(TemplateView):
    template_name = 'admin-add-courses.html'

class AdminAdmissionenquiryPageView(TemplateView):
    template_name = 'admin-admission-enquiry.html'

class AdminAdmissionmenuPageView(TemplateView):
    template_name = 'admin-admission-menu.html'

class AdminAllcoursesPageView(TemplateView):
    template_name = 'admin-all-courses.html'

class AdminAllenquiryPageView(TemplateView):
    template_name = 'admin-all-enquiry.html'

class AdminAllmenuPageView(TemplateView):
    template_name = 'admin-all-menu.html'

class AdmissionPageView(TemplateView):
    template_name = 'admission.html'

class AllCoursesPageView(TemplateView):
    template_name = 'all-courses.html'

class AwardsPageView(TemplateView):
    template_name = 'awards.html'

class BlogdetailsPageView(TemplateView):
    template_name = 'blog-details.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'

class ContactusPageView(TemplateView):
    template_name = 'contact-us.html'

class CoursedetailsPageView(TemplateView):
    template_name = 'course-details.html'

class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class DbcoursesPageView(TemplateView):
    template_name = 'db-courses.html'

class DbexamsPageView(TemplateView):
    template_name = 'db-exams.html'

class DbprofilePageView(TemplateView):
    template_name = 'db-profile.html'

class DbtimelinePageView(TemplateView):
    template_name = 'db-time-line.html'

class DepartmentsPageView(TemplateView):
    template_name = 'departments.html'

class EventdetailsPageView(TemplateView):
    template_name = 'event-details.html'

class EventregisterPageView(TemplateView):
    template_name = 'event-register.html'

class EventsPageView(TemplateView):
    template_name = 'events.html'

class FacilitiesPageView(TemplateView):
    template_name = 'facilities.html'

class FacilitiesdetailPageView(TemplateView):
    template_name = 'facilities-detail.html'

class GalleryphotoPageView(TemplateView):
    template_name = 'gallery-photo.html'

class IndexPageView(TemplateView):
    template_name = 'index.html'

class Index2PageView(TemplateView):
    template_name = 'index-2.html'

class Index1PageView(TemplateView):
    template_name = 'index-1.html'

class ResearchPageView(TemplateView):
    template_name = 'research.html'

class SeminarPageView(TemplateView):
    template_name = 'seminar.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'