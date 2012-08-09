from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from apply.models import apply_track


class ApplyResource(ModelResource):

    class Meta:
        queryset = apply_track.objects.all()
        resource_name = 'apply'
        authorization = Authorization()
