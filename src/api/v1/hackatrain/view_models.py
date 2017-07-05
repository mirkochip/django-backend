from api.v1.hackatrain.models import DeveloperInfo


class SimplePostViewModel(object):

    def save_developer_info(self, data):
        DeveloperInfo(
            name=data['name'],
            city=data['city']
        ).save()

    def get_developers_info(self):
        return DeveloperInfo.objects.all()
