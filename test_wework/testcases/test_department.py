from unittest import TestCase

from test_wework.api.department import Department


class TestDepartment(TestCase):
    department=Department()

    def test_list(self):
        #todo:此处可以通过外部传递参数 比如yaml
        assert self.department.list('2').get("errcode")==0


    def test_create(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_update(self):

        self.fail()
